from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course_project.admin_panel.models import Users
from course_project.admin_panel.serializers import UsersSerializer


@api_view(['GET', 'POST'])
def get_user_api(request, telegram_id):
    data = Users.objects.filter(telegram_id=telegram_id).first()
    serializer = UsersSerializer(data, context={'request': request})
    return Response(serializer.data)
