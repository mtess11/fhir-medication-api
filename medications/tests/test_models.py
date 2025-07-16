from django.test import TestCase
from medications.models import Medication

class MedicationModelTest(TestCase):
    def test_create_medication(self):
        med = Medication.objects.create( # type: ignore[attr-defined]
            code="12345-6789",
            status="active",
            manufacturer="Acme Pharma",
            form="tablet",
            identifier="TY123",
            ingredient={"active_ingredients": [{"name": "Acetaminophen", "strength": "500 mg"}]},
        )
        self.assertEqual(med.code, "12345-6789")
        self.assertEqual(med.status, "active")
        self.assertEqual(med.form, "tablet")
        self.assertEqual(med.ingredient["active_ingredients"][0]["name"], "Acetaminophen")
