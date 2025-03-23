from youtube_transcript_api import YouTubeTranscriptApi
# import re
from flask import Flask, request, render_template
import utilities

app = Flask(__name__)

# Get the video id from the url
# url = 'https://www.youtube.com/watch?v=btJpw6uaZ4g&list=WL&index=12'


@app.route('/')
def index():
    return render_template('index2.html')
    # data = utilities.get_transcript(url)
    # return render_template('index.html', data=data)

@app.route('/fetch', methods=['POST'])
def ask():
    url = request.form['url']
    transcript = utilities.get_transcript(url)    
    return render_template('index2.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True)

# # if __name__ == '__main__':
# app.run(debug=False)


# video_id = url.split('v=')[1]
# video_id = video_id.split('&')[0]

# print(url)
# print(video_id)


# Split a string into multiple parts using a separator
# def split_strings(input, separators):
#     combined_array = []

#     # Create a regular expression pattern to capture separators
#     pattern = f"({'|'.join(map(re.escape, separators))})"

#     # Split the input string using the pattern and keep the separators
#     result = re.split(pattern, input)

#     # Recombine adjacent strings
#     i = 0
#     while i < len(result) - 1:
#         combined_element = result[i] + result[i + 1]
#         combined_array.append(combined_element)
#         i += 2

#     return combined_array


# Expand the dictionary by duplicating rows that have duplicated text
# def build_dictionary_expanding_duplicates(dictionary):
#     result = []

#     for item in dictionary:
#         strings = split_strings(item['text'], ['.', '?', '!'])
#         if len(strings) == 0:
#             result.append({'text': item['text'], 'start': item['start']})
#         else:
#             for string in strings:
#                 result.append({'text': string, 'start': item['start']})

#     return result


# Build dictionary without duplicates
# def build_dictionary_without_duplicates(dictionary):
#     result = []

#     for old_item in dictionary:
#         if not any(new_item['text'] == old_item['text'] for new_item in result):
#             result.append(old_item)

#     return result


# Convert a decimal to a string
# def seconds_to_time_string(time_string):

#     # Calculate hours, minutes, and remaining seconds
#     hours = int(time_string // 3600)
#     minutes = int((time_string % 3600) // 60)
#     seconds = int(time_string % 60)

#     # Format the time string
#     if hours == 0:
#         result = f"{minutes:2}:{seconds:02}"
#     else:
#         result = f"{hours:2}:{minutes:02}:{seconds:02}"

#     return result


# Build a dictionary with the time strings
# def build_dictionary_with_time_string(dictionary):
#     result = []

#     for item in dictionary:
#         new_time = seconds_to_time_string(item['start'])
#         result.append({'text': item['text'], 'start': new_time})

#     return result


# Fetch the transcript
# dictionary_step_one = YouTubeTranscriptApi().fetch(video_id, languages=['de'])

# # Convert it to raw data
# dictionary_step_two = dictionary_step_one.to_raw_data()

# # Build a dictionary expanding duplicates and striping duration
# dictionary_step_three = build_dictionary_expanding_duplicates(
#     dictionary_step_two)

# # Build dictionary without duplicates
# dictionary_step_four = build_dictionary_without_duplicates(
#     dictionary_step_three)

# # Build dictionary with time as a string
# dictionary_step_five = build_dictionary_with_time_string(dictionary_step_four)




# {'text': 'Wenn du dich müde fühlst, solltest du dich ausruhen.', 'start': 1655.353, 'duration': 7.141}
