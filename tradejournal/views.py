from django.shortcuts import render, get_object_or_404
from .models import tradingjournal

# Create your views here.
def journal(request):
    mytradejournal = tradingjournal.objects.all().order_by('-trade_date')   
    return render(request, 'tradejournals.html', {'mytradejournal':mytradejournal})

def journaldetail(request, journal_id):
    myjournaldetail = get_object_or_404(tradingjournal, pk=journal_id)
    return render(request, 'tradejournaldetail.html', {'myjournaldetail':myjournaldetail})
