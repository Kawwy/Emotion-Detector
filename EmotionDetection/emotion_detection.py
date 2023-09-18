import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    resp = requests.post(URL, json = myobj, headers = header)
    fmt_resp = json.loads(resp.text)

    anger_score = int(fmt_resp['emotionPredictions']['emotion']['anger'])
    disgust_score = int(fmt_resp['emotionPredictions']['emotion']['disgust'])
    fear_score = int(fmt_resp['emotionPredictions']['emotion']['fear'])
    joy_score = int(fmt_resp['emotionPredictions']['emotion']['joy'])
    sadness_score = int(fmt_resp['emotionPredictions']['emotion']['sadness'])

    key = list(fmt_resp['emotionPredictions']['emotion'].keys())
    value =  list(fmt_resp['emotionPredictions']['emotion'].values())
    dominant_value = key[value.index(max(value))]

    emotions = {
        "anger" : anger_score,
        "disgust" : disgust_score,
        "fear" : fear_score,
        "joy" : joy_score,
        "sadness" : sadness_score,
        "dominant_emotion" : dominant_value
    }

    return emotions
