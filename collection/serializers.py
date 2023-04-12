from rest_framework import serializers
from .models import Collection, Game_Wishlist, Game_Blacklist

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class Game_WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Wishlist
        fields = '__all__'

class Game_BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Blacklist
        fields = '__all__'
