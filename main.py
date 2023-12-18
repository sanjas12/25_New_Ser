import logging
import os
import pprint
import re
import sys
import time
from urllib.request import urlopen
from config.config import *
from orm import Title, DbSession

if sys.version_info[1]>=9:
    logging.basicConfig(filename=LOG_FILE, encoding='utf-8', level=logging.INFO, format=FORMAT)
else:
    logging.basicConfig(handlers=[logging.FileHandler(filename=LOG_FILE, encoding='utf-8', mode='a')],
                        format=FORMAT, level=logging.INFO)


class MyTitle():
    name_css_class = "main__big__title"
    start_title = '<span class="main__big__title" data-vr-headline>'
    end_title = """<!--
         --></span><!"""
    file_name = ""
    encoding = "UTF-8"
    # pattern = '<class="main__big__title".*?>.*?<\/span>'

    def __init__(self):
        self.title, self.content, self.timestamp  = (None for _ in range(3))
        self.title_message, self.current_title = ('' for _ in range(2))
        self.dict_title = dict()
        self.url = "https://www.rbc.ru/"
        self.orm_base_news = Title()
        self.read_local_base()

    def get_title_content(self) -> tuple:
        page = urlopen(self.url)

        html_byte = page.read()
        html = html_byte.decode("utf-8")

        #TODO переписать на re
        #TODO переписать на beateful soap
        css_class_index = html.find(__class__.name_css_class)
        start_title_index = css_class_index + len(__class__.start_title)
        end_title_index = html.find(__class__.end_title)
        self.title = html[start_title_index:end_title_index]
        _del = '-->'
        self.title = self.title.split(_del)[1]
        self.timestamp = time.ctime()
        self.content = 'test'
        # self.dict_title[self.title] = self.timestamp

        # raw_pattern = r'<class="main__big__title".*?>.*?<\/span>'
        # pattern = re.compile(raw_pattern)
        # for l, n in re.findall(pattern, raw_title):
        #     print(f"{l} -> {n}")

        # match_results = re.search(pattern, raw_title, re.IGNORECASE)
        # self.title = match_results.group()
        # self.title = re.sub("", "", self.title)
        
        self.current_title = f"{self.title}->{self.timestamp}"
        self.log_message('get title, content, timestamp')
        if self.title not in self.dict_title:
            self.add_to_local_base()
            self.add_to_database()
        else:
            self.log_message('already exist in local base and database')
        return self.title, self.content, self.timestamp 
        
    def log_message(self, end_text:str="")-> None:
        log_message = self.current_title + '->' + end_text
        print(log_message)
        logging.info(log_message)

    def read_local_base(self):
        if not os.path.exists(LOCAL_BASE_FILE):
            with open(LOCAL_BASE_FILE, 'w+', encoding=__class__.encoding):
                pass
        #TODO add exist file.
        with open(LOCAL_BASE_FILE, '+r', encoding=__class__.encoding) as f:
            for line  in f.readlines():
                time, title, _ = line.split(';')
                if title not in self.dict_title:
                    self.dict_title[title] = time
        # pprint.pprint(self.dict_title)
        # for k,v in self.dict_title:
        #     self.add_to_database()
        self.log_message('read local base (old news)')

    def add_to_local_base(self):
        self.dict_title[self.title] = self.timestamp
        title = ';'.join((self.timestamp, self.title, '\n'))
        print('add_title', title)
        with open(LOCAL_BASE_FILE, '+a', encoding=__class__.encoding) as f:
            f.write(title) 
        self.log_message('add in local base')
    
    def add_to_database(self):
        with DbSession() as db_seccion:
            news_entry = Title(title=self.title,
                        content='Example Content',
                        timestamp=self.timestamp)
            db_seccion.add(news_entry)
        self.log_message('add to database')

    def __str__(self) -> str:
         return f'{self.title} -> {self.content} -> {self.timestamp}'

    def my_decorator(self, func):
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result
        return wrapper

    @property
    def get_dict_title(self):
        #  pprint.pprint(self.dict_title)
        for k, v in self.dict_title.items():
            print(f'{time.ctime()} local base-> {k} {v}')

    @property
    def get_title(self):
         self.log_message()
         print('get-title', self.title_message)


if __name__ == "__main__":
    title = MyTitle()
    while True:
        title.get_title_content()
        # title.add_to_database()
        title.get_dict_title
        time.sleep(TIMEOUT)
        