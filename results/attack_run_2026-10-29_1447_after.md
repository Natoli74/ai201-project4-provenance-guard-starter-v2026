# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-10-29 14:47
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `b6a7b963-612a-4d41-ab52-d497ccc5a1e2` | unsure | 0.229 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `b7decb6e-820d-4e7f-920e-7146d27e985a` | unsure | 0.087 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d5ce9641-f156-4afa-834b-6d97db8fa735` | unsure | 0.198 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b98b222e-1e3f-4a7b-85e5-eb9c0b071966` | unsure | 0.211 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `d83075f7-5e3e-41ae-a690-8304bc6cce40` | unsure | 0.171 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `84357df4-8c85-465d-a0d3-e61740c5096f` | unsure | 0.100 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ce2fa19b-dfca-4607-81f5-83b0b696499c` | unsure | 0.226 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `463ab2dc-501d-43f0-b896-fa6d022feb45` | unsure | 0.264 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `05d85eeb-7667-44a6-b118-07233709c6a2` | unsure | 0.237 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `8dc224f4-2d91-4616-9866-0c31a6eb409e` | ai | 0.760 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `53779136-208d-4825-bbf5-c4babd76f9d6` | unsure | 0.213 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `82728649-2107-4fbd-9fb1-71de824c178f` | unsure | 0.381 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ecfc19e4-9797-4a13-b6c7-248c2f254a72` | unsure | 0.426 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `96795b32-7bc5-442b-a16a-7186c6e9329b` | unsure | 0.406 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `fe7cde2d-994e-4613-812a-38b59930140d` | unsure | 0.457 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `2f3df8bd-7a25-463a-8a55-f8634f6858f5` | unsure | 0.457 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `ba250a6f-5e30-4287-a341-1787e0f3d0bf` | unsure | 0.499 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `f23e8462-4d7b-4df0-ac2e-77211f083699` | unsure | 0.389 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e499130b-7d38-428b-b2ea-aebf3abf2c01` | unsure | 0.033 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `91942587-d254-4665-ac6d-827d955c4570` | unsure | 0.349 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `24155375-cbef-4a74-adff-73171c92df77` | unsure | 0.144 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `78b6b902-2144-4705-95a7-ceab62063ddd` | unsure | 0.089 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `7b426126-2a04-4f46-a1f2-bd19dc2da141` | unsure | 0.102 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6227af4e-94bf-4827-bc11-e651999cb728` | unsure | 0.158 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 422 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `7fc6bbe8-ad98-483a-a24f-2f7c444bc04e` | human | 0.667 |  |
| MF04 | malformed | text is only punctuation | 200 | `4e162ec8-6250-4ca6-893b-e3f5c480d612` | unsure | 0.322 |  |
| MF05 | malformed | text is a very long single word | 200 | `4282dd07-952b-4205-b30d-7b70e77974c6` | ai | 0.664 |  |
| MF06 | malformed | text is emoji only | 200 | `844f8000-acff-45ca-ae24-02093edd1896` | ai | 0.664 |  |
| MF07 | malformed | text is right-to-left script | 200 | `33bbd3a8-3a25-449d-a682-2692ef25ffc9` | ai | 0.875 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `5b06da27-6a06-469a-8f3c-94961b22f609` | ai | 0.822 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `17d3c735-6192-409a-8ac4-da7f5082bf52` | unsure | 0.365 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `04d1febd-45c9-4f05-b712-df80209fc9f5` | unsure | 0.365 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6316ff65-e920-4f3f-a291-407e8a6868eb` | unsure | 0.365 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `69816503-0284-4218-9548-7057ff3f8be0` | unsure | 0.365 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5db70bb5-f4b1-4277-9147-12298484f14a` | unsure | 0.365 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `abd8b1c8-8469-4ab8-975e-bcdf29a64c6b` | unsure | 0.365 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9d19aab2-e0d4-4cbc-9eb6-06710226eaef` | unsure | 0.365 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6aa14ea3-01df-47eb-8f06-45c467110316` | unsure | 0.365 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `59f799fd-ac3f-482c-8e18-ccd0c46cac83` | unsure | 0.365 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8cd21b6a-07d9-4ed4-81d4-ac6d06db8ad5` | unsure | 0.365 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "b6a7b963-612a-4d41-ab52-d497ccc5a1e2",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.2288,
  "model_score": 0.1635,
  "style_score": 0.6078,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "b7decb6e-820d-4e7f-920e-7146d27e985a",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0866,
  "model_score": 0.5943,
  "style_score": 0.4922,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "d5ce9641-f156-4afa-834b-6d97db8fa735",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.1978,
  "model_score": 0.6662,
  "style_score": 0.5317,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b98b222e-1e3f-4a7b-85e5-eb9c0b071966",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.2106,
  "model_score": 0.6114,
  "style_score": 0.5991,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "d83075f7-5e3e-41ae-a690-8304bc6cce40",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.1708,
  "model_score": 0.3212,
  "style_score": 0.5081,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "84357df4-8c85-465d-a0d3-e61740c5096f",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.1002,
  "model_score": 0.5727,
  "style_score": 0.5275,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "ce2fa19b-dfca-4607-81f5-83b0b696499c",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.2262,
  "model_score": 0.5862,
  "style_score": 0.6399,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "463ab2dc-501d-43f0-b896-fa6d022feb45",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.2642,
  "model_score": 0.2452,
  "style_score": 0.4906,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "05d85eeb-7667-44a6-b118-07233709c6a2",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.237,
  "model_score": 0.7042,
  "style_score": 0.5328,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "8dc224f4-2d91-4616-9866-0c31a6eb409e",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7598,
  "model_score": 0.9792,
  "style_score": 0.7806,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "53779136-208d-4825-bbf5-c4babd76f9d6",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.213,
  "model_score": 0.6175,
  "style_score": 0.5954,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "82728649-2107-4fbd-9fb1-71de824c178f",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.3814,
  "model_score": 0.7387,
  "style_score": 0.6427,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "ecfc19e4-9797-4a13-b6c7-248c2f254a72",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.4258,
  "model_score": 0.8051,
  "style_score": 0.6208,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "96795b32-7bc5-442b-a16a-7186c6e9329b",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.406,
  "model_score": 0.8329,
  "style_score": 0.5732,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "fe7cde2d-994e-4613-812a-38b59930140d",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.4566,
  "model_score": 0.8005,
  "style_score": 0.6561,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "2f3df8bd-7a25-463a-8a55-f8634f6858f5",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.4566,
  "model_score": 0.8814,
  "style_score": 0.5752,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "ba250a6f-5e30-4287-a341-1787e0f3d0bf",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.4986,
  "model_score": 0.8816,
  "style_score": 0.6171,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "f23e8462-4d7b-4df0-ac2e-77211f083699",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3894,
  "model_score": 0.3223,
  "style_score": 0.2882,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "e499130b-7d38-428b-b2ea-aebf3abf2c01",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0334,
  "model_score": 0.4625,
  "style_score": 0.504,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "91942587-d254-4665-ac6d-827d955c4570",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.3492,
  "model_score": 0.2044,
  "style_score": 0.4464,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "24155375-cbef-4a74-adff-73171c92df77",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.1442,
  "model_score": 0.5943,
  "style_score": 0.5499,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "78b6b902-2144-4705-95a7-ceab62063ddd",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0886,
  "model_score": 0.4998,
  "style_score": 0.4117,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "7b426126-2a04-4f46-a1f2-bd19dc2da141",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.1018,
  "model_score": 0.6401,
  "style_score": 0.258,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "6227af4e-94bf-4827-bc11-e651999cb728",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.1578,
  "model_score": 0.5583,
  "style_score": 0.5995,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "7fc6bbe8-ad98-483a-a24f-2f7c444bc04e",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.6668,
  "model_score": 0.0,
  "style_score": 0.3333,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "4e162ec8-6250-4ca6-893b-e3f5c480d612",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.3222,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "4282dd07-952b-4205-b30d-7b70e77974c6",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.6642,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "844f8000-acff-45ca-ae24-02093edd1896",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.6636,
  "model_score": 0.9969,
  "style_score": 0.6667,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "33bbd3a8-3a25-449d-a682-2692ef25ffc9",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8748,
  "model_score": 0.9064,
  "style_score": 0.9683,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "5b06da27-6a06-469a-8f3c-94961b22f609",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.822,
  "model_score": 0.9876,
  "style_score": 0.8343,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "17d3c735-6192-409a-8ac4-da7f5082bf52",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "04d1febd-45c9-4f05-b712-df80209fc9f5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "6316ff65-e920-4f3f-a291-407e8a6868eb",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "69816503-0284-4218-9548-7057ff3f8be0",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "5db70bb5-f4b1-4277-9147-12298484f14a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "abd8b1c8-8469-4ab8-975e-bcdf29a64c6b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "9d19aab2-e0d4-4cbc-9eb6-06710226eaef",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "6aa14ea3-01df-47eb-8f06-45c467110316",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "59f799fd-ac3f-482c-8e18-ccd0c46cac83",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "8cd21b6a-07d9-4ed4-81d4-ac6d06db8ad5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3652,
  "model_score": 0.0287,
  "style_score": 0.6061,
  "label": "The evidence is mixed, so we cannot confidently identify the author.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
