from django.shortcuts import HttpResponse, render
from .forms import CsvModelForm
from .models import Csv 
import csv


# Create your views here.
def index(request):
    #return HttpResponse("this is home page")
    return render(request, 'index.html')
def about(request):
    return HttpResponse("this is about page")
def data(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        #obj=Csv
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row =" ".join(row)
                    row = row.replace(';',' ')
                    row = row.split()
                    x=row[0]
                    y=row[1]
                    x=row[2]

                    #name=row[2].upper()
                    print(y)
                    #print(type(x))
                    #print(name)
                    #print(row)
                    #print(type(row))
            obj.activated = True
            obj.save()

    return render(request, 'data.html', {'form':form})
def plot(request):
    return render(request, 'plot.html')
def homepage(request):
    return render(request, 'homepage.html')