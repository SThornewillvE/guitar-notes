# guitar-notes

A terminal-based fretboard note quiz for guitarists. The app presents a highlighted position on the fretboard and you type the note name — great for drilling your knowledge of every note up and down the neck.

Note that this was written entirely using Claude Code.

## How to learn the fretboard progressively

The most effective way to memorise every note on the neck is to work in small, manageable chunks, and only expand the scope once the current chunk feels easy using the following progression; 

1. Low E string, inlay frets only (start here)
2. Low E string, all frets
    * Optional: Learn non-accidental (natural note) frets
3. Then move to the A string and do the same as above until you know all notes
4. Test yourself for the Low E and A string
5. Progressively do the above to add progressively higher strings (D, G, B and high E) until you are testing the whole fretboard

If you are beginner guitarist, it can be useful to do this only until the 4th fret, as beginners will usually only play notes and scales within this range.

Finally, make sure to test yourself across multiple days, as sleep helps the brain to learn. 

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
| `--open-strings` | flag | off | Test open strings only (fret 0). Cannot be combined with `--frets`, `--notes`, `--min-fret`, or `--max-fret`. |
| `--min-fret` | `0`–`17` | `0` | Lowest fret to include (inclusive). Cannot be combined with `--open-strings`. |
| `--max-fret` | `0`–`17` | `17` | Highest fret to include (inclusive). Cannot be combined with `--open-strings`. |
| `--show-labels` | flag | off | Show string names (e, B, G, D, A, E) to the left of the nut. Hidden by default so you can't use them as a reference. |

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

# Drill only the upper part of the neck (frets 7–12)
python -m guitar_notes --min-fret 7 --max-fret 12
```

## Fretboard display

The quiz renders an ASCII fretboard for each question. The highlighted position shows the fret number. String names are hidden by default so you can't use them as a shortcut — use `--show-labels` to reveal them.

```
 |- - - - - - - - - - - - - - - - - - - |
 |- - - - - - - - - - - - - - - - - - - |
 |- - - - - - - - - - - - - - - - - - - |
 |- - - - - - - - - - - - - - - - - - - |
 |- - - - 5 - - - - - - - - - - - - - - |
 |- - - - - - - - - - - - - - - - - - - |
 |    .   .   .   .     :     .     .   |
```

Open strings are shown with `0` on the active string. The dots below the bottom row are fretboard inlays (at frets 1, 5, 7, 9, 15, 17) and the double-dot (`:`) marks fret 12.

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
