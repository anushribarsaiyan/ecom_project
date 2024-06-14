from rest_framework import viewsets
from .serializers import productserializers
from .models import Product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = productserializers
