import graphene

from graphene_django.types import DjangoObjectType
from .models import User, Zona, Tour


class UserType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo User """
    class Meta:
        model = User


class TourTypeDjangoObjectType):
    """ Tipo de dato para manejar el tipo Tour """
    class Meta:
        model = Tour


class ZonaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Zona """
    class Meta:
        model = Zona


class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    all_tours = graphene.List(TourType)  # allTours
    all_zonas = graphene.List(ZonaType)  # allZonas

    # Se define las respuestas para cada campo definido
    def resolve_all_tours(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Tour.objects.all()

    def resolve_all_zonas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Zona.objects.all()

# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query)
