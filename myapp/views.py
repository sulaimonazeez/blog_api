from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer


from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def home(request):
    api_key = request.GET.get('key')
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    if not is_valid_api_key(api_key):
        return JsonResponse({'error': 'Invalid API key'}, status=401)

    # Your API logic here

    return Response(serializer.data)
@csrf_exempt
@api_view(['GET'])
def blog_detail(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=404)

    serializer = BlogSerializer(blog)
    return Response(serializer.data)
  

def is_valid_api_key(api_key):
    # Implement your API key validation logic here.
    # Check if the provided api_key is valid.
    valid_api_key = '$keyProtect'  # Replace with your actual valid API key
    return api_key == valid_api_key

  