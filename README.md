# guitar-notes

A terminal-based fretboard note quiz for guitarists. The app presents a highlighted position on the fretboard and you type the note name — great for drilling your knowledge of every note up and down the neck.

Note that this was written entirely using Claude Code.

## Setup

Requires [conda](https://docs.conda.io/) (or mamba).

```bash
conda env create -f environment.yml
conda activate guitar-notes
```

## Usage

Navigate to the `src/` directory first, then run the app:

```bash
cd src
python -m guitar_notes
```

Type the note name when prompted (e.g. `A`, `C#`, `Bb`). Flat equivalents are accepted. Press `Ctrl-C` to end the session and see your score.

### Options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--strings` | `1`–`6` (space-separated) | all | Strings to include. 1 = high-e, 6 = low-E. |
| `--frets` | `all`, `inlay`, `non_inlay` | `all` | Restrict to inlay frets (1,5,7,9,12,15,17), non-inlay, or all. |
| `--notes` | `all`, `naturals_only` | `all` | Restrict to natural notes only (no sharps/flats). |
| `--open-strings` | flag | off | Test open strings only (fret 0). Cannot be combined with `--frets`, `--notes`, or `--max-fret`. |
| `--max-fret` | `0`–`17` | `17` | Highest fret to include (inclusive). Useful for beginners drilling the first few frets. Cannot be combined with `--open-strings`. |

#### Examples

```bash
# Drill only the low E string
python -m guitar_notes --strings 6

# Inlay frets only on the bottom two strings
python -m guitar_notes --strings 5 6 --frets inlay

# Natural notes only, all strings
python -m guitar_notes --notes naturals_only

# Open strings only (great for beginners)
python -m guitar_notes --open-strings

# Open strings on the bottom two strings only
python -m guitar_notes --open-strings --strings 5 6

# First four frets only (great for beginners starting out)
python -m guitar_notes --max-fret 4

# Inlay frets up to the 7th fret
python -m guitar_notes --frets inlay --max-fret 7
```

## Fretboard display

The quiz renders an ASCII fretboard for each question. The highlighted position shows the fret number; the string label on the left identifies which string is being played. Open strings are shown with `0`.

```
e|-------------------|
B|-------------------|
G|-------------------|
D|-------------------|
A|----5--------------|
E|-------------------|
 |  . . . .  :  .  . |
```

The dots below the low-E row are fretboard inlays (at frets 1, 5, 7, 9, 15, 17) and the double-dot (`:`) marks fret 12.

## String numbering

Strings follow standard guitarist convention:

| Number | Name | Open note |
|--------|------|-----------|
| 1 | e | E4 |
| 2 | B | B3 |
| 3 | G | G3 |
| 4 | D | D3 |
| 5 | A | A2 |
| 6 | E | E2 |
