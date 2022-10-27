from django.db import models

from wagtail.models import Page
from wagtail.core import blocks
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from blog.models import BlogPage


class HomePage(Page):

    hero_banner = StreamField([
        ('subheading', blocks.CharBlock()),
        ('content', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ], null = True, blank = True, use_json_field = True)

    featured_blogs_title = models.CharField(max_length=100, null = True, blank = True)

    def featured_blogs(self):
        all_blogs = BlogPage.objects.all()
        max_display = 3
        featured_blogs = all_blogs.order_by('-date')[:max_display]
        return featured_blogs

    content_panels = Page.content_panels + [
       FieldPanel('hero_banner'),
        FieldPanel('featured_blogs_title')
    ]



