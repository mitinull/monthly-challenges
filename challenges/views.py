from django.shortcuts import render

from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect

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
    "december": None,
}

not_found_message = "<h2 style='color:red'>This month is not supported!</h2>"


def monthly_challenge(request, month: str):
    if not month in challenges:
        raise Http404()

    return render(
        request,
        "challenges/challenge.html",
        {"challenge": challenges[month], "month": month},
    )


def monthly_challenge_by_number(request, month):
    months_list = list(challenges.keys())

    if month > len(months_list):
        raise Http404()

    redirect_url = reverse("month-challenge", args=[months_list[month - 1]])

    return HttpResponseRedirect(redirect_url)


def list_of_months(request):
    months = [month for month in challenges.keys()]
    return render(request, "challenges/index.html", {"months": months})
