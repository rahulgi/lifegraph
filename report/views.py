import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from report.forms import ReportForm

def new_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return HttpResponseRedirect('/')
    else:
        form = ReportForm()

    return render(request, 'new.html', {
        'form': form,
    })
