# -*- coding: utf-8 -*-

# Scrapy settings for Clinical project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Clinical'

SPIDER_MODULES = ['Clinical.spiders']
NEWSPIDER_MODULE = 'Clinical.spiders'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# LOG_FILE = "log/scrapy.log"

ITEM_PIPELINES = {
    'Clinical.pipelines.ClinicalPipeline': 300,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Clinical (+http://www.yourdomain.com)'
