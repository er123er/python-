# Scrapy设置文件

BOT_NAME = "pet"  # 项目名称

SPIDER_MODULES = ["pet.spiders"]  # 爬虫模块
NEWSPIDER_MODULE = "pet.spiders"  # 新建爬虫模块

# 通过USER_AGENT识别爬虫
# USER_AGENT = "pet (+http://www.yourdomain.com)"

# 是否遵守robots.txt规则
ROBOTSTXT_OBEY = False

# 最大并发请求数
CONCURRENT_REQUESTS = 32

# 请求同一网站的延迟
DOWNLOAD_DELAY = 3
# 可以配置CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 是否启用cookies
# COOKIES_ENABLED = False

# 是否启用Telnet Console
# TELNETCONSOLE_ENABLED = False

# 默认请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

# 爬虫中间件
SPIDER_MIDDLEWARES = {
    "pet.middlewares.UAMiddleware": 543,  # 随机User-Agent
    "pet.middlewares.ProxyMiddleware": 542,  # 代理IP
}

# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    "pet.middlewares.UAMiddleware": 543,  # 随机User-Agent
    "pet.middlewares.ProxyMiddleware": 542,  # 代理IP
    # "pet.middlewares.PetDownloaderMiddleware": 543,
}

# Item Pipeline
ITEM_PIPELINES = {
    "pet.pipelines.MySQLPipeline": 300,  # 存储到MySQL数据库
}

# 是否启用AutoThrottle扩展
AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
AUTOTHROTTLE_START_DELAY = 5
# 最大下载延迟
AUTOTHROTTLE_MAX_DELAY = 60
# 平均每个远程服务器的并行请求数
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 是否显示每个响应接收到的节流统计信息
AUTOTHROTTLE_DEBUG = True

# 是否启用HTTP缓存
# HTTPCACHE_ENABLED = True
# 缓存过期时间
# HTTPCACHE_EXPIRATION_SECS = 0
# 缓存存储目录
# HTTPCACHE_DIR = "httpcache"
# 忽略的HTTP状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []
# 缓存存储后端
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 设置默认值为过时的设置
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# MYSQL数据库连接信息
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'web'

# 是否启用重定向
REDIRECT_ENABLED = True


CS_BACKEND = 'http://localhost:4520'
CS_API_TOKEN = '92d62d2c2640a364584308a924c32220003b472f'
EXTENSIONS = {
    'cs_sender.ScrapyMonitor': 500,
}