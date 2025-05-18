from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from reviews.models import Review
from django.db.models import Avg


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the post model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    review_id = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    review_title = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    review_rating = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Validates the image file size and height
        and sends a message if file is too large to upload
        """
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 5MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_like_id(self, obj):
        """
        returns the like id if it exists for the post
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_is_owner(self, obj):
        """
        returns true if the user making rthe request is
        the owner of the object
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def get_review_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(
                owner=user, post=obj
            ).first()
            return review.id if review else None
        return None
    
    def get_review_title(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(owner=user, post=obj).first()
            return review.title if review else None
        return None

    def get_review_content(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(owner=user, post=obj).first()
            return review.content if review else None
        return None

    def get_review_rating(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(owner=user, post=obj).first()
            return review.rating if review else None
        return None
    
    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 2) if avg else None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
            'review_id', 'average_rating',
            'review_title', 'review_content', 'review_rating',
        ]