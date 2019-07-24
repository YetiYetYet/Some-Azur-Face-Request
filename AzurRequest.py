import requests
import json
from colorama import Fore
from requests import HTTPError


def request_detect(config, url):
    """
    This function send a request to the microsoft API
    It detect human faces in an image, return face rectangles with faceIds, landmarks, and attributes.
    https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236

    :type config: Config
    :type url: basestring
    :return: None
    """
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

    print(Fore.LIGHTWHITE_EX + "[REQUETE] Detect")
    try:
        request = requests.post(url, headers=headers, data=json.dumps(data))
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] Detect ok")
            print(json.dumps(request.json(), indent=4))
            return
        else:
            print(Fore.RED + "[REQUETE] Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return
