from django.test import TestCase
from django.core.management import call_command
from medications.models import Medication
from unittest.mock import patch

class ImportFDATest(TestCase):
    @patch("medications.management.commands.import_fda_data.requests.get")
    def test_import_creates_medications(self, mock_get):
        # Mock OpenFDA response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [
                {
                    "product_ndc": "11111-2222",
                    "labeler_name": "Test Pharma",
                    "dosage_form": "tablet",
                    "generic_name": "Testmed",
                    "active_ingredients": [{"name": "Teststuff", "strength": "250mg"}],
                }
            ]
        }

        call_command("import_fda_data")

        self.assertEqual(Medication.objects.count(), 1) # type: ignore[attr-defined]
        med = Medication.objects.first() # type: ignore[attr-defined]
        self.assertEqual(med.code, "11111-2222")
        self.assertEqual(med.manufacturer, "Test Pharma")
        self.assertEqual(med.form, "tablet")
