from typing import Dict, List, Union
from youtube_transcript_api import YouTubeTranscriptApi
import re

# High level entry point for the YouTube Transcript API


def get_transcript(url: str) -> List[Dict[str, str]]:

    # Get the video id from the url
    video_id = url.split('v=')[1]
    video_id = video_id.split('&')[0]

    # Fetch the transcript
    step_one = YouTubeTranscriptApi().fetch(video_id, languages=['de'])

    # Convert it to raw data
    step_two = step_one.to_raw_data()

    # Build a dictionary expanding duplicates and striping duration
    step_three = build_dictionary_expanding_duplicates(step_two)

    # Build dictionary without duplicates
    step_four = build_dictionary_without_duplicates(step_three)

    # Build dictionary with time as a string
    step_five = build_dictionary_with_time_string(step_four)

    return step_five


# Split a string into multiple parts using a separator
def split_strings(input: str, separators: List[str]) -> List[str]:
    combined_array: List[str] = []

    # Create a regular expression pattern to capture separators
    pattern: str = f"({'|'.join(map(re.escape, separators))})"

    # Split the input string using the pattern and keep the separators
    result: List[str] = re.split(pattern, input)

    # Recombine adjacent strings
    i: int = 0
    while i < len(result) - 1:
        combined_element: str = result[i] + result[i + 1]
        combined_array.append(combined_element)
        i += 2

    return combined_array


# Expand the dictionary by duplicating rows that have duplicated text
def build_dictionary_expanding_duplicates(dictionary: List[Dict[str, str]]) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []

    for item in dictionary:
        strings: List[str] = split_strings(item['text'], ['.', '?', '!'])
        if len(strings) == 0:
            result.append({'text': item['text'], 'start': item['start']})
        else:
            for string in strings:
                result.append({'text': string, 'start': item['start']})

    return result


# Build dictionary without duplicates
def build_dictionary_without_duplicates(dictionary):
    result = []

    for old_item in dictionary:
        if not any(new_item['text'] == old_item['text'] for new_item in result):
            result.append(old_item)

    return result


# Convert a decimal to a string
def seconds_to_time_string(time_string):

    # Calculate hours, minutes, and remaining seconds
    hours = int(time_string // 3600)
    minutes = int((time_string % 3600) // 60)
    seconds = int(time_string % 60)

    # Format the time string
    if hours == 0:
        result = f"{minutes:2}:{seconds:02}"
    else:
        result = f"{hours:2}:{minutes:02}:{seconds:02}"

    return result


# Build a dictionary with the time strings
def build_dictionary_with_time_string(dictionary):
    result = []

    for item in dictionary:
        new_time = seconds_to_time_string(item['start'])
        result.append({'text': item['text'], 'start': new_time})

    return result
