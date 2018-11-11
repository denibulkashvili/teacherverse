from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404

from braces.views import SelectRelatedMixin

from django.views import generic

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class PostList(SelectRelatedMixin, generic.list.ListView):
    model = models.Post
    select_related = ('user', 'group')

