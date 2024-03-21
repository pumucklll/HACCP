import datetime
from django.views.generic import ListView
from .models import Audit_Ereignis
from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Checkliste, ObjektOrt, Audit, MangelArt, Benutzer, Audit_Ereignis, oknok
from django.shortcuts import render, redirect
from .forms import CSVImportForm
import csv


class AllToDos(ListView):
    model = Audit_Ereignis
    template_name = "index.html"


#  def get_queryset(self):
#       return ToDoItem.objects.filter(due_date__gte=datetime.date.today())

class TodayToDos(ListView):
    model = Audit_Ereignis
    template_name = "today.html"


#   def get_queryset(self):
#       return ToDoItem.objects.filter(due_date=datetime.date.today())


# Import export
def home(request):
    return render(request, 'csv/home.html')





def export_query_to_csv(request):
    data = Audit_Ereignis.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Export_Audit_Ereignis.csv"'

    writer = csv.writer(response)
    writer.writerow(['checkliste', 'objektort', 'pruefpunkt', 'ok', 'mangel', 'frist', 'behoben', 'von'])  # CSV header

    for audit in data:
        writer.writerow([audit.checkliste, audit.objektort, audit.pruefpunkt, audit.ok,
                         audit.mangel, audit.frist, audit.behoben, audit.von])

    return response





def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file, delimiter=",")

            for row in csv_reader:
                Audit_Ereignis.objects.create(
                    checkliste=Checkliste.objects.get(name=row["checkliste"]),
                    pruefpunkt=Audit.objects.get(name=row['pruefpunkt']),
                    ok=oknok.objects.get(name=row['ok']),
                    objektort=ObjektOrt.objects.get(name=row['objektort']),
                    mangel=MangelArt.objects.get(name=row['mangel']),
                    frist=row['frist'],
                    behoben=row['behoben'],
                    von=Benutzer.objects.get(name=row['von']),
                )

            return redirect('csv/home')  # Redirect to a success page
    else:
        form = CSVImportForm()

    return render(request, 'csv/import.html', {'form': form})
