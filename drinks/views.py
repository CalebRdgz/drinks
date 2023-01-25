# where you create all of your endpoints (certain url you can access data from)
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    # get all the drinks
    drinks = Drink.objects.all()
    # serialize the drinks
    DrinkSerializer(drink_list, many=True) # use our DrinkSerializer class
    serializer = DrinkSerializer(drinks, many=True) # create reference to the object^
    # return JSON
    return JsonResponse({"drinks": serializer.data}, safe=False)