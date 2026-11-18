# Student Result Processing Module

Level 3 Software Engineering – Week 6 Practical: *High-Quality Routines (Writing, Reviewing, Refactoring)*

A small Python project that validates student details and scores, calculates the total score, grade and grade point, computes a credit-unit weighted GPA, and returns structured result data.

## Project structure

```
Week6_Student_Result_System/
|-- main.py                # coordinates the workflow and displays output
|-- validation.py          # validates student details and scores
|-- grading.py             # grade boundaries and grade calculation
|-- result_module.py       # totals, result records and GPA
|-- test_grading.py        # grade boundary and input tests
|-- test_result_module.py  # score, validation, result and GPA tests
|-- test_refactoring.py    # compares refactored code with the original routine
|-- legacy_routine.py      # original routine from the code review (reference only)
|-- CODE_REVIEW.md         # code review and refactoring explanation
`-- README.md
```

## Requirements

- Python 3.8 or later (standard library only; no packages to install)

## Setup

```bash
git clone <your-repository-url>
cd Week6_Student_Result_System
python --version
```

## Run the application

```bash
python main.py
```

Expected output for the sample student:

```
STUDENT RESULT
Student Name: John
Registration Number: CSC/2026/001
Course Code: SWE 306
Total: 87
Grade: A
Grade Point: 5
GPA: 4.0
```

## Run the tests

```bash
python -m unittest -v
```

All 29 tests should report `ok`. They cover normal, boundary and invalid inputs.

## Scoring rules

| Component   | Maximum |
|-------------|---------|
| Assignment  | 20      |
| Test        | 20      |
| Examination | 60      |
| **Total**   | **100** |

Illustrative grading scale:

| Score  | Grade | Grade point |
|--------|-------|-------------|
| 70–100 | A     | 5           |
| 60–69  | B     | 4           |
| 50–59  | C     | 3           |
| 45–49  | D     | 2           |
| 40–44  | E     | 1           |
| 0–39   | F     | 0           |

GPA = sum(grade point × credit unit) ÷ sum(credit units).

## Error handling

| Situation | Exception |
|-----------|-----------|
| Blank student name or registration number | `ValueError` |
| Registration number not text | `TypeError` |
| Score not numeric (including `True`/`False`) | `TypeError` |
| Score outside its allowed range | `ValueError` |
| Empty course list, grade point outside 0–5, credit unit ≤ 0 | `ValueError` |

## Version control

```bash
git init
git add .
git commit -m "Create initial student result routines"
# after refactoring and tests pass:
git add .
git commit -m "Refactor routines and add unit tests"
```

## Notes

The grading scale is illustrative, as supplied in the practical manual, and is not an official institutional policy.
