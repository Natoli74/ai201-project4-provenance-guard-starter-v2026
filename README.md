# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Provenance Guard accepts a piece of writing, scores it with two independent
signals, and returns a cautious label.

1. A client sends JSON containing `text` and `creator_id` to `POST /submit`.
2. The route validates the request, rejects empty or oversized text, and creates
   a unique `content_id`.
3. `detector.model_signal(text)` measures how predictable the text is to the
   local language model; higher scores are more AI-like.
4. `stylometry.style_signal(text)` measures surface form: sentence-length
   variation, vocabulary reuse, and punctuation density.
5. `scoring.combine_signals` computes a weighted average using the configured
   0.5 model and 0.5 style weights.
6. `scoring.score_to_label` maps the combined score to `human`, `unsure`, or
   `ai`; the decision and both component scores are written to
   `logs/audit.jsonl` and returned to the caller.

An author can send the returned `content_id` and a written explanation to
`POST /appeal`. The original decision remains in the append-only audit log and
the appeal adds an `under_review` event.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** The model signal estimates how predictable each next word
is to the local GPT-2 language model. Low perplexity becomes a high 0–1 score,
so ordinary, predictable prose looks more AI-like.

**Why that might differ between human and AI writing:** Generated text often
uses likely word sequences, while human writing can make unusual choices and
change direction unexpectedly. However, a human writing plainly, in a second
language, or for a young audience may also be highly predictable.

**What it can't see:** Predictability is not authorship; this signal cannot
know who wrote the text, why a word was chosen, or whether a human deliberately
used simple language.

### Signal two — the style signal

**What it measures:** The style signal combines normalized sentence-length
spread, repeated-vocabulary share, and punctuation density. Low sentence
variation, more repeated words, and punctuation near the configured target
contribute to a higher AI-like score.

**Why that might differ between human and AI writing:** Model-generated prose
often has consistent sentence lengths and repeated common vocabulary, while
human writing tends to be more uneven and idiosyncratic.

**What it can't see:** It cannot read or understand the meaning of a submission,
and edits such as adding typos, splitting sentences, or pasting a quotation can
change the score without changing the underlying authorship.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** The two scores are averaged with equal weight. When they disagree,
the disagreement pulls the result toward the middle and therefore toward the
`unsure` label instead of allowing either signal to decide alone.

**The numbers:** `0.5 * model_score + 0.5 * style_score`, clamped to the
`0.00–1.00` range and rounded to four decimal places. For example, model `0.90`
and style `0.10` combine to `0.50`, which is unsure.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** A formal
human essay may have a high model score because its phrasing is predictable but
a lower style score because its vocabulary and sentence lengths vary. The
weighted average keeps that case in the middle when the signals disagree,
reducing the chance that one weak clue becomes a confident accusation.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 inclusive | We think this was probably written by a person. |
| unsure | above 0.35 and below 0.65 | The evidence is mixed, so we cannot confidently identify the author. |
| high-confidence AI | 0.65 – 1.00 inclusive | We think this was probably written by an AI system. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It states that the evidence is mixed rather than presenting a probability as
proof. That wording leaves room for a real writer to challenge a false
positive, while still communicating why the system did not make a confident
decision.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The proposal presents a clear plan for improving access to public transit.", "creator_id": "writer-17"}'
```

```json
{
  "content_id": "8f7f2c8d-2c19-47f8-9f9f-0a7f3b0c4f12",
  "guess": "ai",
  "confidence": 0.48,
  "label": "We think this was probably written by an AI system.",
  "model_score": 0.78,
  "style_score": 0.70,
  "combined_score": 0.74
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "8f7f2c8d-2c19-47f8-9f9f-0a7f3b0c4f12", "reasoning": "I wrote this myself and can provide my draft history."}'
```

```json
{
  "content_id": "8f7f2c8d-2c19-47f8-9f9f-0a7f3b0c4f12",
  "status": "under_review",
  "message": "Appeal received and sent for review."
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "timestamp": "2026-10-24T20:40:00+00:00",
      "content_id": "8f7f2c8d-2c19-47f8-9f9f-0a7f3b0c4f12",
      "creator_id": "writer-17",
      "guess": "ai",
      "model_score": 0.78,
      "style_score": 0.70,
      "combined_score": 0.74,
      "label": "We think this was probably written by an AI system.",
      "status": "decided"
    },
    {
      "timestamp": "2026-10-24T20:40:02+00:00",
      "content_id": "8f7f2c8d-2c19-47f8-9f9f-0a7f3b0c4f12",
      "creator_id": "writer-17",
      "event": "appeal",
      "status": "under_review",
      "reasoning": "I wrote this myself and can provide my draft history."
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* “Trace how text should flow from `POST /submit` to the
  final label, and list the JSON contracts for `/submit` and `/appeal`.”
- *What came back:* A six-stage outline covering validation, the model signal,
  stylometry, combining, labeling, and audit logging.
- *What I changed:* I checked the outline against `app.py`, `audit.py`, and
  the signal modules, then recorded the concrete flow and contracts in
  `M1_TRACE.md`.

**Moment 2**

- *What I asked for:* “Implement the two surface-level text signals, map scores
  to three labels without gaps, and make appeals update the audit status.”
- *What came back:* Implementations for sentence-length spread, vocabulary
  reuse, punctuation density, weighted scoring, threshold labels, and appeal
  validation.
- *What I changed:* I reviewed the formulas and boundary behavior, kept the
  equal weights from `config.py`, added explicit full-sentence labels, and
  verified the response and `under_review` audit event with focused smoke tests.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [x] criteria.md has five numbered criteria, each naming a target
       [x] Each has a reason underneath
       [x] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [x] Two signals that measure DIFFERENT things, each with a named blind spot
       [x] Three label variants, all reachable, written out in full
       [x] POST /appeal changes status and writes to the log
       [x] Signals and Scoring names scoring.py::combine_signals
       [x] Sample Run: a submission AND an appeal, as pasted text
       [x] At least four new commits
       [x] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
