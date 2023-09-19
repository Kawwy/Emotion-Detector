from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotionDetect():
    text_to_analyse = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyse)
    return f"For the given statement, the system response is 'anger' : {resp['anger']}, 'disgust' : {resp['disgust']}, 'fear' : {resp['fear']}, 'joy' : {resp['joy']} and 'sadness' : {resp['sadness']}. The dominant emotion is {resp['dominant_emotion'].upper()}"

@app.route("/")
def render_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
