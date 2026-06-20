from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import math

from .models import FuelRecord,MaintenanceRecord
from .forms import FuelRecordForm, MaintenanceForm

def record_list(request):
    # ★ ここを修正する
    records = FuelRecord.objects.order_by('date')

    return render(request, "fuel/record_list.html", {"records": records})

def record_add(request):
    if request.method == "POST":
        form = FuelRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            latest = MaintenanceRecord.objects.order_by('-date').first()
            if latest and record.odometer>latest.next_change:
                messages.warning(request, "オイル交換時期を過ぎています。")
                

            # 給油金額を切り上げで計算
            if record.price_per_liter and record.fuel_liters:
                value = record.price_per_liter * record.fuel_liters
                record.total_price = math.ceil(value)

            record.save()
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
            record = form.save(commit=False)
            # 給油金額を切り上げで計算
            if record.price_per_liter and record.fuel_liters:
                value = record.price_per_liter * record.fuel_liters
                record.total_price = math.ceil(value)
            
            record.save()
            return redirect('fuel:record_detail', pk=record.pk)
    else:
        form = FuelRecordForm(instance=record)

    return render(request, 'fuel/record_edit.html', {'form': form, 'record':record})

#追加画面（maintenance_add)
def maintenance_add(request):
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fuel:maintenance_list')
    else:
        form = MaintenanceForm()
        
    return render(request, 'fuel/maintenance_add.html', {'form': form})
#一覧画面（maintenance_list)
def maintenance_list(request):
    records = MaintenanceRecord.objects.order_by('-date')#日付の新しい順に並べる
    
    return render(request, "fuel/maintenance_list.html", {"records": records})
    

