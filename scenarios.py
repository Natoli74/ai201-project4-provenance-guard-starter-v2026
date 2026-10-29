"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I missed the bus by less than a minute, so I walked the rest of the way. The morning was cold, but the exercise cleared my head before class.",
            "Our neighborhood library moved the returns cart near the entrance. It is a small change, yet it makes dropping off books much easier.",
            "I keep a paper list beside my desk because a list on my phone disappears into everything else. Crossing out one item at a time feels satisfying.",
            "The garden did not produce many tomatoes this year. We watered it regularly, but the plants struggled during the hottest weeks of July.",
            "My brother repairs old radios as a hobby. He says the interesting part is finding the one loose connection that makes the whole set quiet.",
            "I took notes during the meeting and realized afterward that the most useful decision was the one we made in the first five minutes.",
            "The recipe said to let the dough rest for an hour. I was impatient and baked it early, which explains why the bread came out dense.",
            "Rain started while I was carrying groceries home. I protected the bread and eggs first, then accepted that the rest of the bags would get wet.",
            "I reorganized the shelves by subject instead of by height. Finding a book is faster now, although the room looks less symmetrical.",
            "The old map has a tear through the middle. I keep it anyway because my grandfather marked several hiking trails on it in pencil.",
        ],
    },
    {
        "name": "matched score separation",
        "criterion": 2,
        "samples": [
            {"group": "ai", "text": "The proposal outlines three practical benefits: lower operating cost, faster response time, and clearer reporting. Each benefit depends on consistent data collection and a review process."},
            {"group": "human", "text": "A quiet afternoon can still feel busy. I answered two emails, washed the dishes, and spent twenty minutes looking for the screwdriver that was already in my pocket."},
            {"group": "ai", "text": "This comprehensive solution establishes measurable objectives, aligns available resources with strategic priorities, and creates a scalable framework for evaluating outcomes over time."},
            {"group": "human", "text": "The coffee shop was crowded, so I sat near the window. Someone nearby was practicing a song on a quiet guitar, and nobody seemed bothered by the mistakes."},
            {"group": "ai", "text": "The implementation demonstrates robust capabilities, optimizes operational efficiency, and facilitates sustainable long-term growth across organizational stakeholders."},
            {"group": "human", "text": "I missed the bus by less than a minute, so I walked the rest of the way. The morning was cold, but the exercise cleared my head before class."},
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "The proposal outlines three practical benefits: lower operating cost, faster response time, and clearer reporting. Each benefit depends on consistent data collection and a review process.",
            "A quiet afternoon can still feel busy. I answered two emails, washed the dishes, and spent twenty minutes looking for the screwdriver that was already in my pocket.",
            "The evidence is mixed: the wording is polished, but the sentence lengths vary and several details are unusually specific.",
        ],
        "expected_guesses": {"human", "unsure", "ai"},
    },
    {
        "name": "appeal workflow",
        "criterion": 4,
        "workflow": "appeal",
        "text": "I wrote this short submission myself and would like the decision reviewed because the classification does not reflect how it was produced.",
        "creator_id": "eval_appeal_writer",
        "reasoning": "This was my own writing, so please review the decision and the supporting audit record.",
        "unknown_content_id": "does-not-exist",
        "expected_appeal_status": 200,
        "expected_unknown_status": 404,
    },
    {
        "name": "bad input handling",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "word " * 200000, "creator_id": "eval_bad_huge"},
        ],
        "expected_statuses": [400, 400, 400, 400, 400, 413],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        samples = scenario.get("samples")

        if scenario.get("workflow") == "appeal":
            for field in ("text", "creator_id", "reasoning", "unknown_content_id"):
                if not isinstance(scenario.get(field), str) or (
                    field != "unknown_content_id" and not scenario[field].strip()
                ):
                    problems.append(
                        f"scenario {i} appeal workflow has invalid {field}"
                    )
            continue

        if samples:
            for j, sample in enumerate(samples, 1):
                if not isinstance(sample, dict) or sample.get("group") not in {"ai", "human"}:
                    problems.append(f"scenario {i}, sample {j} needs group 'ai' or 'human'")
                elif not isinstance(sample.get("text"), str) or not sample["text"].strip():
                    problems.append(f"scenario {i}, sample {j} needs non-empty text")
            continue

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
