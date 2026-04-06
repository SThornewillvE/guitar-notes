"""Entry point — argument parsing and quiz launch."""

from __future__ import annotations

import argparse
import sys
from .settings import Settings, ALL_STRINGS
from .quiz import run_quiz


def parse_args(argv: list[str] | None = None) -> Settings:
    parser = argparse.ArgumentParser(
        prog="guitar_notes",
        description="Terminal fretboard note quiz for guitar practice.",
    )
    parser.add_argument(
        "--strings",
        nargs="+",
        type=int,
        choices=ALL_STRINGS,
        default=ALL_STRINGS,
        metavar="N",
        help="Active strings to test (1=high-e … 6=low-E). Default: all.",
    )
    parser.add_argument(
        "--frets",
        choices=["all", "inlay", "non_inlay"],
        default="all",
        help="Which frets to include. Default: all.",
    )
    parser.add_argument(
        "--notes",
        choices=["all", "naturals_only"],
        default="all",
        help="Restrict to natural notes only. Default: all.",
    )
    parser.add_argument(
        "--open-strings",
        action="store_true",
        default=False,
        help="Test open strings only (fret 0). Cannot be combined with --frets or --notes.",
    )

    args = parser.parse_args(argv)

    if args.open_strings:
        if args.frets != "all":
            parser.error("--open-strings cannot be combined with --frets (open strings are always fret 0).")
        if args.notes != "all":
            parser.error("--open-strings cannot be combined with --notes (open strings are always natural notes).")

    return Settings(
        active_strings=args.strings,
        fret_filter=args.frets,
        note_set=args.notes,
        open_strings=args.open_strings,
    )


def main() -> None:
    settings = parse_args()
    run_quiz(settings)


if __name__ == "__main__":
    main()
