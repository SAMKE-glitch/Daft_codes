"""
Database models for customers, orders, and uploaded photos.
"""

from django.db import models


class Customer(models.Model):
    """Represents a customer with contact details."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        """Return a human-readable name for the customer."""
        return self.name


class Order(models.Model):
    """Represents an order placed by a customer."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return product name and quantity."""
        return f"{self.product} (x{self.quantity})"


class Photo(models.Model):
    """Stores photos uploaded through the camera interface."""
    image = models.ImageField(upload_to='uploads/photos/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return an identifier for the photo with timestamp."""
        return f"Photo {self.id} - {self.uploaded_at:%Y-%m-%d %H:%M:%S}"

