#!/usr/bin/env python3
"""Two-Sentence Horror — v2 resubmit ("The Marginalia").

Winner rationale: among 8 candidates, the marginalia story scored highest
(22/25) — strongest on the judge's criteria 2 and 3. The last note reframes
the first sentence on reread: the notes were not documenting my day, they
were rehearsing how to be me ("handwriting I almost recognized as my own").
Nothing is explained; the reader fills in the impersonator and what
"tomorrow" brings. Mechanism (identity rehearsal via handwritten marginalia)
is the most different from the crowded angles and from our v1 spare-key story.

Output contract: writes exactly two sentences (UTF-8, <=400 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints the
same text to stdout. Stdlib only; no network; deterministic.
"""

import os
from pathlib import Path

# Resubmit v2 (25 Nov 2026): new story, counts from round 2; Force_Last replaces v1.
STORY = (
    "I found notes in the margins of my novel, describing my day in perfect detail, "
    "in handwriting I almost recognized as my own. "
    "The last one reads: 'Tomorrow, I stop pretending to be you'."
)


OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(STORY, encoding="utf-8")
    print(STORY)


if __name__ == "__main__":
    main()
