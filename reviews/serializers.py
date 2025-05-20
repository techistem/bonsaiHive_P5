from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    owner_profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    owner_profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url')

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'owner_username', 'owner_profile_id',
            'owner_profile_image', 'post', 'title', 'content',
            'rating', 'created_at', 'updated_at'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """

    class Meta(ReviewSerializer.Meta):
        fields = ReviewSerializer.Meta.fields + ['post']
