from django.contrib import admin
from .models import FuelRecord

@admin.register(FuelRecord)
class FuelRecordAdmin(admin.ModelAdmin):
    list_display = ("date", "odometer", "fuel_liters", "fuel_efficiency_display")
    readonly_fields = ("fuel_efficiency_display",)

    fields = (
        "date",
        "odometer",
        "fuel_liters",
        "price_per_liter",
        "memo",
        "fuel_efficiency_display",
    )

    def fuel_efficiency_display(self, obj):
        if obj.fuel_efficiency:
            return f"{obj.fuel_efficiency} km/L"
        return "-"
    fuel_efficiency_display.short_description = "燃費"



# Register your models here.
