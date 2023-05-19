import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from image_app.models import Image
import os
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image as PIL_Image

def generate_thumbnail_task(pk: str):
    instance = Image.objects.get(id=pk)
    filename, ext = os.path.splitext(os.path.basename(instance.image.name))
    image_name = filename.split("/")[-1]

    account_tier = instance.user.account_tier
    thumbnail_sizes = account_tier.get_thumbnail_sizes

    
    for size in thumbnail_sizes:
        img_file = BytesIO(instance.image.read())
        original_image = PIL_Image.open(img_file)

        # Resize the image
        thumbnail = original_image.resize((size.width, size.height), PIL_Image.ANTIALIAS)

        # Save the resized image to the path
        thumb_io = BytesIO()

        thumbnail.save(thumb_io, format="JPEG" if ext.lower() == ".jpg" else "PNG")
        thumbnail_path = f"{image_name}_{size.height}{ext.lower()}"

        thumbnail_file = SimpleUploadedFile(
            thumbnail_path, thumb_io.getvalue(), content_type="image/jpeg" if ext.lower() == ".jpg" else "image/png"
        )
        instance.image.save(thumbnail_path, thumbnail_file, save=False)


@receiver(post_save, sender=Image)
def create_thumbnails(sender, instance: Image, **kwargs):
    generate_thumbnail_task.delay(instance.id)
