import csv


class CardConverter:
    """
    Converter from dog breed data to Anki card info in CSV format.
    """

    fields = [
        "breed_name",
        "breed_group",
    ]

    @staticmethod
    def _breed_group(breed):
        if "breed_group" in breed:
            return breed["breed_group"]
        return "unknown"

    def generate_csv(self, breeds, outfile):
        """
        Generate an Anki card CSV file for given data.
        """
        with open(outfile, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")

            csvfile.write("# ")
            writer.writerow(self.fields)

            for breed in breeds:
                writer.writerow(
                    [getattr(breed, field) for field in self.fields]
                )
