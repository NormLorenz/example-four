from youtube_transcript_api import YouTubeTranscriptApi
import requests

# Get the video id from the url
url = 'https://www.youtube.com/watch?v=btJpw6uaZ4g&list=WL&index=12'
video_id = url.split('v=')[1]
video_id = video_id.split('&')[0]

print(url)
print(video_id)


# Split a string into multiple parts using a separator
def split_strings(input, separator):
    result = []

    if separator in input:
        parts = input.split(separator)
        if len(parts) == 3:
            parts[0] = (parts[0] + separator).strip()
            parts[1] = (parts[1] + separator).strip()
            result = parts

    return result


# Expand the dictionary by duplicating rows that have duplicated text
def build_dictionary_expanding_duplicates(dictionary):
    result = []

    for item in dictionary:
        periods = split_strings(item['text'], '.')
        questions = split_strings(item['text'], '?')
        exclamation = split_strings(item['text'], '!')
        if len(periods) == 3:
            result.append({'text': periods[0], 'start': item['start']})
            result.append({'text': periods[1], 'start': item['start']})
        elif len(questions) == 3:
            result.append({'text': questions[0], 'start': item['start']})
            result.append({'text': questions[1], 'start': item['start']})
        elif len(exclamation) == 3:
            result.append({'text': exclamation[0], 'start': item['start']})
            result.append({'text': exclamation[1], 'start': item['start']})
        else:
            result.append({'text': item['text'], 'start': item['start']})

    return result


def build_dictionary_without_duplicates(dictionary):
    result = []

    for item in dictionary:
        if item not in result:
            result.append(item)

    return result


# Fetch the transcript
dictionary_step_one = YouTubeTranscriptApi().fetch(
    video_id, languages=['de'])
# print(dictionary_step_one)

# Convert it to raw data
dictionary_step_two = dictionary_step_one.to_raw_data()
print(len(dictionary_step_two))
# print(dictionary_step_two)

# Build a dictionary expanding duplicates and striping duration
dictionary_step_three = build_dictionary_expanding_duplicates(
    dictionary_step_two)
print(len(dictionary_step_three))
print(dictionary_step_three)


# Get the transcript step 2 - duplicate rows that have duplicated text and build a new dictionary

# Get the transcript step 3 - build the final dictionary without not duplicates

# Get the transcript step 4 - convert a float to a time string

# Get the transcript step 5 - print the final dictionary


# {'text': 'Wenn du dich müde fühlst, solltest du dich ausruhen.', 'start': 1655.353, 'duration': 7.141}
