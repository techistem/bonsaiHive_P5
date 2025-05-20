from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from reviews.models import Review
from django.db.models import Avg
from reviews.serializers import ReviewSerializer


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model
    Includes like info, user review info, and aggregated review data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    review_id = serializers.SerializerMethodField()
    review_title = serializers.SerializerMethodField()
    review_content = serializers.SerializerMethodField()
    review_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context.get('request').user
        if user and user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_review_data(self, obj):
        """
        Helper method to fetch the current user's review for the given post.
        """
        user = self.context.get('request').user
        if user and user.is_authenticated:
            return Review.objects.filter(owner=user, post=obj).first()
        return None

    def get_review_id(self, obj):
        review = self.get_review_data(obj)
        return review.id if review else None

    def get_review_title(self, obj):
        review = self.get_review_data(obj)
        return review.title if review else None

    def get_review_content(self, obj):
        review = self.get_review_data(obj)
        return review.content if review else None

    def get_review_rating(self, obj):
        review = self.get_review_data(obj)
        return review.rating if review else None

    def get_review_count(self, obj):
        return obj.reviews.count()

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 2) if avg is not None else None

    def validate_image(self, value):
        """
        Validates image dimensions and file size.
        """
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 5MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!')
        return value

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'content',
            'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
            'review_id', 'review_title', 'review_content',
            'review_rating', 'review_count', 'average_rating',
            'reviews'
        ]