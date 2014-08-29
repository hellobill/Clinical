# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecordItem(scrapy.Item):
	record_id = scrapy.Field()
	url = scrapy.Field()

	# Tracking Information
	purpose = scrapy.Field()
	FRD = scrapy.Field()
	LUD = scrapy.Field()
	SD = scrapy.Field()
	EPCD1 = scrapy.Field()
	CPOM = scrapy.Field()
	OPOM = scrapy.Field()
	CH = scrapy.Field()
	CSOM = scrapy.Field()
	OSOM = scrapy.Field()
	COOM = scrapy.Field()
	OOOM = scrapy.Field()

	# Descriptive Information
	BT = scrapy.Field()
	OT = scrapy.Field()
	BS = scrapy.Field()
	DD = scrapy.Field()
	ST = scrapy.Field()
	SP = scrapy.Field()
	SDs = scrapy.Field()
	Co = scrapy.Field()
	Intv = scrapy.Field()
	SA = scrapy.Field()
	Pub = scrapy.Field()

	# Recruitment Information
	RS = scrapy.Field()
	EE = scrapy.Field()
	CD = scrapy.Field()
	EPCD2 = scrapy.Field()
	EC = scrapy.Field()
	Gend = scrapy.Field()
	Age = scrapy.Field()
	AHV = scrapy.Field()
	Cont = scrapy.Field()
	LC = scrapy.Field()

	# Administrative Information
	NCTN = scrapy.Field()
	OSID = scrapy.Field()
	HDMC = scrapy.Field()
	RP = scrapy.Field()
	SS = scrapy.Field()
	Coll = scrapy.Field()
	Inves = scrapy.Field()
	IPB = scrapy.Field()
	VD = scrapy.Field()

	pass

# class BasicItem(scrapy.Item):
# 	url = scrapy.Field()
# 	pass
class ClinicalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    condition = scrapy.Field()
    interventions = scrapy.Field()
    link = scrapy.Field()

    pass


class ShowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    pass