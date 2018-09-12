import requests
import json


class BaseEloquaHandler(object):
    login_url = 'https://login.eloqua.com/id'
    headers = {'Content-Type': 'application/json'}
    endpoint = ""
    api_version = '2.0'

    def __init__(self, company, username, password):
        self.auth = (company + '\\' + username, password)

        req = requests.get(self.login_url, auth=self.auth)
        self.user_id = req.json()['user']['id']
        self.user_display = req.json()['user']['displayName']
        self.url_base = req.json()['urls']['base']
        self.site_id = req.json()['site']['id']
        self.app_bs_un = req.json()['urls']['apis'][
            'rest']['standard']
        self.app_base = self.app_bs_un.format(
            version=self.api_version)
        self.bulk_bs_un = req.json()['urls']['apis']['rest']['bulk']
        self.bulk_base = self.bulk_bs_un.format(
            version=self.api_version)

        self.request_url = "{base}/{endpoint}".format(base=self.app_base,
                                                      endpoint=self.endpoint)

    @staticmethod
    def _url(base, endpoint):
        return "{}/{}".format(base, endpoint)

    def _post(self, base: str, endpoint: str, data=None):
        """
        Posts data as a json to the endpoint defined by the base and endpoint

        If no data is passed, doesn't include it in the request body
        :param base: (str) base url for the request (i.e. 'https://secure.p01.eloqua.com/API/REST/2.0/')
        :param endpoint: (str) specific endpoint for the request (i.e. 'contacts/data')
        :param data: (dict) payload to post, converted to json string
        :return: Response object returned by API
        """
        if data:
            return requests.post(self._url(base, endpoint), auth=self.auth,
                                 headers=self.headers,
                                 data=json.dumps(data))
        return requests.post(self._url(base, endpoint), auth=self.auth,
                             headers=self.headers)

    def app_get(self, endpoint):
        return requests.get(self._url(self.app_base, endpoint), auth=self.auth)

    def bulk_get(self, endpoint):
        return requests.get(self._url(self.bulk_base, endpoint), auth=self.auth)

    def app_post(self, endpoint, data=None):
        return self._post(self.app_base, endpoint, data)

    def bulk_post(self, endpoint, data=None):
        return self._post(self.bulk_base, endpoint, data)

    def app_delete(self, endpoint):
        return requests.delete(self._url(self.app_base, endpoint),
                               auth=self.auth)

