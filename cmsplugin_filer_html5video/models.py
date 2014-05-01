# -*- coding: utf-8 -*-

from cms.models import CMSPlugin
from cmsplugin_filer_html5video import plugin_settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

class FilerHTML5Video(CMSPlugin):
    # player settings
    
    title = models.CharField(_('title'), blank=True, default='', max_length=100)
    
    video_mp4  = FilerFileField(verbose_name=_('movie file (MP4[H.264)'), help_text=_('MP4 encoded video file (Android3+, Chrome3+, Firefox26+, IE9+, iOS3+, Safari3.1+)'), blank=True, null=True, related_name='+')
    video_webm = FilerFileField(verbose_name=_('movie file (webM[VP8])'), help_text=_('webM encoded video file (Android2.3+, Chrome6+, Firefox3.5+, Opera 10.60+)'), blank=True, null=True, related_name='+')
    video_ogv = FilerFileField(verbose_name=_('movie file (ogv[Theora])'), help_text=_('ogv encoded video file (Android2.3+, Chrome3+, Firefox4+, Opera 10.50+ )'), blank=True, null=True, related_name='+')
    image = FilerImageField(verbose_name=_('image'), help_text=_('preview image file'), null=True, blank=True, related_name='+')

    width = models.PositiveSmallIntegerField(_('width'), default=plugin_settings.VIDEO_WIDTH)
    height = models.PositiveSmallIntegerField(_('height'), default=plugin_settings.VIDEO_HEIGHT)

    auto_play = models.BooleanField(_('auto play'), default=plugin_settings.VIDEO_AUTOPLAY)
    auto_hide = models.BooleanField(_('auto hide'), default=plugin_settings.VIDEO_AUTOHIDE)
    fullscreen = models.BooleanField(_('fullscreen'), default=plugin_settings.VIDEO_FULLSCREEN)
    loop = models.BooleanField(_('loop'), default=plugin_settings.VIDEO_LOOP)


    def __unicode__(self):
        return u"%s" % self.title

    def get_height(self):
        return "%s" % self.height

    def get_width(self):
        return "%s" % self.width

