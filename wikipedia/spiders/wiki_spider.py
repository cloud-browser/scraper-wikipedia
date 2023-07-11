# -*- coding: utf-8 -*-
import logging

import scrapy
from faker import Faker

fake = Faker()


log = logging.getLogger(__name__)


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    base_url = 'https://en.wikipedia.org'

    allowed_domains = ['wikipedia.org']

    custom_settings = {
        'FEEDS': {
            'data/%(name)s_%(time)s.csv': {
                'format': 'csv',
            }
        }
    }

    def start_requests(self):
        keyword_list = [fake.name() for _ in range(100_000)]

        for keyword in keyword_list:
            search_url = f'https://en.wikipedia.org/wiki/{keyword}'
            yield scrapy.Request(
                url=search_url,
                callback=self.parse_search_results,
                meta={'keyword': keyword},
            )

    def parse_search_results(self, response):
        for link in response.xpath('//div/p/a'):
            log.info(f'Search result: {link=}')
            yield {'link': self.base_url + link.xpath('.//@href').get()}
