"""
Flask server for Emotion Detection web application.
Handles routes and returns emotion analysis results.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Render the home page with the input form.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Analyze the input text and return emotion scores and dominant emotion.
    Returns an error message if the text is empty or invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
