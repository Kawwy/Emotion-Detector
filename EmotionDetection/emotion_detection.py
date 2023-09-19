import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    resp = requests.post(URL, json = myobj, headers = header)
    fmt_resp = json.loads(resp.text)

    anger_score = float(fmt_resp['emotionPredictions'][0]['emotion']['anger'])
    disgust_score = float(fmt_resp['emotionPredictions'][0]['emotion']['disgust'])
    fear_score = float(fmt_resp['emotionPredictions'][0]['emotion']['fear'])
    joy_score = float(fmt_resp['emotionPredictions'][0]['emotion']['joy'])
    sadness_score = float(fmt_resp['emotionPredictions'][0]['emotion']['sadness'])

    key = list(fmt_resp['emotionPredictions'][0]['emotion'].keys())
    value =  list(fmt_resp['emotionPredictions'][0]['emotion'].values())

    dominant_value = key[value.index(max(value))]

    if resp.status_code == 200:
        emotions = {
        "anger" : anger_score,
        "disgust" : disgust_score,
        "fear" : fear_score,
        "joy" : joy_score,
        "sadness" : sadness_score,
        "dominant_emotion" : dominant_value
    }
    elif resp.status_code == 400:
        emotions = {
        "anger" : None,
        "disgust" : None,
        "fear" : None,
        "joy" : None,
        "sadness" : None,
        "dominant_emotion" : None
    }

    return emotions
