import unittest
from grading import calculate_grade, calculate_grade_point


class TestGrading(unittest.TestCase):
    def test_grade_a_boundary(self):
        self.assertEqual(calculate_grade(70), "A")

    def test_grade_b_boundary(self):
        self.assertEqual(calculate_grade(60), "B")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(0), "F")

    def test_invalid_high_score(self):
        with self.assertRaises(ValueError):
            calculate_grade(101)

    def test_all_grade_transitions(self):
        cases = {0: "F", 1: "F", 39: "F", 40: "E", 44: "E", 45: "D",
                 49: "D", 50: "C", 59: "C", 60: "B", 69: "B", 70: "A",
                 99: "A", 100: "A"}
        for score, grade in cases.items():
            with self.subTest(score=score):
                self.assertEqual(calculate_grade(score), grade)

    def test_grade_points_at_boundaries(self):
        cases = {0: 0, 39: 0, 40: 1, 45: 2, 50: 3, 60: 4, 70: 5, 100: 5}
        for score, points in cases.items():
            with self.subTest(score=score):
                self.assertEqual(calculate_grade_point(score), points)

    def test_decimal_scores(self):
        self.assertEqual(calculate_grade(69.5), "B")
        self.assertEqual(calculate_grade(39.9), "F")

    def test_out_of_range_scores(self):
        for bad in (-1, 101):
            with self.subTest(score=bad):
                with self.assertRaises(ValueError):
                    calculate_grade(bad)
                with self.assertRaises(ValueError):
                    calculate_grade_point(bad)

    def test_non_numeric_scores(self):
        for bad in ("70", None, True, [70]):
            with self.subTest(score=bad):
                with self.assertRaises(TypeError):
                    calculate_grade(bad)
                with self.assertRaises(TypeError):
                    calculate_grade_point(bad)


if __name__ == "__main__":
    unittest.main()
