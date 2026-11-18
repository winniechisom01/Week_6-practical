"""Grade boundaries and grade calculation (illustrative scale)."""

# (minimum score, grade, grade point) - checked from highest to lowest.
GRADE_BOUNDARIES = [
    (70, "A", 5),
    (60, "B", 4),
    (50, "C", 3),
    (45, "D", 2),
    (40, "E", 1),
    (0, "F", 0),
]


def _lookup(total_score):
    """Validate a total score and return its (grade, grade_point) pair.

    Raises:
        TypeError: if the score is not numeric (booleans are rejected).
        ValueError: if the score is outside 0..100.
    """
    if not isinstance(total_score, (int, float)) or isinstance(total_score, bool):
        raise TypeError("Total score must be numeric")
    if not 0 <= total_score <= 100:
        raise ValueError("Total score must be between 0 and 100")
    for minimum, grade, points in GRADE_BOUNDARIES:
        if total_score >= minimum:
            return grade, points


def calculate_grade(total_score):
    """Return the letter grade (A-F) for a total score of 0..100."""
    return _lookup(total_score)[0]


def calculate_grade_point(total_score):
    """Return the grade point (0-5) for a total score of 0..100."""
    return _lookup(total_score)[1]
