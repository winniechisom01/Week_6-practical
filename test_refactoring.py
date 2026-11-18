"""Behaviour-preservation check: refactored code vs the original routine."""
import io
import unittest
from contextlib import redirect_stdout

from legacy_routine import x
from result_module import calculate_total_score
from grading import calculate_grade


class TestBehaviourPreserved(unittest.TestCase):
    def test_same_total_and_grade_for_passing_scores(self):
        # The original only handled totals >= 50 correctly (A, B, C).
        for a, b, c in [(20, 20, 60), (14, 14, 42), (12, 12, 36), (10, 10, 30)]:
            with self.subTest(scores=(a, b, c)):
                with redirect_stdout(io.StringIO()) as out:
                    old_total = x(a, b, c, "N")
                new_total = calculate_total_score(a, b, c)
                self.assertEqual(old_total, new_total)
                self.assertIn(calculate_grade(new_total), out.getvalue())

    def test_known_intentional_difference_below_50(self):
        # Original returned "F" for 45; the specified scale gives "D".
        with redirect_stdout(io.StringIO()) as out:
            x(10, 10, 25, "N")
        self.assertIn("F", out.getvalue())
        self.assertEqual(calculate_grade(45), "D")


if __name__ == "__main__":
    unittest.main()
