# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from main.models import Fire, FireType
from random import randint
import csv

#logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        from random import randint
        Fire.objects.all().delete()
        FireType.objects.all().delete()
        print 'start'
        ft1 = FireType()
        ft1.name = 'Неопределено'
        ft1.save()
        ft = FireType()
        ft.name = 'Низкая'
        ft.rule = '1&2'
        ft.save()
        ft = FireType()
        ft.name = 'Средняя'
        ft.rule = '1&2&3'
        ft.save()
        ft = FireType()
        ft.name = 'Высокая'
        ft.rule = '1&2&3&4'
        ft.save()
        ft = FireType()
        ft.name = 'Критическая'
        ft.rule = '1&2&3&4&5'
        ft.save()

        for i in range(10):
            f = Fire()
            f.type = ft1
            f.l_people_day = randint(0,1)
            f.l_people_machine = randint(0,1)
            f.l_people_other = randint(0,1) 
            f.m_people_day = randint(0,1)
            f.m_people_machine = randint(0,1)
            f.m_people_other = randint(0,1)
            f.d_people_day = randint(0,1)
            f.d_people_machine = randint(0,1)
            f.d_people_other = randint(0,1)
            f.save()
            print 'process.....%s' % i
        print 'done'



       
