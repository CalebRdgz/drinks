# where you create all of your endpoints (certain url you can access data from)
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# GET and POST request:
@api_view(['GET', 'POST'])
def drink_list(request):
    # if GET request:
    if request.method == 'GET':
        # get all the drinks
        drinks = Drink.objects.all()
        # serialize the drinks
        serializer = DrinkSerializer(drinks, many=True) # create reference to the object
        # return JSON
        return JsonResponse({"drinks": serializer.data})
    # if POST request:
    if request.method == 'POST':
        # add a drink to database:
        serializer = DrinkSerializer(data=request.data) # get data from the request, with reference "serializer"
        # check if data is valid:
        if serializer.is_valid(): 
            serializer.save() # save the data if it is valid
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return a response with a status code