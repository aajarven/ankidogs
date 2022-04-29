import click

from src.dog_api import DogAPI
from src.card_converter import CardConverter


@click.command()
@click.argument("apikey")
@click.argument("outfile", type=click.Path())
def ankipy(apikey, outfile):
    """Create breed information CSV"""
    breeds = DogAPI(apikey).breed_data()

    card_converter = CardConverter()
    card_converter.generate_csv(breeds, outfile)


if __name__ == '__main__':
    ankipy()
