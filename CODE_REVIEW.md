# Code Review and Refactoring Report

## 1. Original routine reviewed

```python
def x(a, b, c, n):
    t = a + b + c
    if t >= 70:
        g = "A"
    elif t >= 60:
        g = "B"
    elif t >= 50:
        g = "C"
    else:
        g = "F"
    print(n, t, g)
    return t
```

## 2. Weaknesses identified

| # | Weakness | Why it matters |
|---|----------|----------------|
| 1 | Unclear names (`x`, `a`, `b`, `c`, `n`, `t`, `g`) | Readers cannot tell what the routine or its parameters mean. |
| 2 | Calculation, grading and display are mixed in one routine | It has several responsibilities (low cohesion); changing one risks breaking another. |
| 3 | `print` inside the processing logic | The routine cannot return the grade, and its output is hard to test or reuse. |
| 4 | No validation of data types or score ranges | Text, negative numbers or scores above the maximum are silently accepted. |
| 5 | Incomplete grading policy | Every total under 50 becomes "F"; grades D and E and the grade points are missing. |
| 6 | Grade boundaries hard-coded in `if/elif` | The policy cannot be changed or reused in one place. |
| 7 | No documentation or failure contract | Callers do not know what is returned or which errors can occur. |
| 8 | Hard to test individual responsibilities | Output goes to the screen and the grade is not returned. |

## 3. Refactoring workflow followed

1. Ran the original routine and recorded its outputs.
2. Documented the intended behaviour (the full A–F scale, scores 0–100).
3. Extracted one responsibility at a time: validation, grading, totals, result record, GPA, display.
4. Renamed everything to communicate intent.
5. Centralised the grade boundaries in `GRADE_BOUNDARIES`.
6. Ran `python -m unittest -v` after each change.
7. Compared the outputs (`test_refactoring.py`) to confirm behaviour was preserved.

## 4. Improvements made

| Area | Before | After |
|------|--------|-------|
| Names | `x(a, b, c, n)` | `calculate_total_score`, `generate_result`, `calculate_grade`, `calculate_gpa` |
| Responsibilities | One routine does everything | Separate files: `validation.py`, `grading.py`, `result_module.py`, `main.py` |
| Output | `print` inside logic | Routines return data; only `main.py` prints |
| Validation | None | Type and range checks with `TypeError` / `ValueError` |
| Grading policy | A, B, C, F only | Full A–F scale with grade points |
| Configuration | Hard-coded `if/elif` | One `GRADE_BOUNDARIES` table |
| Duplication | Validation and lookup loop repeated in `calculate_grade` and `calculate_grade_point` | One shared helper, `_lookup` |
| Documentation | None | Docstrings state inputs, outputs and exceptions |
| Testing | None | 29 automated tests covering normal, boundary and invalid inputs |

## 5. Behaviour preservation

For totals of 50 and above, the refactored code returns the same total and grade as the original routine. The one deliberate difference is for totals below 50: the original returned "F", whereas the specified scale gives D (45–49), E (40–44) and F (below 40). This is a bug fix against the specification, and `test_refactoring.py` documents it.

## 6. Reflection

- **Why separate validation from calculation?** Rules can be tested, reused and changed independently, and invalid data is stopped before it reaches the calculation.
- **Which routines show functional cohesion?** `validate_score`, `calculate_grade`, `calculate_total_score` and `calculate_gpa` each perform one well-defined task.
- **How are dependencies made explicit?** Through `import` statements (for example `result_module.py` imports from `validation.py` and `grading.py`) and through function parameters instead of hidden globals.
- **What happens when a score exceeds its maximum?** `validate_score` raises a `ValueError`, for example "Examination must be between 0 and 60".
- **Which tests verify grade boundaries?** `test_all_grade_transitions` and `test_grade_points_at_boundaries` in `test_grading.py` (39/40, 44/45, 49/50, 59/60, 69/70, plus 0 and 100).
- **How do tests help during refactoring?** They show immediately whether behaviour has changed, so internal structure can be improved with confidence.
- **What further controls are needed before real deployment?** Secure storage in a database, user authentication and role-based access, audit logs, approval workflows, handling of absent or resit students, data-protection compliance, and confirmation of the grading policy against the institution's official rules.
