from django.db.models import ObjectDoesNotExist
import graphene
from graphene_django.types import DjangoObjectType
from .models import Medication

class MedicationType(DjangoObjectType):
    class Meta:
        model = Medication

class Query(graphene.ObjectType):
    medications = graphene.List(MedicationType)
    medication = graphene.Field(MedicationType, id=graphene.Int())

    def resolve_medications(root, info):
        return Medication.objects.all()  # type: ignore[attr-defined]

    def resolve_medication(root, info, id):
        try:
            return Medication.objects.get(pk=id)  # type: ignore[attr-defined]
        except ObjectDoesNotExist:
            return None

class CreateMedication(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.String(required=True)
        manufacturer = graphene.String()

    medication = graphene.Field(MedicationType)

    @staticmethod
    def mutate(root, info, name, code, manufacturer=None):
        medication = Medication(name=name, code=code, manufacturer=manufacturer)
        medication.save()
        return CreateMedication(medication=medication)  # type: ignore[reportAttributeAccessIssue]

class Mutation(graphene.ObjectType):
    create_medication = CreateMedication.Field()