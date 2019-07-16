import requests
import json


def request_detect(config, url):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': config.key,
    }
    face_attributes = "age,gender,headPose,smile,facialHair,glasses,emotion," \
                      "hair,makeup,occlusion,accessories,blur,exposure,noise"

    data = {
        "url": url
    }

    url = config.endpoint + "/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=" \
                            + face_attributes + "&recognitionModel=recognition_01&returnRecognitionModel=false&" \
                            "detectionModel=detection_01"

    request = requests.post(url, headers=headers, data=json.dumps(data))

    print(json.dumps(request.json(), indent=4))
    print(request.status_code)
