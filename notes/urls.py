"""
URL configuration for openotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
<<<<<<< HEAD
from notes.views import *

urlpatterns = [
    path('<str:id>/', NotesDetailView.as_view()),
]
=======

from course.views import CourseDetailView, CourseListView
from notes.views import NotesListView, DetailNotesView, VoteView

urlpatterns = [
    path("<str:id>/",NotesListView.as_view()),
    path("<str:id1>/<str:id2>/", DetailNotesView.as_view()),
    path("<str:id1>/<str:id2>/vote/", VoteView.as_view())
]
>>>>>>> 6b79ce646afe8780f508c6f6fde1381584d4f5c5
