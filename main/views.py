from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from main import models


def rate(request, title):
    if request.method == "GET":
        return render(request, "main/rate.html", {
            "title": title,
        })
    elif request.method == "POST":

        class RatingForm(forms.ModelForm):
            class Meta:
                model = models.Rating
                fields = ["value"]

        form = RatingForm(request.POST)
        rating = form.save(commit=False)
        rating.title = title
        rating.save()
        return HttpResponse("rating saved")
