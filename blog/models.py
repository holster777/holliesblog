from django.db import models
from django.contrib import messages
from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.models import User

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page, Orderable
from wagtail.core import blocks
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet



class BlogIndexPage(RoutablePageMixin, Page):

    subpage_types = ["BlogPage"]

    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context["posts"] = (
            BlogPage.objects.descendant_of(self).live().order_by("date")
        )
        return context

    @route(r"^tags/$", name="tag_archive")
    @route(r"^tags/([\w-]+)/$", name="tag_archive")
    def tag_archive(self, request, tag=None):

        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no blog posts tagged with "{}"'.format(tag)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        posts = self.get_posts(tag=tag)
        context = {"tag": tag, "posts": posts}
        return render(request, "blog/blog_index_page.html", context)

    def get_posts(self, tag=None):
        posts = BlogPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts


    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags
    
    class Meta:
        verbose_name = 'Blog'


class BlogPageTag(TaggedItemBase):

    content_object = ParentalKey(
        "BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )



class BlogAuthorsOrderable(Orderable):
    """Allows us to select one or more blog authors from snippets"""
    page = ParentalKey("blog.BlogPage", related_name="blog_authors" )
    author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel("author")
    ]

class BlogAuthor(models.Model):
    """Blog author for snippets"""

    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    website =models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null = True,
        blank = False,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("image"),
                FieldPanel("bio")
            ],
            heading = "Author Information",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ],
            heading = "Links"
        )
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)

class BlogPage(Page):

    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = '+'
    )
     

    date = models.DateField("Post date")
    excerpt = models.CharField(max_length = 250, null = True, blank = True)
    # categories = ParentalManyToManyField("blog.BlogCategory", blank = True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    blog_post = StreamField([
        ('heading', blocks.CharBlock()),
        ('content', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], null = True, blank = True, use_json_field = True)


    content_panels = Page.content_panels + [
        FieldPanel('featured_image'),
        FieldPanel('date'),
        MultiFieldPanel([
            InlinePanel("blog_authors", label = "Author", min_num = 1, max_num = 3)
        ],
        heading = "Author(s)"
        ),
        FieldPanel("tags"),
        FieldPanel('excerpt'),
        FieldPanel('blog_post'),

    ]

    @property
    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = "/" + "/".join(
                s.strip("/") for s in [self.get_parent().url, "tags", tag.slug]
            )
        return tags

    parent_page_types = ["BlogIndexPage"]
    subpage_types = []
    
    @property
    def next_post(self):
        return self.get_next_siblings().type(self.__class__).live().first()

    @property
    def prev_post(self):
        return self.get_prev_siblings().type(self.__class__).live().first()
    



   
    
    