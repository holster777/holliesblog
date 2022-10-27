from django.db import models
from wagtail.core.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.core.fields import StreamField

from streams import blocks

class FlexPage(Page):
    
    
    subtitle = models.CharField(max_length = 100, blank = True, null = True)
    
    content = StreamField([
        
        ("title_and_text", blocks.TitleAndTextBlock()),
        ("full_rich_text", blocks.RichTextBlock()),
        ("simple_rich_text", blocks.SimpleRichTextBlock()),
        ("button_block", blocks.ButtonBlock()),
        ("banner_block", blocks.BannerBlock()),
        ("split_section", blocks.SplitSection()),
    
    ], null = True, blank = True, use_json_field = True)
    
    content_panels = Page.content_panels + [
        
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
    