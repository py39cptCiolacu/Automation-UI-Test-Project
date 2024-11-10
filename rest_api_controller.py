import requests

from constants import API_KEY


class RestApiController:

    def __init__(self, base_url: str, auth: dict = None):
        self.base_url = base_url
        self.headers = self.__create_header()
        self.auth = auth

    def __create_header(self) -> dict:

        # TODO - make this configurable by the user

        default_header = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        return default_header

    def get(self, endpoint: str, params: dict = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(
                url, headers=self.headers, params=params, auth=self.auth
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(
        self,
        endpoint: str,
        data: dict = None,
        json: dict = None,
    ) -> requests.Response:

        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.post(
                url, headers=self.headers, data=data, json=json, auth=self.auth
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def put(
        self,
        endpoint: str,
        data: dict = None,
        json: dict = None,
    ) -> requests.Response:

        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(
                url, headers=self.headers, data=data, json=json, auth=self.auth
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint: str) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, headers=self.headers, auth=self.auth)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None
