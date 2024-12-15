import pandas as pd
from django.core.management.base import BaseCommand
from fuel.models import FuelStop

class Command(BaseCommand):
    help = 'Load fuel prices from a CSV file into the FuelStop model.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file containing fuel prices.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            # Load the CSV file
            fuel_prices_data = pd.read_csv(file_path)

            # Extract relevant columns and remove duplicates
            processed_data = fuel_prices_data[['Truckstop Name', 'City', 'State', 'Retail Price']].drop_duplicates()

            # Create FuelStop objects and save to the database
            fuel_stops = []
            for _, row in processed_data.iterrows():
                fuel_stops.append(FuelStop(
                    name=row['Truckstop Name'],
                    city=row['City'],
                    state=row['State'],
                    price_per_gallon=row['Retail Price']
                ))

            FuelStop.objects.bulk_create(fuel_stops, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS('Fuel prices loaded successfully.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error loading fuel prices: {e}'))
