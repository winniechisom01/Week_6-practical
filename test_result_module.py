import unittest
from result_module import calculate_total_score, generate_result, calculate_gpa
from validation import validate_student, validate_score


class TestTotalScore(unittest.TestCase):
    def test_total_normal(self):
        self.assertEqual(calculate_total_score(18, 17, 52), 87)

    def test_total_minimum_and_maximum(self):
        self.assertEqual(calculate_total_score(0, 0, 0), 0)
        self.assertEqual(calculate_total_score(20, 20, 60), 100)

    def test_score_above_maximum(self):
        for args in ((21, 10, 10), (10, 21, 10), (10, 10, 61)):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    calculate_total_score(*args)

    def test_negative_score(self):
        with self.assertRaises(ValueError):
            calculate_total_score(-1, 10, 10)

    def test_non_numeric_score(self):
        for bad in ("18", None, True):
            with self.subTest(value=bad):
                with self.assertRaises(TypeError):
                    calculate_total_score(bad, 17, 52)


class TestValidation(unittest.TestCase):
    def test_valid_student(self):
        self.assertTrue(validate_student("John", "CSC/2026/001"))

    def test_blank_name(self):
        with self.assertRaises(ValueError):
            validate_student("   ", "CSC/2026/001")

    def test_blank_registration_number(self):
        with self.assertRaises(ValueError):
            validate_student("John", "  ")

    def test_registration_number_not_text(self):
        with self.assertRaises(TypeError):
            validate_student("John", 12345)

    def test_score_boundaries(self):
        self.assertTrue(validate_score(0, 20, "Test"))
        self.assertTrue(validate_score(20, 20, "Test"))
        with self.assertRaises(ValueError):
            validate_score(20.1, 20, "Test")


class TestGenerateResult(unittest.TestCase):
    def test_generate_result(self):
        r = generate_result(" John ", " CSC/2026/001 ", "SWE 306", 18, 17, 52)
        self.assertEqual(r["student_name"], "John")
        self.assertEqual(r["registration_number"], "CSC/2026/001")
        self.assertEqual((r["total"], r["grade"], r["grade_point"]), (87, "A", 5))

    def test_failing_result(self):
        r = generate_result("Ada", "CSC/2026/002", "SWE 306", 5, 5, 20)
        self.assertEqual((r["total"], r["grade"], r["grade_point"]), (30, "F", 0))

    def test_blank_name_rejected(self):
        with self.assertRaises(ValueError):
            generate_result("  ", "CSC/2026/001", "SWE 306", 10, 10, 10)


class TestGPA(unittest.TestCase):
    def test_gpa_sample(self):
        courses = [{"grade_point": 5, "credit_unit": 3},
                   {"grade_point": 4, "credit_unit": 2},
                   {"grade_point": 3, "credit_unit": 3}]
        self.assertAlmostEqual(calculate_gpa(courses), 4.0)

    def test_gpa_is_weighted(self):
        courses = [{"grade_point": 5, "credit_unit": 1},
                   {"grade_point": 0, "credit_unit": 4}]
        self.assertAlmostEqual(calculate_gpa(courses), 1.0)

    def test_gpa_empty(self):
        with self.assertRaises(ValueError):
            calculate_gpa([])

    def test_gpa_bad_credit_unit(self):
        for unit in (0, -2):
            with self.subTest(unit=unit):
                with self.assertRaises(ValueError):
                    calculate_gpa([{"grade_point": 4, "credit_unit": unit}])

    def test_gpa_bad_grade_point(self):
        for gp in (-1, 6):
            with self.subTest(gp=gp):
                with self.assertRaises(ValueError):
                    calculate_gpa([{"grade_point": gp, "credit_unit": 3}])


if __name__ == "__main__":
    unittest.main()
