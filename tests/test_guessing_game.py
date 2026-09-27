import unittest
from unittest.mock import patch

import guessing_game


class TestGuessingGame(unittest.TestCase):
    @patch("guessing_game.random.randint", return_value=42)
    def test_generate_target_uses_expected_range(self, mock_randint):
        self.assertEqual(guessing_game.generate_target(), 42)
        mock_randint.assert_called_once_with(1, 100)

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

    @patch("guessing_game.get_guess", side_effect=[150, 30, 50])
    def test_play_game_rejects_out_of_range_guess(self, mock_get_guess):
        with patch("builtins.print"):
            self.assertTrue(
                guessing_game.play_game(target=50, max_attempts=2)
            )
        self.assertEqual(mock_get_guess.call_count, 3)

    @patch("builtins.input", side_effect=["abc", "30", "50"])
    def test_play_game_continues_after_invalid_input(self, mock_input):
        with patch("builtins.print"):
            self.assertTrue(
                guessing_game.play_game(target=50, max_attempts=2)
            )
        self.assertEqual(mock_input.call_count, 3)

    def test_play_game_win(self):
        with patch("guessing_game.get_guess", side_effect=[30, 50]):
            self.assertTrue(guessing_game.play_game(target=50, max_attempts=3))

    def test_play_game_max_attempts(self):
        with patch("guessing_game.get_guess", side_effect=[10, 20, 30]):
            with patch("builtins.print") as mock_print:
                self.assertFalse(
                    guessing_game.play_game(target=50, max_attempts=3)
                )
        mock_print.assert_any_call("Game over! The correct number was 50.")

    @patch("guessing_game.play_game", return_value=True)
    @patch("builtins.input", side_effect=["n"])
    def test_main_replay_prompt(self, mock_input, _mock_play_game):
        with patch("builtins.print"):
            guessing_game.main()
        mock_input.assert_called_once_with("\nPlay again? (y/n): ")


if __name__ == "__main__":
    unittest.main()
