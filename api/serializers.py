from rest_framework import serializers

from .models import CoffeeOrder, CoffeeProduct


class CoffeeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeProduct
        fields = "__all__"


class CoffeeOrderSerializer(serializers.ModelSerializer):
    coffee_name = serializers.CharField(source="coffee.name", read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = CoffeeOrder
        fields = [
            "id",
            "coffee",
            "coffee_name",
            "customer_name",
            "phone_number",
            "address",
            "quantity",
            "grind_size",
            "notes",
            "status",
            "created_at",
            "total_price",
        ]
