import json
import Config
import AzurRequest
from colorama import Fore, init


init(autoreset=True)

config = Config.Config("1dba96f8e6ae4363bc6bbf9a43708f86", "https://northeurope.api.cognitive.microsoft.com/face/v1.0")
print(Fore.LIGHTWHITE_EX + "Key = " + Fore.LIGHTYELLOW_EX + config.key + Fore.RESET + "\n"
      + Fore.LIGHTWHITE_EX + "EndPoint = " + config.endpoint)

# [REQUEST] DETECT
data = AzurRequest.request_detect(config, "https://cdn.images.express.co.uk/img/dynamic/130/750x445/900176.jpg")
# [REQUEST] CREATE LARGEFACELIST
AzurRequest.request_create_largefacelist(config, "satisfyy1", "Salon Geneve 2002", "Liste des visages du salon")
# [REQUEST] LIST LARGEFACELSIT
AzurRequest.request_list_largefacelist(config)
# [REQUEST] DELETE LARGEFACELIST
AzurRequest.request_delete_largefacelist(config, "satisfyy1")
# EXTRACT FACEIDS FROM REQUEST RESULT
faceIds = []
for faceId in json.loads(data):
    faceIds.append(faceId['faceId'])
# [REQUEST] GROUP
AzurRequest.request_group(config, faceIds)
