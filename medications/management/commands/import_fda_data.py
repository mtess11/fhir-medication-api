import requests
from django.core.management.base import BaseCommand
from medications.models import Medication

class Command(BaseCommand):
    help = "Import medication data from the OpenFDA NDC API"

    def handle(self, *args, **options):
        self.stdout.write("Fetching data from OpenFDA...")

        url = "https://api.fda.gov/drug/ndc.json?limit=20"
        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write("Failed to fetch data.")
            return

        results = response.json().get("results", [])
        count = 0

        for item in results:
            try:
                medication, created = Medication.objects.get_or_create( # type: ignore[attr-defined]
                    code=item.get("product_ndc"),
                    defaults={
                        "status": "active",
                        "manufacturer": item.get("labeler_name"),
                        "form": item.get("dosage_form"),
                        "identifier": item.get("generic_name"),
                        "ingredient": {"active_ingredients": item.get("active_ingredients", [])}
                    }
                )
                if created:
                    count += 1
            except Exception as e:
                self.stderr.write(f"Error importing record: {e}")

        self.stdout.write(f"Imported {count} new medications.")
