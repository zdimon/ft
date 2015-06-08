# -*- coding: utf-8 -*-
from django.db import models

class FireType(models.Model):
    name = models.CharField(max_length=250, blank=True, verbose_name=u'Название')
    rule = models.CharField(max_length=250, blank=True, verbose_name=u'Правило')
    def __unicode__(self):
        return self.name


class Fire(models.Model):
    l_people_day = models.IntegerField(u'Лесхоз (человекодни)', null=True, blank=True)
    l_people_machine = models.IntegerField(u'Лесхоз (машиносмены)', null=True, blank=True)
    l_people_other = models.IntegerField(u'Лесхоз (другая техника)', null=True, blank=True)
    m_people_day = models.IntegerField(u'МЧС (человекодни)', null=True, blank=True)
    m_people_machine = models.IntegerField(u'МЧС (машиносмены)', null=True, blank=True)
    m_people_other = models.IntegerField(u'МЧС (другая техника)', null=True, blank=True)
    d_people_day = models.IntegerField(u'Другие организации (человекодни)', null=True, blank=True)
    d_people_machine = models.IntegerField(u'Другие организации (машиносмены)', null=True, blank=True)
    d_people_other = models.IntegerField(u'Другие организации (другая техника)', null=True, blank=True)
    type = models.ForeignKey(FireType, null=True, blank=True)





