from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import uuid

class Disket(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, help_text=_("The title of the disket"))
    slug = models.SlugField(unique=True, blank=True, help_text=_("The slug of the disket"))
    tagline = models.CharField(max_length=160, help_text=_("Short description of the disket. Max 160 characters."))
    tags = models.CharField(max_length=255, help_text=_("The tags of the disket"))
    visibility = models.CharField(
        max_length=10, 
        choices=[('public', _('Public')), ('unlisted', _('Unlisted'))],
        help_text=_("The visibility of the disket")
    )
    aspect_ratio = models.CharField(
        max_length=5, 
        choices=[('1/1', _('1/1')), ('16/9', _('16/9')), ('9/16', _('9/16'))],
        help_text=_("The aspect ratio of the content.")
    )
    zip_file = models.FileField(upload_to='uploads/', help_text=_("The zip file of the disket"))
    created_at = models.DateTimeField(auto_now_add=True, help_text=_("The date and time the disket was created"))
    approved = models.BooleanField(default=False, help_text=_("Whether the disket has been approved"))
    content_path = models.CharField(max_length=255, blank=True, help_text=_("The path to the content of the disket"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{uuid.uuid4()}")
        super().save(*args, **kwargs) 