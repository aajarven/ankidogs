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
        :returns: Breed data as list of Breeds
        """
        r = requests.get(
            "https://api.thedogapi.com/v1/breeds",
            headers={"x-api-key": self.apikey}
            )
        breed_data = r.json()
        return [Breed(breed_dict) for breed_dict in breed_data]


class Breed:
    """
    Representation for a dog breed
    """
    def __init__(self, breed_dict):
        """
        Create a new breed

        :breed_dict: Breed information as a dict from thedogapi.com
        """
        self.data = breed_dict

    def _get(self, key, default=""):
        """
        Return field value from breed data dict.

        If field is not found, the default value is returned.
        """
        if key in self.data:
            return self.data[key]
        return default

    @property
    def breed_name(self):
        return ""

    @property
    def english_name(self):
        return self._get("name")

    @property
    def alternative_names(self):
        return ""

    @property
    def breed_group(self):
        return self._get("breed_group")

    @property
    def image_url(self):
        if "image" in self.data:
            return self.data["image"]["url"]
        return ""

    @property
    def origin_country(self):
        return ""

    @property
    def use(self):
        return self._get("bred_for")

    @property
    def personality(self):
        return self._get("temperament")

    @property
    def weight(self):
        if "weight" in self.data:
            return "{} kg".format(self.data["weight"]["metric"])
        return ""

    @property
    def height(self):
        if "height" in self.data:
            return "{} cm".format(self.data["height"]["metric"])
        return ""
