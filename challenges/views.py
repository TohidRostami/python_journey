from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
monthly_challenges_texts = {
    "january": "Eat no meat for the whole month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Read 10 pages of a book each day!",
    "april": "Practice meditation for 10 minutes daily!",
    "may": "Drink at least 2 liters of water every day!",
    "june": "Wake up before 7 AM every day!",
    "july": "Write down 3 things you’re grateful for each day!",
    "august": "Learn something new for at least 20 minutes daily!",
    "september": "Spend at least 15 minutes journaling each day!",
    "october": "Do a 30-minute workout at least 4 times a week!",
    "november": "Avoid added sugar for the whole month!",
    "december": "Reflect on your year by writing weekly summaries!",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_texts.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_texts[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_texts.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month -1]
    redicrect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redicrect_path)