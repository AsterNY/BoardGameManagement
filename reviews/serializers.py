from rest_framework import serializers
from .models import GameReviewRating

class GameReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameReviewRating
        fields = ('id', 'custom_user', 'game', 'review', 'rating', 'timestamp')
