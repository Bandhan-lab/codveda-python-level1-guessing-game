import unittest
from unittest.mock import patch

import guessing_game


class TestGuessingGame(unittest.TestCase):
    def test_generate_target_is_in_range(self):
        for _ in range(100):
            target = guessing_game.generate_target()
            self.assertGreaterEqual(target, 1)
            self.assertLessEqual(target, 100)

    def test_check_guess_too_low(self):
        self.assertEqual(guessing_game.check_guess(25, 50), "Too low!")

    def test_check_guess_too_high(self):
        self.assertEqual(guessing_game.check_guess(75, 50), "Too high!")

    def test_check_guess_correct(self):
        self.assertEqual(guessing_game.check_guess(50, 50), "Correct!")

    @patch("builtins.input", side_effect=["abc", "50"])
    def test_get_guess_handles_invalid_input(self, _mock_input):
        with patch("builtins.print") as mock_print:
            self.assertIsNone(guessing_game.get_guess())
            self.assertEqual(guessing_game.get_guess(), 50)
            mock_print.assert_called_once_with(
                "Invalid input. Please enter a whole number."
            )

    def test_play_game_win(self):
        with patch("guessing_game.get_guess", side_effect=[30, 50]):
            self.assertTrue(guessing_game.play_game(target=50, max_attempts=3))

    def test_play_game_max_attempts(self):
        with patch("guessing_game.get_guess", side_effect=[10, 20, 30]):
            self.assertFalse(guessing_game.play_game(target=50, max_attempts=3))


if __name__ == "__main__":
    unittest.main()
