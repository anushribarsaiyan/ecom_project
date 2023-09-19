from rest_framework import serializers
from .models import Order


class Orderserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user')