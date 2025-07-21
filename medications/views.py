from django.shortcuts import render
from rest_framework import viewsets
from .models import Medication
from .serializers import MedicationSerializer

from typing import Any

class MedicationViewSet(viewsets.ModelViewSet):
    queryset: Any = Medication.objects.all()  # type: ignore[attr-defined]
    serializer_class = MedicationSerializer
