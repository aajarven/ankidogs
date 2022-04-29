import pprint

import click

from src.dog_api import DogAPI
from src.card_converter import CardConverter


@click.command()
@click.argument("apikey")
@click.argument("outfile", type=click.Path())
def ankipy(apikey, outfile):
    """Print dog breed information"""
    breed_data = DogAPI(apikey).breed_data()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(breed_data)

    card_converter = CardConverter()
    card_converter.generate_csv(breed_data, outfile)


if __name__ == '__main__':
    ankipy()
