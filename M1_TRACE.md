# Milestone 1 Trace

## Six-step text flow

1. **Receive the submission.** A client sends `POST /submit` with a JSON
   object containing the text to evaluate and the creator's identifier. Flask
   parses the request body into `payload`.
2. **Extract and identify the content.** The route reads `text` and
   `creator_id`, creates a unique `content_id`, and validates that the
   submission contains usable text before attempting to score it.
3. **Calculate the model signal.** `detector.model_signal(text)` measures how
   predictable the writing is to the local language model. A higher score
   means the text looks more AI-like to this signal.
4. **Calculate and combine the signals.** `stylometry.style_signal(text)`
   measures writing shape, including sentence-length variation, vocabulary
   reuse, and punctuation. `scoring.combine_signals(model_score, style_score)`
   combines the two 0–1 scores into one score, preserving the meaning that a
   higher value is more AI-like.
5. **Map the score to a decision.** `scoring.score_to_label(combined_score)`
   returns a machine-readable `guess` (`human`, `unsure`, or `ai`) and the
   reader-facing `label` text. The response and audit entry retain both
   component scores and the combined score.
6. **Persist and return the final label.** `audit.log_decision(...)` writes
   the decision, scores, creator, content ID, and status to the append-only
   audit log. The route returns the JSON result to the client, where the
   caller sees the final label. If the writer disputes it, `POST /appeal`
   uses the same `content_id` to append an `under_review` event without
   erasing the original decision.

## `POST /submit` JSON contract

### Request

```http
POST /submit
Content-Type: application/json
```

```json
{
  "text": "The text to evaluate.",
  "creator_id": "writer-123"
}
```

| Field | Type | Required | Description |
|---|---|---:|---|
| `text` | string | yes | Writing to score. It must not be missing or empty. |
| `creator_id` | string | yes | Identifier used for auditability and, when enabled, rate limiting. |

### Successful response

```json
{
  "content_id": "3d7c2f9e-0f8c-4b8c-8f06-9d7b7f6d3b2a",
  "guess": "unsure",
  "confidence": 0.52,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "model_score": 0.61,
  "style_score": 0.43,
  "combined_score": 0.52
}
```

`content_id` is unique per submission. `model_score`, `style_score`,
`combined_score`, and `confidence` are numbers from 0.0 through 1.0.
`guess` is one of `human`, `unsure`, or `ai`; `label` is the complete
human-readable explanation associated with that guess.

Invalid JSON or missing/empty required fields should return a 4xx JSON error
instead of producing a decision or a misleading success response. A typical
error shape is:

```json
{
  "error": "invalid_request",
  "message": "text must be a non-empty string"
}
```

## `POST /appeal` JSON contract

### Request

```http
POST /appeal
Content-Type: application/json
```

```json
{
  "content_id": "3d7c2f9e-0f8c-4b8c-8f06-9d7b7f6d3b2a",
  "reasoning": "I wrote this text myself and can provide my draft history."
}
```

| Field | Type | Required | Description |
|---|---|---:|---|
| `content_id` | string | yes | ID returned by the original `/submit` response. |
| `reasoning` | string | yes | The writer's explanation for challenging the decision. |

### Successful response

```json
{
  "content_id": "3d7c2f9e-0f8c-4b8c-8f06-9d7b7f6d3b2a",
  "status": "under_review",
  "message": "Appeal received and sent for review."
}
```

The appeal appends an audit entry with `event: "appeal"` and
`status: "under_review"`. It does not overwrite the original decision or
automatically rescore the text. An unknown `content_id`, missing reasoning, or
invalid JSON should return a 4xx JSON error and should not create an appeal
entry.

## False-positive scenario

Maya is a real human writing a short scholarship response in her second
language. She deliberately uses common words and short, grammatically regular
sentences because she is trying to be clear and avoid vocabulary she is unsure
about. The model signal finds this predictable, and the regular sentence
length and punctuation also make the style signal look AI-like. Their
combined score crosses the AI threshold, so `/submit` returns `guess: "ai"`.

This is a false positive: the system has flagged a human writer. Maya submits
the returned `content_id` and explains that the response is hers, attaching
her outline and earlier drafts in the review process. `POST /appeal` records
the reasoning and changes the audit trail to `under_review`; the original
score remains visible so reviewers can understand both the initial mistake and
the appeal.
