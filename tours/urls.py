from django.urls import path
from graphene_django.views import GraphQLView


from . import views
from . import schema


urlpatterns = [
    path('', views.index, name='index'),
	
]
