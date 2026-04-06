"""Note logic (string/fret → note name) and ASCII fretboard rendering."""

import shutil

CHROMATIC = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

FLAT_TO_SHARP = {
    "Bb": "A#", "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#",
}

# Open string notes, strings 1–6 (high-e to low-E)
OPEN_STRINGS: dict[int, str] = {
    1: "E",  # e4
    2: "B",  # B3
    3: "G",  # G3
    4: "D",  # D3
    5: "A",  # A2
    6: "E",  # E2
}

STRING_LABELS: dict[int, str] = {
    1: "e",
    2: "B",
    3: "G",
    4: "D",
    5: "A",
    6: "E",
}

# Frets 1–17 are displayed. Fret 0 = open string (no fret marker).
DISPLAY_FRETS = list(range(1, 18))  # 17 fret positions

# Each fret cell is CELL chars wide. 2 chars fits single- and double-digit fret numbers.
CELL = 3
INLAY_POSITIONS = {1, 5, 7, 9, 12, 15, 17}
MIN_TERMINAL_WIDTH = 30


def note_at(string: int, fret: int) -> str:
    """Return the note name for the given string (1–6) and fret (0–17)."""
    open_note = OPEN_STRINGS[string]
    start = CHROMATIC.index(open_note)
    return CHROMATIC[(start + fret) % len(CHROMATIC)]


def normalize_input(raw: str) -> str:
    """Normalise user input: capitalise, convert flats to sharps."""
    raw = raw.strip()
    if not raw:
        return raw
    normalised = raw[0].upper() + raw[1:].lower() if len(raw) > 1 else raw.upper()
    return FLAT_TO_SHARP.get(normalised, normalised)


def is_correct(answer: str, string: int, fret: int) -> bool:
    """Return True if the answer matches the note at string/fret."""
    return normalize_input(answer) == note_at(string, fret)


def _fret_cell(fret: int, highlighted: bool) -> str:
    """Return a CELL-wide string for one fret position."""
    if highlighted:
        # center() puts single-digit at position 1; for double-digit "15" → "15-",
        # keeping the units digit at position 1, aligned with the inlay marker.
        return str(fret).center(CELL, "-")
    return "-" * CELL


def _inlay_cell(fret: int) -> str:
    """Return a CELL-wide inlay indicator for the dots row."""
    if fret not in INLAY_POSITIONS:
        return " " * CELL
    marker = ":" if fret == 12 else "."
    # Marker at position 1 to align with centered fret numbers
    return " " + marker + " " * (CELL - 2)


def render_fretboard(highlight_string: int, highlight_fret: int) -> str:
    """Return the ASCII fretboard as a string with the given position highlighted."""
    terminal_width = shutil.get_terminal_size(fallback=(80, 24)).columns
    board_width = 2 + 1 + len(DISPLAY_FRETS) * CELL + 1  # label + | + frets + |
    if terminal_width < board_width:
        return (
            f"[Terminal too narrow: need {board_width} cols, have {terminal_width}]"
        )

    lines: list[str] = []
    open_fret = highlight_fret == 0

    for s in range(1, 7):
        is_active = s == highlight_string

        # Left label column (1 char, padded to 2 with space or nut separator)
        if is_active and open_fret:
            label = "0"
        elif open_fret:
            label = " "
        else:
            label = STRING_LABELS[s]

        # Fret cells (frets 1–17)
        fret_str = "".join(
            _fret_cell(f, is_active and f == highlight_fret) for f in DISPLAY_FRETS
        )
        lines.append(f"{label}|{fret_str}|")

    # Inlay dots row
    dots = "".join(_inlay_cell(f) for f in DISPLAY_FRETS)
    lines.append(f" |{dots}|")

    return "\n".join(lines)
