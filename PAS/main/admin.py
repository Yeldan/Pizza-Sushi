from django.contrib import admin
from .models import PizzaSushi, Food, Restaurants, Menu, Customer, Order


class CustomOrder(admin.ModelAdmin):
    filter_horizontal = ('product', 'product',)


admin.site.register(PizzaSushi)
admin.site.register(Food)
admin.site.register(Restaurants)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Order, CustomOrder)


