from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, render_template
import utilities

app = Flask(__name__)

# url = 'https://www.youtube.com/watch?v=btJpw6uaZ4g&list=WL&index=12'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def ask():
    url = request.form['url']
    transcript = utilities.get_transcript(url)    
    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True)
