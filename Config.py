class Config(object):
    """
    Class containing mandatory information for request.

    :param key: The subscription keys used to access to your Cognitive Service API
    :param endpoint: The endpoint of your subcriptions used to access to your Cognitive Service API
    :type key: basestring
    :type endpoint: basestring

    Example :

    :Example:
    config = AzurConfig("1dba96f8e6ae4363bc6bbf9a43708f86", "https://northeurope.api.cognitive.microsoft.com/face/v1.0")
    """
    def __init__(self, key, endpoint):
        self.key = key
        self.endpoint = endpoint


