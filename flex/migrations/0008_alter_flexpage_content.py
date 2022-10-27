# Generated by Django 4.1.2 on 2022-10-24 15:45

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0007_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True))])), ('full_rich_text', streams.blocks.RichTextBlock()), ('simple_rich_text', streams.blocks.SimpleRichTextBlock()), ('button_block', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='button text', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='page', required=False)), ('external_url', wagtail.blocks.URLBlock(label='external URL', required=False))])), ('banner_block', wagtail.blocks.StructBlock([('main_text', wagtail.blocks.CharBlock(label='main text', required=True)), ('subtitle', wagtail.blocks.CharBlock(label='subtitle', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('button_text', wagtail.blocks.CharBlock(label='main text', required=True)), ('page', wagtail.blocks.PageChooserBlock(label='page', required=False)), ('external_url', wagtail.blocks.URLBlock(label='external URL', required=False))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
