import requests


class APIClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get(endpoint, headers=None):
        url = f"{APIClient.BASE_URL}{endpoint}"
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(endpoint, payload=None, headers=None):
        url = f"{APIClient.BASE_URL}{endpoint}"
        response = requests.post(url, json=payload, headers=headers)
        return response