from django.db import models

class Medication(models.Model):
    code = models.CharField(max_length=100)  # FHIR: code.coding.code
    status = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="active | inactive | entered-in-error"
    )
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    form = models.CharField(max_length=100, blank=True, null=True)  # FHIR: code.coding.display or form.text
    identifier = models.CharField(max_length=100, blank=True, null=True)  # e.g. NDC or internal ID
    ingredient = models.JSONField(blank=True, null=True)  # FHIR: list of ingredients
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code or "Unnamed Medication"
