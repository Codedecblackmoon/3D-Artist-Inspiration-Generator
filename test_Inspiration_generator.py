import unittest
from unittest.mock import patch
import Inspiration_generator  # Replace with the actual module name

class TestYourFunctions(unittest.TestCase):

    @patch("builtins.input", side_effect=["easy"])
    def test_whatufeeling_easy(self, mock_input):
        self.assertEqual(Inspiration_generator.whatufeeling(), "easy")

    @patch("builtins.input", side_effect=["Hard"])
    def test_whatufeeling_hard(self, mock_input):
        self.assertEqual(Inspiration_generator.whatufeeling(), "hard")

    @patch("builtins.input", side_effect=["Middium"])
    def test_whatufeeling_medium(self, mock_input):
        self.assertEqual(Inspiration_generator.whatufeeling(), "middium")

    @patch("builtins.input", side_effect=["", "easy"])
    def test_whatufeeling_empty_then_easy(self, mock_input):
        self.assertEqual(Inspiration_generator.whatufeeling(), "easy")

    def test_simple(self):
        with patch('builtins.open', side_effect=[open('simple.txt', 'r')]):
            self.assertIsInstance(Inspiration_generator.simple(), str)

    def test_hard(self):
        with patch('builtins.open', side_effect=[open('hard.txt', 'r')]):
            self.assertIsInstance(Inspiration_generator.hard(), str)

    def test_middium(self):
        with patch('builtins.open', side_effect=[open('middum.txt', 'r')]):
            self.assertIsInstance(Inspiration_generator.middium(), str)

    def test_Theme(self):
        with patch('builtins.open', side_effect=[open('theme.txt', 'r')]):
            self.assertIsInstance(Inspiration_generator.Theme(), str)

    def test_colors(self):
        with patch('builtins.open', side_effect=[open('color.txt', 'r')]):
            self.assertIsInstance(Inspiration_generator.colors(), str)

    def test_chosing(self):
        theme = "test_theme"
        output = "easy"
        color = ["color1", "color2"]
        result = Inspiration_generator.chosing(theme, output, color)
        self.assertIsInstance(result, str)

    @patch("builtins.print")
    def test_deffination(self, mock_print):
        theme = "test_theme"
        with patch('builtins.open', side_effect=[open('theme_def.txt', 'r')]):
            Inspiration_generator.deffination(theme)
        mock_print.assert_called()

    @patch("builtins.print")
    @patch("Inspiration_generator.whatufeeling", return_value="easy")
    @patch("Inspiration_generator.chosing")
    def test_main_easy(self, mock_chosing, mock_whatufeeling, mock_print):
        Inspiration_generator.main()
        mock_chosing.assert_called_once()
        mock_print.assert_called()

    @patch("builtins.print")
    @patch("Inspiration_generator.whatufeeling", return_value="hard")
    @patch("Inspiration_generator.chosing")
    @patch("Inspiration_generator.deffination")
    def test_main_hard(self, mock_deffination, mock_chosing, mock_whatufeeling, mock_print):
        Inspiration_generator.main()
        mock_chosing.assert_called_once()
        mock_deffination.assert_called_once()
        mock_print.assert_called()


if __name__ == '__main__':
    unittest.main()