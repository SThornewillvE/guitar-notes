# Guitar Notes Quiz — Project Context

*Description*: A terminal-based fretboard note quiz app for guitar practice. 

Make an app for guitarists learn to identify notes across the fretboard to quiz them, by rendering a fretboard within the 
terminal. The app presents a highlighted position (string + fret) and the user types the note name.

## Tech Stack

- Python 3.11+
- No web framework is required, this is to be done within the terminal (stdlib `curses` or `rich` for rendering)
- No database is necessary, it's okay for no statistics to be saved over time
- `pyproject.toml` + `uv` to manage the Python environment
- This app will not be deployed, and therefore code testing using `pytest` is *not necessary*

## Commands
- Run app: `uv run python -m guitar_notes` (from project root or `src/`)

## Architecture

```
guitar-notes/
├── src/
│   └── guitar_notes/
│       ├── __init__.py      # Required to make `python -m guitar_notes` work
│       ├── main.py          # Entry point, argument parsing, launches quiz loop
│       ├── fretboard.py     # Note logic (string/fret → note name) + ASCII rendering
│       ├── quiz.py          # Quiz loop, input handling, scoring, session state
│       └── settings.py      # Settings model (active strings, fret ranges, note sets)
├── pyproject.toml
├── .python-version
└── README.md
```

Core data flow: `settings → quiz.py` selects a random position → `fretboard.py`
renders the board with that position highlighted → user inputs note →
`quiz.py` checks answer → repeat.

## Rendering The fretboard

The rendered fretboard should show the following:

* The fretboard is to be rendered using a clear ASCII grid.
* String names on the left.
* Unplayed frets denoted by a `-` and the played fret has the `-` replaced by the fret number in the correct position.

For more information see the diagrams below.

You can render the fretboard using the following diagram:

```
e|-------------------|
B|-------------------|
G|-------------------|
D|-------------------|
A|-------------------|
E|-------------------|
 |  . . . .  :  .  . |
```

The dots below the low-E string are the inlays, to help orient the user.

Naturally, if the user is testing the open strings then you can hide them like this:

```
 |-------------------|
 |-------------------|
 |-------------------|
 |-------------------|
 |-------------------|
 |-------------------|
 |  . . . .  :  .  . |
```

As an example for if you want to test the open G string, then you can render it like this:

```
 |-------------------|
 |-------------------|
0|-------------------|
 |-------------------|
 |-------------------|
 |-------------------|
 |  . . . .  :  .  . |
```

Note that because the string is played without fretting any notes we denote it using a `0`

If you want to test the 5th fret of the A string, then you can render it like this:

```
e|-------------------|
B|-------------------|
G|-------------------|
D|-------------------|
A|----5--------------|
E|-------------------|
 |  . . . .  :  .  . |
```

Note that the 5th fret is above the inlay for the 5th fret and is 5 frets along from the "nut" (the line of `|`s on the left hand side.)

It's okay to render only up to the 18th fret, allowing the user to test their knwowledge for the first 17 frets of the fretboard.


## Domain: Guitar Note Logic

* Standard tuning open strings (low to high): E2, A2, D3, G3, B3, E4.
* In the app, strings are numbered 1–6 from high E to low E or labelled by name (E, A, D, G, B, e)
    * Note that labelling the low E string as the 6th string is standard guitarist convention.
* Notes use the chromatic scale with sharps by default: A A# B C C# D D# E F F# G G#.
* The app must also accept flat equivalents as correct answers (Bb = A#, Eb = D#, etc.).
* No double sharps/flats are necessary.
* Fret 0 = open string. 
* Fret 12 = octave (same note name as open).
* Standard inlay positions: 1, 5, 7, 9, 12, 15, 17.

## Quiz Modes (progressive difficulty)

The app should support filtering by:
- Which strings are active for testing (e.g. low E only, then add A, etc.)
- Which frets are active for testing (e.g. inlay frets only, non-inlay frets only, or all frets)
- Whether to include sharps/flats or naturals only

Settings should be configurable at startup (interactive menu or CLI flags).

## Conventions

- Prefer clarity over cleverness — this codebase is also a learning tool for its author to learn Claude code
- Write python code using functions rather than classes where state isn't needed
- Type hints on all function signatures
- Short, focused modules — if a file exceeds ~150 lines, split it
- IMPORTANT: Do not add dependencies without asking first — the python stdlib is preferred

## Common Pitfalls to Avoid

- Do not hardcode note lists as strings — compute them from a chromatic scale array
- Do not mix string numbering conventions mid-codebase (pick one and stick to it)
- Do not assume the terminal width — the fretboard render should adapt or at minimum
  warn if the terminal is too narrow
- Do not fill in the `README.md` file until you have completed the app
- Do not run commands outside the directory that the `guitar-notes` repo is in 
- Do not run any git commands, let the user manage this for themselves
- Do not add external dependencies to `pyproject.toml` without asking first — the python stdlib is preferred
    - The user runs `uv run python -m guitar_notes` from the project root (or `src/`) with the relevant flags when needed.
