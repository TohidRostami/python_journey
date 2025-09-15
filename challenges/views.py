from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}


def index(request):
    months = list(monthly_challenges_texts.keys())

    return render(request , "challenges/index.html", {
        "months": months
    })

def monthly_challenges(request, month):
    # try:
        challenge_text = monthly_challenges_texts[month]
        return render(request , "challenges/challenge.html", {
            "text": challenge_text,
            "month_name" : month
        })
    # except:
    #     raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_texts.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month -1]
    redicrect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redicrect_path)