import requests
import json
import Config
from colorama import Fore
from requests import HTTPError


def request_detect(config: Config.Config, url: str):
    """
    This function send a Face-Detect [POST]request to the microsoft API
    It detect human faces in an image, return face rectangles with faceIds, landmarks, and attributes.
    https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236

    :param config: object containing mandatory information for request (subscription Key and endpoint).
    :param url: The url of the images (need images extensions like .png...)
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

    print(Fore.LIGHTWHITE_EX + "[REQUETE]" + Fore.YELLOW + "[POST]" + Fore.LIGHTWHITE_EX + " Detect")
    try:
        request = requests.post(url, headers=headers, data=json.dumps(data))
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] Detect ok")
            print(json.dumps(request.json(), indent=4))
            return
        else:
            print(Fore.RED + "[REQUETE] Detect Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return


def request_create_largefacelist(config: Config.Config, large_face_list_id: str, name: str, user_data: str):
    """

    :param config:
    :param large_face_list_id:
    :param name:
    :param user_data:
    :return:
    """
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': config.key,
    }

    data = {
        "name": name,
        "userData": user_data,
        "recognitionModel": "recognition_02"
    }

    url = config.endpoint + "/largefacelists/" + large_face_list_id
    print(Fore.LIGHTWHITE_EX + "[REQUETE]" + Fore.YELLOW + "[PUT]" + Fore.LIGHTWHITE_EX + " Create LargeFaceList")

    try:
        request = requests.put(url, headers=headers, data=json.dumps(data))
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] Create LargeFaceList ok")
            return
        else:
            print(Fore.RED + "[REQUETE] Create LargeFaceList Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return


def request_delete_largefacelist(config: Config.Config, large_face_list_id: str):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': config.key,
    }

    url = config.endpoint + "/largefacelists/" + large_face_list_id
    print(Fore.LIGHTWHITE_EX + "[REQUETE]" + Fore.YELLOW + "[DELETE]" + Fore.LIGHTWHITE_EX + " Delete LargeFaceList")

    try:
        request = requests.delete(url, headers=headers)
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] Delete LargeFaceList ok")
            return
        else:
            print(Fore.RED + "[REQUETE] Delete LargeFaceList Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return


def request_list_largefacelist(config: Config.Config):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': config.key,
    }

    url = config.endpoint + "/largefacelists"
    print(Fore.LIGHTWHITE_EX + "[REQUETE]" + Fore.YELLOW + "[GET]" + Fore.LIGHTWHITE_EX + " List LargeFaceList")

    try:
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] List LargeFaceList ok")
            print(json.dumps(request.json(), indent=4))
            return
        else:
            print(Fore.RED + "[REQUETE] List LargeFaceList Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return
