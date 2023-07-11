import os


BOT_NAME = 'wikipedia'

SPIDER_MODULES = ['wikipedia.spiders']
NEWSPIDER_MODULE = 'wikipedia.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}

# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {}

LOG_LEVEL = 'INFO'

DOWNLOADER_MIDDLEWARES = {'scrapy.downloadermiddlewares.retry.RetryMiddleware': 610}
RETRY_ENABLED = True
RETRY_TIMES = 100
RETRY_HTTP_CODES = [503]

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1000
CONCURRENT_REQUESTS_PER_DOMAIN = 1000
LOGSTATS_INTERVAL = 10

DOWNLOAD_HANDLERS = {
    'http': 'scrapy_cloud_browser.CloudBrowserHandler',
    'https': 'scrapy_cloud_browser.CloudBrowserHandler',
}
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

CLOUD_BROWSER = {
    'API_HOST': os.getenv('CLOUD_API_HOST'),
    'API_TOKEN': os.getenv('CLOUD_API_TOKEN'),
    'NUM_BROWSERS': 1,
    'PAGES_PER_BROWSER': 100,
    'INIT_HANDLER': os.getenv('INIT_HANDLER'),
    'START_SEMAPHORES': 30,
    'PROXY_ORDERING': 'random',  # random, round-robin
    'PROXIES': [os.getenv('CLOUD_PROXY')],
}
