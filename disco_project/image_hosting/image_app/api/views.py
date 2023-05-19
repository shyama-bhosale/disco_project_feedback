# views.py

#code below is working
from rest_framework import generics, permissions
from image_app.models import Image
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# from image_app.models import Image, AccountPlan, ExpiringLink
# from .serializers import ImageSerializer, AccountPlanSerializer
from datetime import datetime, timedelta
import random
import string
import mimetypes
from django.http import FileResponse
from rest_framework import generics
from rest_framework.exceptions import NotFound, PermissionDenied
from image_app.models import ExpiringLink, Image
from .serializers import (
    ExpiringLinkCreateSerializer,
    ExpiringLinkListSerializer,
    ImageCreateSerializer,
    ImageListSerializer,
)


class ImageListView(generics.ListAPIView):
    serializer_class = ImageListSerializer

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class ImageCreateView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageCreateSerializer

