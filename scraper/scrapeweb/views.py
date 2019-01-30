from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import time


def fetch_website(request):
    headers = {
        'User-Agent': 'Mozilla/64.0.2',
        'From': 'youremail@domain.com'  # This is another valid field
    }
    year = request.GET.get("year", None)
    session = request.GET.get("session", None)
    if not year:
        year = 2019
    if not session:
        session = "S"
    data = None
    while data is None:
        try:
            data = requests.get("https://web.stevens.edu/roomsched/?year=" + str(year) + "&session="+session, headers=headers).content
        except:
            time.sleep(5)
            continue
    soup = BeautifulSoup(data, 'html.parser')
    # soup.form.decompose()
    return HttpResponse(soup.prettify())

