from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page

from lenguapurhepecha.utils import TranslatedField


class ResourceIndexPage(Page):
    translated_title = TranslatedField(
        'title',
        'title_sp',
        'title_pua'
    )
    title_sp = models.CharField(max_length=255, blank=True)
    title_pua = models.CharField(max_length=255, blank=True)

    body = TranslatedField(
        'body_en',
        'body_sp',
        'body_pua',
    )
    body_en = RichTextField(blank=True)
    body_sp = RichTextField(blank=True)
    body_pua = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title_sp', classname="full"),
        FieldPanel('title_pua', classname="full"),
        FieldPanel('body_en', classname="full"),
        FieldPanel('body_sp', classname="full"),
        FieldPanel('body_pua', classname="full"),
    ]

    parent_page_types = ['home.HomePage']
