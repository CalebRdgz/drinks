# where you create all of your endpoints (certain url you can access data from)
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# GET and POST request:
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    # if GET request:
    if request.method == 'GET':
        # get all the drinks
        # serialize the drinks
        # return JSON Response in Django REST Framework HTML view
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    # if POST request:
    if request.method == 'POST':
        # add a drink to database:
        serializer = DrinkSerializer(data=request.data) # get data from the request, with reference "serializer"
        # check if data is valid:
        if serializer.is_valid(): 
            serializer.save() # save the data if it is valid
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return a response with a status code

# build drink detail view:
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    # check if the requested ID is valid in range of existing IDs
    try:
        drink = Drink.objects.get(pk=id) # check if this is valid in range of existing IDs
    except Drink.DoesNotExist: # if something goes wrong with the request:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    # update existing data:
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete requested data:
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)