#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


from django.core.management.base import BaseCommand
import xlrd
from finder.models import Storage, Platform, Category, Domain


class Command(BaseCommand):

    def handle(self, *args, **options):

        # book = xlrd.open_workbook("software.xlsx")
        # sh = book.sheet_by_index(1)

        # for rx in range(1, sh.nrows):

        #     category = None
        #     platform = None
        #     domain = None

        #     row = sh.row(rx)

        #     name = row[1].value
        #     name = name.strip()
        #     if len(name) == 0:
        #         continue

        #     software, created = Software.objects.get_or_create(name=name)
        #     software.categories.clear()
        #     software.platforms.clear()
        #     software.domain.clear()

        #     cats = row[18].value
        #     cats = cats.split(',')

        #     for c in cats:
        #         c = c.strip()
        #         if len(c) > 0:
        #             category, created = Category.objects.get_or_create(name=c)
        #             software.categories.add(category)

        #     platforms = row[19].value
        #     platforms = platforms.split(',')
        #     for p in platforms:
        #         p = p.strip()
        #         if len(p) > 0:
        #             platform, created = Platform.objects.get_or_create(name=p)
        #             software.platforms.add(platform)

        #     domain = row[2].value
        #     domain = domain.split(',')
        #     for p in domain:
        #         p = p.strip()
        #         if len(p) > 0:
        #             domain, created = Domain.objects.get_or_create(name=p)
        #             software.domain.add(domain)




        #     software.description = row[10].value

        #     software.functionality = row[16].value
        #     software.help = row[20].value
        #     software.terms = row[22].value
        #     software.cost = row[21].value

        #     software.support = row[14].value

        #     software.save()

        #     #  print(sh.row(rx)[1], sh.row(rx)[10], sh.row(rx)[18])






        # # url = 'https://sharepoint.tudelft.nl'
        # # account = 'dastud\_sa-SPwsict'
        # # password = 'NWyreispQ5KF'


        # # auth = HttpNtlmAuth(account, password)
        # # site = Site('https://sharepoint.tudelft.nl/sites/ssc-ict/', auth=auth)


        # # #for s in site.get_list_collection():
        # # #    print(s)

        # # sp_list = site.List('Application catalog')
        # # data = sp_list.GetListItems('All Items')
        # # for d in data:

        # #     title = d['Title']
        # #     print('--------------------------', title)
        # #     print(d)

        # #     software, created = Software.objects.get_or_create(sharepoint_id=d['ID'])

        # #     software.name = title
        # #     if 'Omschrijving' in d:
        # #         software.description = d['Omschrijving']
        # #         software.details = d['Omschrijving']
        # #     software.save()



