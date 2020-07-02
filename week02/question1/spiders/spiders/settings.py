# Scrapy settings for spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiders'

SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'

MYSQL_HOST = '39.96.82.178'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'maoyan'
MYSQL_USER = 'liubin'
MYSQL_PASSWORD = 'zefmnemoy90hw45ks'

# Crawl responsibly by identifying yourself (and your website) on the user-agent

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'uuid_n_v=v1; uuid=EEFD7050BC4A11EAB9132154AFB3FD94AD60857BA2D24DFFB4B3CB469FDFDE74; _lxsdk_cuid=1730ef8eefcc8-068620b6a9df66-3e3e5e0e-1fa400-1730ef8eefcc8; _lxsdk=EEFD7050BC4A11EAB9132154AFB3FD94AD60857BA2D24DFFB4B3CB469FDFDE74; mojo-uuid=5bd8c412aa5ed9c2bf3c894ea6f7fa1c; _csrf=16f9ad94fc45864d9f654e8d09f04b49f6bc1bf985fc4c32539ee6994e339c07; mojo-session-id={"id":"60108c5c644c378bb4f47e7dc0c92acc","time":1593693346363}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593684062,1593693346; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593693352; mojo-trace-id=2; __mta=188637079.1593684066759.1593693346430.1593693352541.4; _lxsdk_s=1730f869a57-d76-3d6-391%7C%7C4',
    'Host': 'maoyan.com',
    'Referer': 'https://maoyan.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spiders.middlewares.SpidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'spiders.middlewares.SpidersDownloaderMiddleware': 543,
    'spiders.middlewares.RandomHttpProxyMiddleware': 400,
}
HTTP_PROXY_LIST = [
    'https://54.241.121.74:3128',
    'https://52.179.18.244:8080',
    'https://51.91.212.159:3128',
    'https://178.63.41.235:9999'
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'spiders.pipelines.MySQLPipeline': 401,
}
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
