from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext as _
import uuid


class Shelf(models.TextChoices):
    games = "games", _("games")
    apps = "apps", _("apps")
    tools = "tools", _("tools")
    time_wasters = "time_wasters", _("time wasters")
    demos = "demos", _("demos")
    other = "other", _("other")


class Visibility(models.TextChoices):
    public = "public", _("public")
    unlisted = "unlisted", _("unlisted")


class Agreement(models.TextChoices):
    agree = "agree", _("agree")
    disagree = "disagree", _("disagree")


class Disket(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Author")
    )
    label = models.CharField(
        max_length=255,
        help_text=_("The title of the disket"),
        verbose_name=_("Label"),
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        help_text=_("The slug of the disket"),
        verbose_name=_("Slug"),
    )
    tagline = models.CharField(
        max_length=160,
        help_text=_("Short description of the disket. Max 160 characters."),
        verbose_name=_("Tagline"),
    )
    shelf = models.CharField(
        max_length=255,
        choices=Shelf.choices,
        help_text=_("The shelf of the disket"),
        verbose_name=_("Shelf"),
    )
    visibility = models.CharField(
        max_length=10,
        choices=Visibility.choices,
        help_text=_("The visibility of the disket"),
        verbose_name=_("Visibility"),
    )
    zip_file = models.FileField(
        upload_to="uploads/",
        help_text=_("The zip file of the disket"),
        verbose_name=_("Zip File"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The date and time the disket was created"),
        verbose_name=_("Created At"),
    )
    approved = models.BooleanField(
        default=False,
        help_text=_("Whether the disket has been approved"),
        verbose_name=_("Approved"),
    )
    content_path = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("The path to the content of the disket"),
        verbose_name=_("Content Path"),
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.label}-{uuid.uuid4()}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Disket")
        verbose_name_plural = _("Diskets")
        ordering = ["-created_at"]


class DisketVersion(models.Model):
    disket = models.ForeignKey(
        Disket, on_delete=models.CASCADE, verbose_name=_("Disket")
    )
    log = models.CharField(
        max_length=255,
        help_text=_("The log of the disket version"),
        null=True,
        blank=True,
        verbose_name=_("Log"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The date and time the disket version was created"),
        verbose_name=_("Created At"),
    )

    def __str__(self):
        return f"{self.disket.label} - {self.created_at}"

    class Meta:
        verbose_name = _("Disket Version")
        verbose_name_plural = _("Disket Versions")
        ordering = ["-created_at"]
