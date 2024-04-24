from django.shortcuts import render
from rest_framework import viewsets
from .models import Post , Category, Comment
from django.shortcuts import get_object_or_404
# Create your views here.

from .serializers import PostSerializer , CategorySerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# def get_name(request ,category_id):
#     try:
#         category = get_object_or_404( Category , pk=category_id)
#         category_data = category.
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer        

from django.http import JsonResponse







def get_all_posts_with_categories(request):
    try:
        posts = Post.objects.all()

        # Prepare data for all posts with nested category data
        posts_data = []
        for post in posts:
            post_data = {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author,
                "slug": post.slug,
                "created_on": post.created_on,
                "last_modified": post.last_modified,
                "categories": []  # Initialize an empty list for categories
            }
            # Fetch categories associated with the post
            categories = post.category.all()
            for category in categories:
                post_data["categories"].append({
                    "id": category.id,
                    "name": category.name
                })
            posts_data.append(post_data)

        return JsonResponse({"posts": posts_data})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)