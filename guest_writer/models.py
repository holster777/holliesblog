from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.models import Page
from wagtail.core import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from blog.models import BlogPage


class FormField(AbstractFormField):
    page = ParentalKey('GuestWriter', on_delete=models.CASCADE, related_name='form_fields')


class GuestWriter(AbstractEmailForm):

    def featured_blogs(self):
        all_blogs = BlogPage.objects.all()
        max_display = 3
        featured_blogs = all_blogs.order_by('-date')[:max_display]
        return featured_blogs

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]