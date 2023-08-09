import mysql.connector

class MySQLPipeline:
    def __init__(self, host, port, user, passwd, database):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE')
        )

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        # 插入数据
        sql = "INSERT INTO `pet_2` (`url_id`, `title`, `postcode`, `city`, `streetLine`, `source`, `coordinates`, `en_neme`, `typename`, `platform`, `url`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # sql = "INSERT INTO `pa_copy1_copy1` (`url_id`, `title`, `postcode`, `city`, `streetLine`, `source`, `coordinates`, `en_neme`, `typename`, `platform`, `url`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            item['url_id'],
            item['title'],
            item['postcode'],
            item['city'],
            item['streetLine'],
            item['source'],
            item['coordinates'],
            item['en_neme'],
            item['typename'],
            item['platform'],
            item['url']
        )
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item
