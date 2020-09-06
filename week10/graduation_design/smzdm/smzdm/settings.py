# Scrapy settings for smzdm project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'smzdm'

SPIDER_MODULES = ['smzdm.spiders']
NEWSPIDER_MODULE = 'smzdm.spiders'

MYSQL_HOST = '39.96.82.178'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'mobile'
MYSQL_USER = 'liubin'
MYSQL_PASSWORD = 'zefmnemoy90hw45ks'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'smzdm (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '__ckguid=7TS4Ra5hgabrBcQyg7XraC5; __jsluid_s=577f1462ca911599ce4b238594af707f; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221745bf2970513-05409e90fd452a-5e1a3f18-2073600-1745bf2970655a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221745bf2970513-05409e90fd452a-5e1a3f18-2073600-1745bf2970655a%22%7D; device_id=3732941174159927046659725527297530d56dda1edb8dc91a0a35d3d0; _ga=GA1.2.736567007.1599270460; _gid=GA1.2.1104455319.1599270460; zdm_qd=%7B%7D; smzdm_ec=06; smzdm_ea=200; sess=ZjYyNjF8MTYwNDQ1NTc5NXw3MjIxNTg4ODAzfDU1YTZiYjM0YzJiMmJlOGY4MTI0NmY1ZTFiNjAyZWE1; user=user%3A7221588803%7C7221588803; smzdm_id=7221588803; userId=user:7221588803|7221588803; smzdm_user_source=56E5D21F787C87E83F3235DBC7ADA971; __gads=ID=b9360686233e3708:T=1599283536:S=ALNI_MYVlRan6DNUjlfaJjlvHQSw6hcQ6Q; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1599270459,1599311022; wt3_sid=%3B999768690672041; amvid=6d27d7a05967d46e1416aa69d0270a53; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1599321103; wt3_eid=%3B999768690672041%7C2159927527500042459%232159932110300160861; _gat_UA-27058866-1=1',
    'Host': 'www.smzdm.com',
    'Referer': 'https://www.smzdm.com/fenlei/zhinengshouji/',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
CONCURRENT_REQUESTS = 16
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'smzdm.middlewares.SmzdmSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'smzdm.middlewares.SmzdmDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {
    'smzdm.pipelines.MySQLPipeline': 401,
}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'smzdm.pipelines.SmzdmPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
