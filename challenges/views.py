from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

challenges = {"january": "Exercise 30 min every other day!"}

months_list = ["january"]


def monthly_challenge(request, month):
    if not month in challenges:
        return HttpResponseNotFound("this month is not supported!")
    return HttpResponse(challenges[month])


def monthly_challenge_by_number(request, month):
    if month > len(months_list):
        return HttpResponseNotFound("this month is not supported!")

    return monthly_challenge(request, months_list[month - 1])
