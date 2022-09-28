from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

class hello_world(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)