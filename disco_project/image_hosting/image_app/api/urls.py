# urls.py


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path("", views.ImageListView.as_view(), name="image-list"),
    path("upload/", views.ImageCreateView.as_view(), name="image-create"),

]

urlpatterns = format_suffix_patterns(urlpatterns)




