"""
Views for customer management and camera-based photo upload.
"""

import base64
import logging
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Customer, Photo
from .forms import PhotoForm

logger = logging.getLogger(__name__)


def customer_list(request):
    """Display a list of all customers."""
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})


def customer_detail(request, customer_id):
    """Display details and orders for a specific customer."""
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})


@require_http_methods(["GET"])
def camera_view(request):
    """Render the camera interface page."""
    return render(request, 'customers/camera.html')


@require_http_methods(["POST"])
def camera_upload(request):
    """
    Handle base64-encoded photo uploads via the camera interface.
    Expects a base64 string in POST data under the key 'photo'.
    """
    image_data = request.POST.get("photo")
    if not image_data:
        logger.warning("No image data received in camera upload request.")
        return JsonResponse({"success": False, "error": "No image data received."}, status=400)

    try:
        # Split and decode base64 image data
        format, imgstr = image_data.split(";base64,")
        ext = format.split("/")[-1]
        image_file = ContentFile(base64.b64decode(imgstr), name=f"upload.{ext}")

        # Save photo instance
        photo = Photo.objects.create(image=image_file)

        logger.info(f"Photo uploaded successfully: {photo.image.url}")
        return JsonResponse({
            "success": True,
            "message": "Photo uploaded successfully.",
            "image_url": photo.image.url,
            "id": photo.id,
        })

    except Exception as e:
        logger.error(f"Error during photo upload: {e}")
        return JsonResponse({"success": False, "error": str(e)}, status=400)

