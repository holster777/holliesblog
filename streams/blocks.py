from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructValue

class TitleAndTextBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True)
    text = blocks.TextBlock(required = True)
    
    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"
        

class RichTextBlock(blocks.RichTextBlock):
    
    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Full Rich Text"
        

class SimpleRichTextBlock(blocks.RichTextBlock):
    
    def __init__(self, required = True, editor = "default", features = None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
            
        ]
        
        
    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Simple Rich Text"
        
        
    
class PersonBlock(blocks.StructBlock):
        
    name = blocks.CharBlock(required = True)
    role = blocks.CharBlock(required = True)
    bio = blocks.CharBlock(required = True, max_length = 100)
    image = ImageChooserBlock(required = True)
    
    class Meta:
        template = "streams/person_block.html"
        icon = "user"
        label = "Person Block"
        form_classname = "Person Block"
       
       
class ButtonStructValue(StructValue):
        
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        return external_url or page.url      
    
     

class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(label="button text", required=True)
    page = blocks.PageChooserBlock(label="page", required=False)
    external_url = blocks.URLBlock(label="external URL", required=False)

    class Meta:
        template = "streams/button_block.html"
        icon = "link"
        label = "Button Block"
        value_class = ButtonStructValue
        


class BannerBlock(blocks.StructBlock):
    main_text = blocks.CharBlock(label="main text", required=True)
    subtitle = blocks.CharBlock(label="subtitle", required=True)
    image = ImageChooserBlock(required = True)
    button_text = blocks.CharBlock(label="button text", required=True)
    page = blocks.PageChooserBlock(label="page", required=False)
    external_url = blocks.URLBlock(label="external URL", required=False)
    
    class Meta:
        template = "streams/banner_block.html"
        icon = "edit"
        label = "Banner Block"
        value_class = ButtonStructValue


class SplitSection(blocks.StructBlock):
    header = blocks.CharBlock(label="header", required=True)
    body = blocks.CharBlock(label="body", required=True)
    image = ImageChooserBlock(required = True)
    image_side = blocks.ChoiceBlock(choices=[
    ('left', 'Left'),
    ('right', 'Right'),
], required = True)
    button_text = blocks.CharBlock(label="button text", required=True)
    page = blocks.PageChooserBlock(label="page", required=False)
    external_url = blocks.URLBlock(label="external URL", required=False)
        
    
    class Meta:
        template = "streams/split_section.html"
        icon = "edit"
        label = "Split Section"
        value_class = ButtonStructValue
    
