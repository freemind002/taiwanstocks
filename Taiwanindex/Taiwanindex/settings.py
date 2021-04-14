# -*- coding: utf-8 -*-

# Scrapy settings for Taiwanindex project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent

ua = UserAgent()

# 項目名稱
BOT_NAME = 'Taiwanindex'

# 爬蟲程序的位置
SPIDER_MODULES = ['Taiwanindex.spiders']
NEWSPIDER_MODULE = 'Taiwanindex.spiders'

SPLASH_URL = "http://192.168.99.100:8050/"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Taiwanindex (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 是否遵守robots協議，該為False
ROBOTSTXT_OBEY = False

# 最大并發量，默認為16個
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下載延遲時間為3秒
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 請求報頭
DEFAULT_REQUEST_HEADERS = {
  'User-Agent':ua.random,
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 蜘蛛中間件
SPIDER_MIDDLEWARES = {
   'Taiwanindex.middlewares.TaiwanindexSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 下載器中間件
DOWNLOADER_MIDDLEWARES = {
   'Taiwanindex.middlewares.TaiwanindexDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 管道文件
ITEM_PIPELINES = {
   # 'Taiwanindex.pipelines.MYSQLPipeline': 300,
   'Taiwanindex.pipelines.CSVPipeline': 400,
   # 'Taiwanindex.pipelines.MONGOPipeline': 500,
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
