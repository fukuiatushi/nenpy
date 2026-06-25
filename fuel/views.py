from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import math

from .models import FuelRecord, MaintenanceRecord, DashboardImage
from .forms import FuelRecordForm, MaintenanceForm, DashboardImageForm

def record_list(request):
    records = FuelRecord.objects.order_by('date')
    return render(request, "fuel/record_list.html", {"records": records})

def record_add(request):
    if request.method == "POST":
        form = FuelRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            latest = MaintenanceRecord.objects.order_by('-date').first()
            if latest and record.odometer > latest.next_change:
                messages.warning(request, "オイル交換時期を過ぎています。")

            if record.price_per_liter and record.fuel_liters:
                value = record.price_per_liter * record.fuel_liters
                record.total_price = math.ceil(value)

            record.save()
            return redirect('fuel:record_list')
    else:
        form = FuelRecordForm()

    return render(request, 'fuel/record_add.html', {'form': form})

def record_detail(request, pk):
    record = get_object_or_404(FuelRecord, pk=pk)
    return render(request, "fuel/record_detail.html", {"record": record})

def record_edit(request, pk):
    record = get_object_or_404(FuelRecord, pk=pk)

    if request.method == "POST":
        form = FuelRecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            if record.price_per_liter and record.fuel_liters:
                value = record.price_per_liter * record.fuel_liters
                record.total_price = math.ceil(value)

            record.save()
            return redirect('fuel:record_detail', pk=record.pk)
    else:
        form = FuelRecordForm(instance=record)

    return render(request, 'fuel/record_edit.html', {'form': form, 'record': record})

def maintenance_add(request):
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fuel:maintenance_list')
    else:
        form = MaintenanceForm()

    return render(request, 'fuel/maintenance_add.html', {'form': form})

def maintenance_list(request):
    records = MaintenanceRecord.objects.order_by('-date')
    return render(request, "fuel/maintenance_list.html", {"records": records})

from .forms import DashboardImageForm
from .models import DashboardImage

def dashboard(request):
    main_img = DashboardImage.objects.first()

    if request.method == 'POST':
        form = DashboardImageForm(request.POST, request.FILES)
        if form.is_valid():
            DashboardImage.objects.all().delete()  # ← 1枚だけにする
            form.save()
            return redirect('fuel:dashboard')
    else:
        form = DashboardImageForm()

    return render(request, 'fuel/dashboard.html', {
        'main_img': main_img,
        'form': form,
    })
