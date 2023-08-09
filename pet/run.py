from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import cmdline


def run_2():
    cmdline.execute(["scrapy", "crawl", "bedrijvenpagina"])


def run_1():
    process = CrawlerProcess(get_project_settings())
    process.crawl('bedrijvenpagina')
    process.crawl('local')
    process.crawl('dasoertliche')
    process.start()


if __name__ == '__main__':
    # run_2()
    run_1()
