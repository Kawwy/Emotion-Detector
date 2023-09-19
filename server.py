""" Importing Flask Libraries"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """ Function returning response to the user """
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return "Invalid Text! Please try again!"

    resp = emotion_detector(text_to_analyse)
    if resp['dominant_emotion'] is None:
        return "Invalid Text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger' : {resp['anger']},"
        f" 'disgust' : {resp['disgust']}, 'fear' : {resp['fear']}, 'joy' : {resp['joy']}"
        f" and 'sadness' : {resp['sadness']}."
        f" The dominant emotion is {resp['dominant_emotion'].upper()}"
    )

@app.route("/")
def render_page():
    """ Function returning html page to the user """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
