import graphene
from graphene_django.types import DjangoObjectType
from .models import Medication

class MedicationType(DjangoObjectType):
    class Meta:
        model = Medication

class Query(graphene.ObjectType):
    medications = graphene.List(MedicationType)
    medication = graphene.Field(MedicationType, id=graphene.Int())

    def resolve_medications(root, info, **kwargs):
        return Medication.objects.all()

    def resolve_medication(root, info, id):
        try:
            return Medication.objects.get(pk=id)
        except Medication.DoesNotExist:
            return None

class CreateMedication(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.String(required=True)
        manufacturer = graphene.String()

    medication = graphene.Field(MedicationType)

    def mutate(self, info, name, code, manufacturer=None):
        medication = Medication(name=name, code=code, manufacturer=manufacturer)
        medication.save()
        return CreateMedication(medication=medication)

class Mutation(graphene.ObjectType):
    create_medication = CreateMedication.Field()
