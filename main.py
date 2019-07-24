import Config
from colorama import Fore, init
import AzurRequest


init(autoreset=True)

config = Config.Config("1dba96f8e6ae4363bc6bbf9a43708f86", "https://northeurope.api.cognitive.microsoft.com/face/v1.0")
print(Fore.LIGHTWHITE_EX + "Key = " + Fore.LIGHTYELLOW_EX + config.key + Fore.RESET + "\n"
      + Fore.LIGHTWHITE_EX + "EndPoint = " + config.endpoint)

AzurRequest.request_detect(config, "https://cdn.images.express.co.uk/img/dynamic/130/750x445/900176.jpg")
AzurRequest.request_create_largefacelist(config, "test1", "ugh", "description ugh")
AzurRequest.request_list_largefacelist(config)
AzurRequest.request_delete_largefacelist(config, "test1")
