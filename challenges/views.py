from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.urls import reverse

# Create your views here.

challenges = {
    "january": "Learn a new programming language or framework.",
    "february": "Start a daily exercise routine and stick to it.",
    "march": "Read a book from a genre you've never explored before.",
    "april": "Learn to cook a new type of cuisine.",
    "may": "Take up a new hobby or craft, like painting or knitting.",
    "june": "Set a savings goal and create a budget to achieve it.",
    "july": "Volunteer for a local charity or community organization.",
    "august": "Learn a musical instrument or improve your skills if you already play one.",
    "september": "Take a weekend getaway to explore a new city or town.",
    "october": "Challenge yourself to complete a physical fitness event, like a 5k run or a bike race.",
    "november": "Practice mindfulness and meditation for at least 15 minutes every day.",
    "december": "Create a list of personal or professional goals for the upcoming year and make a plan to achieve them.",
}

not_found_message = "<h2 style='color:red'>This month is not supported!</h2>"


def monthly_challenge(request, month):
    if not month in challenges:
        return HttpResponseNotFound(not_found_message)

    return render(request, "challenges/challenge.html")


def monthly_challenge_by_number(request, month):
    months_list = list(challenges.keys())

    if month > len(months_list):
        return HttpResponseNotFound(not_found_message)

    redirect_url = reverse("month-challenge", args=[months_list[month - 1]])

    return HttpResponseRedirect(redirect_url)


def list_of_months(request):
    months_elements = [
        f'<li><a href="{month}">{month.capitalize()}</a></li>'
        for month in challenges.keys()
    ]
    return HttpResponse(
        f"<h2 style='color:green;'>List of months</h2> <ul>{''.join(months_elements)}</ul>"
    )
