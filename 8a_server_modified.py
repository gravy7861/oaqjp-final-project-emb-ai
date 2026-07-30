"""Flask server for the emotion detection application."""

from flask import Flask, request, render_template

from emotion_detection import emotion_detector


APP = Flask(__name__)


@APP.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@APP.route("/emotionDetector")
def detect_emotion():
    """Analyze submitted text and return its detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
