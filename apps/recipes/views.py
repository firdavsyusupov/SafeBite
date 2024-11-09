from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer


# Create your views here.
@api_view(['GET'])
def get_recipes(request):
    category = request.query_params.get('category', None)
    if category:
        recipes = Recipe.objects.filter(category=category)
    else:
        recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)
