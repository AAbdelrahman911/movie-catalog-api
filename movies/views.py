from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class MovieListCreateView(generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'rating']


    def get(self, request, *args, **kwargs):
        movies = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(movies, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        movies = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    

class MovieDetailView(generics.GenericAPIView):
    def get_object(self):
        return Movie.objects.get(id = self.kwargs['pk'])
    
    serializer_class = MovieSerializer

    def get(self, request , *args, **kwargs):
        movie = self.get_object()
        serializer = self.get_serializer(movie)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = self.get_serializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


