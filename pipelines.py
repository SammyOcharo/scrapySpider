# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#scrapped data is stored on mysql
from itemadapter import ItemAdapter
import mysql.connector


class AvicommPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='sammysteve',
            database='mysql'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS avicomm_tb""")
        self.curr.execute("""create table avicomm_tb(
                              title text, 
                              amount numeric)""")
        self.curr.execute("""ALTER TABLE mysql.avicomm_tb MODIFY COLUMN title text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into avicomm_tb values(%s,%s)""", (
            item['title'][0],
            item['amount'][0:7]
        ))
        self.conn.commit()
