from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie

class MovieTests(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            director="Christopher Nolan",
            genre="sci_fi",
            release_date="2010-07-16",
            rating="PG-13"
        )

    def test_list_movies(self):
        url = reverse('movie-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_movie(self):
        url = reverse('movie-detail', args=[self.movie.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)