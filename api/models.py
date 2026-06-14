from django.db import models
from django.utils.text import slugify


class CoffeeProduct(models.Model):
    class RoastLevel(models.TextChoices):
        LIGHT = "light", "Light Roast"
        MEDIUM = "medium", "Medium Roast"
        DARK = "dark", "Dark Roast"

    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    tagline = models.CharField(max_length=180)
    description = models.TextField()
    origin = models.CharField(max_length=120, default="Danau Toba, Sumatera Utara")
    roast_level = models.CharField(
        max_length=20,
        choices=RoastLevel.choices,
        default=RoastLevel.MEDIUM,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    intensity = models.PositiveSmallIntegerField(default=3)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CoffeeOrder(models.Model):
    class GrindSize(models.TextChoices):
        BEANS = "beans", "Biji utuh"
        FINE = "fine", "Fine grind"
        MEDIUM = "medium", "Medium grind"
        COARSE = "coarse", "Coarse grind"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        BREWING = "brewing", "Brewing"
        DELIVERED = "delivered", "Delivered"
        CANCELED = "canceled", "Canceled"

    coffee = models.ForeignKey(
        CoffeeProduct,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    customer_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=30)
    address = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    grind_size = models.CharField(
        max_length=20,
        choices=GrindSize.choices,
        default=GrindSize.BEANS,
    )
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer_name} - {self.coffee.name}"

    @property
    def total_price(self):
        return self.coffee.price * self.quantity
