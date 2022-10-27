from django import template
from ..models import Menu

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    
    if slug == 'footer':
       footer = Menu.objects.get(slug=slug)
    
       footer_items = footer.menu_items.all()
    
       length = len(footer_items)
       middle_index = length//2
       
       footer_left = footer_items[:middle_index]
       footer_right = footer_items[middle_index:]
       
       return footer_left, footer_right
    
    else:
        
        return Menu.objects.get(slug=slug)

    
    
    