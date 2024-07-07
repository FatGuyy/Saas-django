from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

def members(request):
    qs = PageVisit.objects.all().count()
    page_qs = PageVisit.objects.filter(path=request.path).count()
    context={
        "name":"Omkar Jadhav",
        "name2":"Jeff Wellington",
        "query":qs,
        "page_visits": page_qs
    }
    PageVisit.objects.create(path=request.path)
    return render(request,  "base.html", context=context)