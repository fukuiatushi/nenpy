from django.shortcuts import render, redirect, get_object_or_404

from .models import FuelRecord
from .forms import FuelRecordForm

def record_list(request):
    # ★ ここを修正する
    records = FuelRecord.objects.order_by('date')

    return render(request, "fuel/record_list.html", {"records": records})

def record_add(request):
    if request.method == "POST":
        form = FuelRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fuel:record_list')
    else:
        form = FuelRecordForm()

    return render(request, 'fuel/record_add.html', {'form': form})

        
def record_detail(request,pk):
    record = get_object_or_404(FuelRecord, pk=pk)
    return render(request, "fuel/record_detail.html",{"record": record})

# Create your views here.
#訂正するための追加
def record_edit(request, pk):
    record = get_object_or_404(FuelRecord, pk=pk)

    if request.method == "POST":
        form = FuelRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('fuel:record_detail', pk=record.pk)
    else:
        form = FuelRecordForm(instance=record)

    return render(request, 'fuel/record_edit.html', {'form': form, 'record':record})

