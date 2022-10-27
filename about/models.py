from django.db import models
from wagtail.core.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.core.fields import StreamField

from streams import blocks

class About(Page):

    introduction = models.CharField(max_length=500, null = True, blank = True)

    content = StreamField([
        ("person_block", blocks.PersonBlock()),
        ], null = True, blank = True, use_json_field = True)
    
    content_panels = Page.content_panels + [
        
        FieldPanel("introduction"),
        FieldPanel("content"),
    ]

