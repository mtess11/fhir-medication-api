import graphene
import medications.schema

class Query(medications.schema.Query, graphene.ObjectType):
    pass

class Mutation(medications.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

