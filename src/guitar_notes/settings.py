"""Settings model for the quiz session."""

from dataclasses import dataclass, field
from typing import Literal

# All frets available (0 = open string, up to fret 17)
MAX_FRET = 17
ALL_FRETS = list(range(MAX_FRET + 1))
INLAY_FRETS = [0, 5, 7, 9, 12, 15, 17]
NON_INLAY_FRETS = [f for f in ALL_FRETS if f not in INLAY_FRETS]

# Strings numbered 1–6 high-e to low-E (guitarist convention)
ALL_STRINGS = [1, 2, 3, 4, 5, 6]

NoteSet = Literal["all", "naturals_only"]
FretFilter = Literal["all", "inlay", "non_inlay"]


@dataclass
class Settings:
    active_strings: list[int] = field(default_factory=lambda: list(ALL_STRINGS))
    fret_filter: FretFilter = "all"
    note_set: NoteSet = "all"
    open_strings: bool = False
    max_fret: int = MAX_FRET

    def active_frets(self) -> list[int]:
        if self.open_strings:
            return [0]
        if self.fret_filter == "inlay":
            frets = INLAY_FRETS
        elif self.fret_filter == "non_inlay":
            frets = NON_INLAY_FRETS
        else:
            frets = ALL_FRETS
        return [f for f in frets if f <= self.max_fret]
