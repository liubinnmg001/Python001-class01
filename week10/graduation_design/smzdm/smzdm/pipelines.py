from itemadapter import ItemAdapter
import pymysql

# 爬取到的数据写入到MySQL数据库
class MySQLPipeline(object):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        sql = 'INSERT INTO mobile(name,input_time,comment,sentiments) VALUES(%s,%s,%s,%s)'
        values = (
            item['name'],
            item['input_time'],
            item['comment'],
            item['sentiments']
        )
        self.cursor.execute(sql, values)
        self.db.commit()
        return item