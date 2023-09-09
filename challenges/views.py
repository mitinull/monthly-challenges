from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

challenges = {"january": "Exercise 30 min every other day!"}


def monthly_challenge(request, month):
    if not month in challenges:
        return HttpResponseNotFound("this month is not supported!")
    return HttpResponse(challenges[month])
