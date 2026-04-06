"""Quiz loop, input handling, scoring, and session state."""

import random
from .settings import Settings
from .fretboard import render_fretboard, is_correct, note_at, CHROMATIC

NATURALS = {"A", "B", "C", "D", "E", "F", "G"}


def pick_position(settings: Settings) -> tuple[int, int]:
    """Return a random (string, fret) from the active settings."""
    frets = settings.active_frets()
    if settings.note_set == "naturals_only":
        candidates = [
            (s, f)
            for s in settings.active_strings
            for f in frets
            if note_at(s, f) in NATURALS
        ]
        if not candidates:
            # Fallback: ignore note_set filter
            candidates = [(s, f) for s in settings.active_strings for f in frets]
    else:
        candidates = [(s, f) for s in settings.active_strings for f in frets]
    return random.choice(candidates)


def run_quiz(settings: Settings) -> None:
    """Run the interactive quiz loop."""
    correct = 0
    total = 0

    print("Guitar Notes Quiz — type the note name (e.g. A, C#, Bb). Press Ctrl-C to quit.\n")

    try:
        while True:
            string, fret = pick_position(settings)
            board = render_fretboard(string, fret)
            print(board)
            print()

            try:
                answer = input("Note? ").strip()
            except EOFError:
                break

            if not answer:
                continue

            total += 1
            correct_note = note_at(string, fret)

            if is_correct(answer, string, fret):
                correct += 1
                print(f"  Correct! ({correct_note})  [{correct}/{total}]\n")
            else:
                print(f"  Wrong — the note was {correct_note}.  [{correct}/{total}]\n")

    except KeyboardInterrupt:
        pass

    if total:
        pct = 100 * correct // total
        print(f"\nSession over: {correct}/{total} ({pct}%)")
    else:
        print("\nNo answers recorded.")
