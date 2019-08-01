import json
import time

import Config
import AzurRequest
from colorama import Fore, init


init(autoreset=True)

config = Config.Config("1dba96f8e6ae4363bc6bbf9a43708f86", "https://northeurope.api.cognitive.microsoft.com/face/v1.0")
print(Fore.LIGHTWHITE_EX + "Key = " + Fore.LIGHTYELLOW_EX + config.key + Fore.RESET + "\n"
      + Fore.LIGHTWHITE_EX + "EndPoint = " + config.endpoint)

# [REQUEST] DETECT
# -> Caitline Jenner avant après
data = AzurRequest.request_detect(config, "https://cdn.images.express.co.uk/img/dynamic/130/750x445/900176.jpg")
# -> Chaterine Deneuve
data2 = AzurRequest.request_detect(config, "https://www.francetvinfo.fr/image/7550ntso8-9097/1200/450/6159205.jpg")
# -> Visage Homme
data3 = AzurRequest.request_detect(config, "https://www.researchgate.net/profile/Ammar_Chouchane/publication/303899174/figure/fig2/AS:614128183959558@1523430977947/Exemple-de-quelques-variations-dexpressions-faciales-de-la-meme-personne-1233-La.png")
# [REQUEST] CREATE LARGEFACELIST
AzurRequest.request_create_largefacelist(config, "satisfyy-test", "Salon Geneve 2002", "Liste des visages du salon")
# [REQUEST] LIST LARGEFACELSIT
AzurRequest.request_list_largefacelist(config)
# EXTRACT FACEIDS FROM REQUEST RESULT
faceIds = []
for faceId in json.loads(data):
    faceIds.append(faceId['faceId'])
for faceId in json.loads(data2):
    faceIds.append(faceId['faceId'])
for faceId in json.loads(data3):
    faceIds.append(faceId['faceId'])
# [REQUEST] GROUP
group_results = AzurRequest.request_group(config, faceIds)
# [REQUEST] ADD FACE
persistedFaceIds = [AzurRequest.request_add_face(config, "satisfyy-test",
                                            "https://www.francetvinfo.fr/image/7550ntso8-9097/1200/450/6159205.jpg"),
                    AzurRequest.request_add_face(config, "satisfyy-test",
                                            "https://www.francetvinfo.fr/image/7550ntso8-9097/1200/450/6159205.jpg"),
                    AzurRequest.request_add_face(config, "satisfyy-test",
                                            "https://www.francetvinfo.fr/image/7550ntso8-9097/1200/450/6159205.jpg")]
# JUST IN CASE FOR REQUEST LIMITATIONS
time.sleep(2)
# [REQUEST] TRAIN
AzurRequest.request_train_largefacelist(config, "satisfyy-test")
# [REQUEST] GET TRAIN STATUS
AzurRequest.request_get_train_status(config, "satisfyy-test")
# [REQUEST] FIND SIMILAR
findSimilarResult = AzurRequest.request_findsimilar(config, "satisfyy-test", faceIds)
# [REQUEST] DELETE FACE
AzurRequest.request_delete_face(config, "satisfyy-test", persistedFaceIds[0])
# [REQUEST] FACE LIST
AzurRequest.request_list_face(config, "satisfyy-test")
# [REQUEST] DELETE LARGEFACELIST
AzurRequest.request_delete_largefacelist(config, "satisfyy-test")
