from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import generics

from .forms import CoffeeOrderForm
from .models import CoffeeOrder, CoffeeProduct
from .serializers import CoffeeOrderSerializer, CoffeeProductSerializer


def home(request):
    products = CoffeeProduct.objects.filter(is_available=True)
    product_count = products.count()
    order_count = CoffeeOrder.objects.count()

    if request.method == "POST":
        form = CoffeeOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(
                request,
                f"Pesanan untuk {order.coffee.name} sudah masuk. Tim Coffee Toba akan segera menghubungi Anda.",
            )
            return HttpResponseRedirect(f"{request.path}#order")
        messages.error(
            request,
            "Form pesanan belum lengkap. Silakan cek kembali data yang Anda isi.",
        )
    else:
        initial_coffee = products.first()
        form = CoffeeOrderForm(initial={"coffee": initial_coffee.id if initial_coffee else None})

    context = {
        "products": products,
        "order_form": form,
        "product_count": product_count,
        "order_count": order_count,
        "features": [
            {
                "title": "Single Origin Character",
                "description": "Racikan kopi dengan karakter earthy, rempah lembut, dan aftertaste hangat khas dataran tinggi sekitar Danau Toba.",
            },
            {
                "title": "Inspired by Batak Heritage",
                "description": "Visual dan rasa membawa identitas Toba melalui nuansa tenun, lanskap danau, dan aroma yang terasa akrab sekaligus premium.",
            },
            {
                "title": "Ready to Order",
                "description": "Pengunjung sekarang bisa langsung memilih kopi favorit dan mengirim pesanan dari landing page.",
            },
        ],
        "selling_points": [
            "Aroma smoky-caramel yang langsung terasa sejak seduhan pertama.",
            "Cita rasa hangat dengan sentuhan nutty dan body yang lembut.",
            "Form order langsung terkirim ke database untuk diproses dari admin.",
        ],
        "stats": [
            {"value": "100%", "label": "Arabika Sumatera Utara"},
            {"value": str(product_count or 3), "label": "Varian tersedia"},
            {"value": str(order_count), "label": "Pesanan masuk"},
        ],
        "taste_notes": [
            "Dark cocoa",
            "Caramel palm sugar",
            "Warm spice finish",
        ],
        "api_links": [
            {"label": "Coffee Product API", "path": "/api/coffees/"},
            {"label": "Coffee Order API", "path": "/api/orders/"},
        ],
    }
    return render(request, "api/home.html", context)


class CoffeeProductListCreate(generics.ListCreateAPIView):
    serializer_class = CoffeeProductSerializer

    def get_queryset(self):
        return CoffeeProduct.objects.all()


class CoffeeProductRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoffeeProduct.objects.all()
    serializer_class = CoffeeProductSerializer
    lookup_field = "pk"


class CoffeeOrderListCreate(generics.ListCreateAPIView):
    serializer_class = CoffeeOrderSerializer

    def get_queryset(self):
        return CoffeeOrder.objects.select_related("coffee")


class CoffeeOrderRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoffeeOrder.objects.select_related("coffee")
    serializer_class = CoffeeOrderSerializer
    lookup_field = "pk"
