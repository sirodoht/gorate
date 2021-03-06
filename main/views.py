from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from main import models


def index(request):
    return render(request, "main/index.html", {
        "ratings": models.Rating.objects.all().order_by("id"),
    })


def rate(request, title):
    if request.method == "GET":
        return render(
            request,
            "main/rate.html",
            {
                "title": title,
            },
        )
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
