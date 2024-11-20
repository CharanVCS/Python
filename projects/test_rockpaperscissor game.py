import unittest
from unittest.mock import patch
import pyttsx3
import io
from contextlib import redirect_stdout
from RockPaperScissor_Game import say, rps, get_user_choice, display_instructions, main

class TestRockPaperScissors(unittest.TestCase):

    @patch('pyttsx3.init')
    def test_say(self, mock_init):
        engine = mock_init.return_value
        say("Hello")
        engine.say.assert_called_with("Hello")
        engine.runAndWait.assert_called_once()

    def test_rps(self):
        # Test for a draw
        self.assertIsNone(rps('r', 'r'))
        self.assertIsNone(rps('p', 'p'))
        self.assertIsNone(rps('s', 's'))

        # Test for user wins
        self.assertTrue(rps('s', 'r'))
        self.assertTrue(rps('r', 'p'))
        self.assertTrue(rps('p', 's'))

        # Test for computer wins
        self.assertFalse(rps('r', 's'))
        self.assertFalse(rps('p', 'r'))
        self.assertFalse(rps('s', 'p'))

    @patch('builtins.input', side_effect=['r'])
    def test_get_user_choice_valid(self, mock_input):
        self.assertEqual(get_user_choice(), 'r')

    @patch('builtins.input', side_effect=['invalid', 'r'])
    @patch('pyttsx3.init')
    def test_get_user_choice_invalid(self, mock_init, mock_input):
        engine = mock_init.return_value
        f = io.StringIO()
        with redirect_stdout(f):
            result = get_user_choice()
        output = f.getvalue()
        self.assertIn('Please enter a correct choice', output)
        engine.say.assert_called_with("Your choice is wrong, please enter a correct choice")
        self.assertEqual(result, 'r')

    def test_display_instructions(self):
        f = io.StringIO()
        with redirect_stdout(f):
            display_instructions()
        output = f.getvalue().strip()
        self.assertIn('Choose either Rock, Paper, or Scissor:', output)

    @patch('builtins.input', side_effect=['q'])
    @patch('pyttsx3.init')
    def test_main_quit(self, mock_init, mock_input):
        engine = mock_init.return_value
        f = io.StringIO()
        with redirect_stdout(f):
            main()
        output = f.getvalue()
        self.assertIn('Thank you for playing! Goodbye!', output)
        engine.say.assert_called_with("Thank you for playing! Goodbye!")

    @patch('builtins.input', side_effect=['score', 'q'])
    @patch('pyttsx3.init')
    def test_main_score(self, mock_init, mock_input):
        engine = mock_init.return_value
        f = io.StringIO()
        with redirect_stdout(f):
            main()
        output = f.getvalue()
        self.assertIn("Your score is: Wins - 0, Losses - 0", output)
        engine.say.assert_any_call("Your score is: Wins - 0, Losses - 0")

    @patch('builtins.input', side_effect=['r', 'q'])
    @patch('pyttsx3.init')
    @patch('random.choice', side_effect=['p'])
    def test_main_play(self, mock_choice, mock_init, mock_input):
        engine = mock_init.return_value
        f = io.StringIO()
        with redirect_stdout(f):
            main()
        output = f.getvalue()
        self.assertIn('You chose Rock <-> Computer chose Paper', output)
        self.assertIn('You lose..! :(', output)
        engine.say.assert_any_call('You lose..! :(')

if __name__ == "__main__":
    unittest.main()
