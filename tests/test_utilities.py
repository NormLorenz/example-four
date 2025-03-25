import unittest
from app.utilities import (
    get_transcript,
    split_strings,
    build_dictionary_expanding_duplicates,
    build_dictionary_without_duplicates,
    seconds_to_time_string,
    build_dictionary_with_time_string,
)


class TestUtilities(unittest.TestCase):

    def test_split_strings(self):
        input_text = "Hello world! How are you? I'm fine."
        separators = ['.', '?', '!']
        expected_output = ['Hello world!', ' How are you?', " I'm fine."]
        self.assertEqual(split_strings(
            input_text, separators), expected_output)

    def test_build_dictionary_expanding_duplicates(self):
        input_dict = [{'text': 'Hello world! How are you?', 'start': 0}]
        expected_output = [
            {'text': 'Hello world!', 'start': 0},
            {'text': ' How are you?', 'start': 0},
        ]
        self.assertEqual(build_dictionary_expanding_duplicates(
            input_dict), expected_output)

    def test_build_dictionary_without_duplicates(self):
        input_dict = [
            {'text': 'Hello world!', 'start': 0},
            {'text': 'Hello world!', 'start': 1},
            {'text': 'How are you?', 'start': 2},
        ]
        expected_output = [
            {'text': 'Hello world!', 'start': 0},
            {'text': 'How are you?', 'start': 2},
        ]
        self.assertEqual(build_dictionary_without_duplicates(
            input_dict), expected_output)

    def test_seconds_to_time_string(self):
        self.assertEqual(seconds_to_time_string(3661), " 1:01:01")
        self.assertEqual(seconds_to_time_string(61), " 1:01")
        self.assertEqual(seconds_to_time_string(5), " 0:05")

    def test_build_dictionary_with_time_string(self):
        input_dict = [
            {'text': 'Hello world!', 'start': 3661},
            {'text': 'How are you?', 'start': 61},
        ]
        expected_output = [
            {'text': 'Hello world!', 'start': " 1:01:01"},
            {'text': 'How are you?', 'start': " 1:01"},
        ]
        self.assertEqual(build_dictionary_with_time_string(
            input_dict), expected_output)

    # Note: Testing `get_transcript` requires mocking the YouTubeTranscriptApi
    # because it makes an external API call. Here's an example:
    def test_get_transcript(self):
        # Mocking YouTubeTranscriptApi
        from unittest.mock import patch

        mock_transcript = [
            {'text': 'Hello world!', 'start': 0},
            {'text': 'How are you?', 'start': 5},
        ]

        with patch('app.utilities.YouTubeTranscriptApi.fetch', return_value=mock_transcript):
            result = get_transcript("https://www.youtube.com/watch?v=example")
            expected_output = [
                {'text': 'Hello world!', 'start': " 0:00"},
                {'text': 'How are you?', 'start': " 0:05"},
            ]
            self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
