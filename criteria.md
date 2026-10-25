# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Of 10 clearly human submissions, at most 1 may receive the high-confidence AI
label in each evaluation trial.

**Why this target:** A false accusation harms a real writer more than allowing
some AI text to pass, so the system should strongly favor avoiding false
positives. Allowing 1 in 10 leaves room for an imperfect detector while making
the human-safety requirement measurable.



---

## 2.

Across a matched set of clearly AI-written and clearly human-written samples,
the mean combined score for the AI set must be at least 0.20 higher than the
mean combined score for the human set.

**Why this target:** A measurable gap shows that the signals provide useful
separation rather than producing nearly identical scores for every text. A
0.20 gap is demanding enough to reveal weak scoring while still allowing
overlap for ambiguous writing and model variability.



---

## 3.

All three labels—`human`, `unsure`, and `ai`—must be reachable by at least one
valid submission, with the returned `guess` and reader-facing `label` matching
the corresponding score range.

**Why this target:** A label that cannot be produced is dead code and prevents
the service from expressing the uncertainty its thresholds are meant to
represent. Requiring all three labels preserves both confident decisions and a
safer middle outcome for borderline cases.



---

## 4.

For every valid submitted `content_id`, a valid appeal with non-empty
`reasoning` must return HTTP 200, append an appeal event to the audit log, and
leave the item with status `under_review`; an unknown `content_id` must return
a 4xx response without creating an appeal event.

**Why this target:** Writers need a reliable way to challenge a wrong
classification, and the append-only record must make that challenge visible
without erasing the original decision. Rejecting unknown IDs prevents
orphaned appeals and keeps the audit trail tied to real submissions.



---

## 5.

Empty, whitespace-only, missing, or non-string `text` must receive a 4xx JSON
error without scoring or creating a decision log entry, while an enormous
submission of at least 1,000,000 characters must be rejected or safely capped
without a 5xx response.

**Why this target:** Invalid input should produce a clear client error rather
than a crash, misleading label, or unexplained audit record. Bounding enormous
text protects latency and memory, while accepting either rejection or an
explicit safe cap keeps the service predictable under stress.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
