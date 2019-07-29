import requests
import json
import Config
from colorama import Fore
from requests import HTTPError
from typing import List


def request_detect(config: Config.Config, url: str) -> json:
    """
    This function send a Face-Detect [POST] request to the microsoft API
    It return the result Json or an empty Json if the request don't succed.
    It detect human faces in an image, return face rectangles with faceIds, landmarks, and attributes.

    https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395236

    :param config: object containing mandatory information for request (subscription Key and endpoint).
    :param url: The url of the images (need images extensions like .png...).
    :type config: Config
    :type url: basestring
    :return: Json file (Empty if the request fail).
    """
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': config.key,
    }
    face_attributes = "age,gender,headPose,smile,facialHair,glasses,emotion," \
                      "hair,makeup,occlusion,accessories,blur,exposure,noise"

    data = {
        # Json content
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
            return json.dumps(request.json(), indent=4)
        else:
            print(Fore.RED + "[REQUETE] Detect Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return {}

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return {}
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return {}


def request_create_largefacelist(config: Config.Config, largefacelist_id: str, name: str, user_data: str) -> bool:
    """
    This function send a [PUT] request to the microsoft API.
    Create an empty large face list with user-specified largeFaceListId, name, an optional userData
    and recognitionModel. Large face list is a list of faces, up to 1,000,000 faces, and used by Face - Find Similar.

    https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc

    :param config: object containing mandatory information for request (subscription Key and endpoint).
    :param largefacelist_id: the id of the LargeFaceList Valid character is letter in lower case or digit or '-' or '_'.
    :param name: Name of the created large face list.
    :param user_data: user defined data for the large face list.
    :return: Boolean : True if everything is ok or False when someting wrong append.
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

    url = config.endpoint + "/largefacelists/" + largefacelist_id
    print(Fore.LIGHTWHITE_EX + "[REQUETE]" + Fore.YELLOW + "[PUT]" + Fore.LIGHTWHITE_EX + " Create LargeFaceList")

    try:
        request = requests.put(url, headers=headers, data=json.dumps(data))
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] Create LargeFaceList ok")
            return True
        else:
            print(Fore.RED + "[REQUETE] Create LargeFaceList Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return False

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return False


def request_delete_largefacelist(config: Config.Config, largefacelist_id: str) -> bool:
    """
    This function send a [DELETE]request to the microsoft API.
    Delete a specified large face list.

    https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/5a157b68d2de3616c086f2cc

    :param config: object containing mandatory information for request (subscription Key and endpoint).
    :param largefacelist_id: the id of the LargeFaceList you want to delete.
    :return: Boolean : True if everything is ok or False when someting wrong append.
    """
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': config.key,
    }

    url = config.endpoint + "/largefacelists/" + largefacelist_id
    print(Fore.LIGHTWHITE_EX + "[REQUETE]" + Fore.YELLOW + "[DELETE]" + Fore.LIGHTWHITE_EX + " Delete LargeFaceList")

    try:
        request = requests.delete(url, headers=headers)
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] Delete LargeFaceList ok")
            return True
        else:
            print(Fore.RED + "[REQUETE] Delete LargeFaceList Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return False

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return False


def request_list_largefacelist(config: Config.Config) -> json:
    """
    This function send a [GET]request to the microsoft API
    It give the List large face lists’ information of largeFaceListId, name, userData and recognitionModel.
    https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/5a158387d2de3616c086f2d0

    :param config: object containing mandatory information for request (subscription Key and endpoint).
    :return: Json File with the list of LargeFaceList in this Instance (Empty if something wrong append).
    """
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
            return json.dumps(request.json(), indent=4)
        else:
            print(Fore.RED + "[REQUETE] List LargeFaceList Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return {}

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return {}
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return {}


def request_group(config: Config.Config, faces_ids: List[str]) -> json:
    """
    This function send a [POST]request to the microsoft API
    Divide candidate faces into groups based on face similarity.
    The output is one or more disjointed face groups and a messyGroup. A face group contains faces that have similar
    looking, often of the same person. Face groups are ranked by group size, i.e. number of faces.
    MessyGroup is a special face group containing faces that cannot find any similar counterpart face from original
    faces. The messyGroup will not appear in the result if all faces found their counterparts.

    https://westus.dev.cognitive.microsoft.com/docs/services/563879b61984550e40cbbe8d/operations/563879b61984550f30395238

    :param config: object containing mandatory information for request (subscription Key and endpoint).
    :param faces_ids: Array of candidate faceId created by Face - Detect.
    :return: Json File (Empty if something wrong append).
    """
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': config.key,
    }

    url = config.endpoint + "/group"
    print(Fore.LIGHTWHITE_EX + "[REQUETE]" + Fore.YELLOW + "[POST]" + Fore.LIGHTWHITE_EX + " Group")

    try:
        request = requests.post(url, headers=headers, data=json.dumps({'faceIds': faces_ids}, indent=4))
        if request.status_code == 200:
            print(Fore.GREEN + "[REQUETE] Group ok")
            print(json.dumps(request.json(), indent=4))
            return json.dumps(request.json(), indent=4)
        else:
            print(Fore.RED + "[REQUETE] Group Fail : " + request.status_code)
            print(Fore.RED + json.dumps(request.json(), indent=4))
            return {}

    except HTTPError as http_err:
        print(Fore.RED + f'HTTP error occurred: {http_err}')
        return {}
    except Exception as err:
        print(Fore.RED + f'Other error occurred: {err}')
        return {}

# def request_find_similar(config, face_ids):
