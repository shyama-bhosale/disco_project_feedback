from django.db import models


class Image(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name


class AccountPlan(models.Model):
    name = models.CharField(max_length=255)
    thumbnail_sizes = models.JSONField(default=[
        {"name": "thumbnail_1", "height": 200, "width": 200}
    ])
    link_to_original = models.BooleanField(default=False)
    generate_expiring_links = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ExpiringLink(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    expiry_time = models.DateTimeField()

class Membership(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    membership = models.ForeignKey('AccountPlan', on_delete=models.CASCADE)





