import unittest
import io
import sys
from main import list_movies

class TestListMovies(unittest.TestCase):
    def test_empty_list(self):
        movies = []
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_movies(movies)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected = "---- Movies (sorted by highest score) ----\n(no movies)\n---- End of list (0 movies) ----\n"
        self.assertEqual(output, expected)

    def test_single_movie_with_year(self):
        movies = [{'title': 'Inception', 'grade': 8.5, 'year': '2010'}]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_movies(movies)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected = "---- Movies (sorted by highest score) ----\nInception (2010): 8.5\n---- End of list (1 movies) ----\n"
        self.assertEqual(output, expected)

    def test_single_movie_without_year(self):
        movies = [{'title': 'Inception', 'grade': 8.0, 'year': ''}]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_movies(movies)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected = "---- Movies (sorted by highest score) ----\nInception: 8\n---- End of list (1 movies) ----\n"
        self.assertEqual(output, expected)

    def test_multiple_movies_sorted_by_grade(self):
        movies = [
            {'title': 'Low', 'grade': 5.0, 'year': ''},
            {'title': 'High', 'grade': 9.0, 'year': '2021'},
            {'title': 'Mid', 'grade': 7.5, 'year': '2019'}
        ]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_movies(movies)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected = "---- Movies (sorted by highest score) ----\nHigh (2021): 9\nMid (2019): 7.5\nLow: 5\n---- End of list (3 movies) ----\n"
        self.assertEqual(output, expected)

    def test_grade_as_string_treated_as_zero(self):
        movies = [{'title': 'Invalid', 'grade': 'not_a_number', 'year': ''}]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_movies(movies)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected = "---- Movies (sorted by highest score) ----\nInvalid: not_a_number\n---- End of list (1 movies) ----\n"
        self.assertEqual(output, expected)

    def test_mixed_grades_and_years(self):
        movies = [
            {'title': 'A', 'grade': 10.0, 'year': '2000'},
            {'title': 'B', 'grade': '', 'year': '2001'},
            {'title': 'C', 'grade': 8, 'year': ''}
        ]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_movies(movies)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected = "---- Movies (sorted by highest score) ----\nA (2000): 10\nC: 8\nB (2001): \n---- End of list (3 movies) ----\n"
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()