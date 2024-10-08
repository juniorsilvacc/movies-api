from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer
from app.permissions import GlobalDefaultPermission

class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get(self, request):
        movies = Movie.objects.all()
        
        search = request.GET.get('search') # search?=NeedForSpeed
        if search:
            movies = Movie.objects.filter(title__icontains=search)
        
        serializer = MovieSerializer(movies, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    