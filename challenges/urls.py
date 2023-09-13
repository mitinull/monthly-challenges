from django.urls import path

from . import views


urlpatterns = [
    path("", views.list_of_months, name="all-challenges"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
