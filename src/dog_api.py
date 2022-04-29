import requests


class DogAPI:
    """
    A tool for fetching data from https://thedogapi.com
    """

    def __init__(self, apikey):
        """
        Initialize the class.

        :apikey: API key from https://thedogapi.com/signup
        """
        self.apikey = apikey

    def breed_data(self, limit=999):
        """
        Get breed data.

        :limit: Maximum number of breeds to return. Defaults to 999 (i.e.
                significantly more than the size of the breed list).
        :returns: Breed data as list of individual breed info dicts
        """
        r = requests.get(
            "https://api.thedogapi.com/v1/breeds",
            headers={"x-api-key": self.apikey}
            )
        return r.json()
