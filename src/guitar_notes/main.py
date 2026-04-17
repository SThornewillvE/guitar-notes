"""Entry point — argument parsing and quiz launch."""

from __future__ import annotations

import argparse
import sys
from .settings import Settings, ALL_STRINGS, MAX_FRET, MIN_FRET
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
        help="Test open strings only (fret 0). Cannot be combined with --frets, --notes, or --max-fret.",
    )
    parser.add_argument(
        "--min-fret",
        type=int,
        default=MIN_FRET,
        metavar="N",
        help=f"Minimum fret to include (0–{MAX_FRET}, inclusive). Default: {MIN_FRET}.",
    )
    parser.add_argument(
        "--max-fret",
        type=int,
        default=MAX_FRET,
        metavar="N",
        help=f"Maximum fret to include (0–{MAX_FRET}, inclusive). Default: {MAX_FRET}.",
    )
    parser.add_argument(
        "--show-labels",
        action="store_true",
        default=False,
        help="Show string names (e, B, G, D, A, E) to the left of the nut. Hidden by default to avoid using them as a reference.",
    )

    args = parser.parse_args(argv)

    if args.open_strings:
        if args.frets != "all":
            parser.error("--open-strings cannot be combined with --frets (open strings are always fret 0).")
        if args.notes != "all":
            parser.error("--open-strings cannot be combined with --notes (open strings are always natural notes).")
        if args.max_fret != MAX_FRET:
            parser.error("--open-strings cannot be combined with --max-fret (open strings are always fret 0).")
        if args.min_fret != MIN_FRET:
            parser.error("--open-strings cannot be combined with --min-fret (open strings are always fret 0).")

    if not (MIN_FRET <= args.min_fret <= MAX_FRET):
        parser.error(f"--min-fret must be between {MIN_FRET} and {MAX_FRET} (got {args.min_fret}).")

    if not (MIN_FRET <= args.max_fret <= MAX_FRET):
        parser.error(f"--max-fret must be between {MIN_FRET} and {MAX_FRET} (got {args.max_fret}).")

    if args.min_fret > args.max_fret:
        parser.error(f"--min-fret ({args.min_fret}) cannot be greater than --max-fret ({args.max_fret}).")

    if args.max_fret == 0 and args.frets != "all":
        parser.error("--max-fret 0 includes only the open string; --frets cannot further restrict this.")

    return Settings(
        active_strings=args.strings,
        fret_filter=args.frets,
        note_set=args.notes,
        open_strings=args.open_strings,
        min_fret=args.min_fret,
        max_fret=args.max_fret,
        show_labels=args.show_labels,
    )


def main() -> None:
    settings = parse_args()
    run_quiz(settings)


if __name__ == "__main__":
    main()
