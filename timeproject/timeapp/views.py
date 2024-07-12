from django.shortcuts import HttpResponse
from datetime import datetime, timedelta
def current_datetime(request):
    now = datetime.now()
    ltr = now - timedelta(hours = 4)
    html = "<html><body>Current date and time %s<br/> %s </body></html>"%(now, ltr)
    return HttpResponse(html)
