import pprint

import click

from src.dog_api import DogAPI


@click.command()
@click.argument("apikey")
def ankipy(apikey):
    """Print dog breed information"""
    dog_api = DogAPI(apikey)
    breed_data = dog_api.breed_data()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(breed_data)


if __name__ == '__main__':
    ankipy()
