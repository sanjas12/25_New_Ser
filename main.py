import logging
# import pprint
import re
import sys
import time
from urllib.request import urlopen
from config.config import *



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
    # pattern = '<class="main__big__title".*?>.*?<\/span>'

    def __init__(self):
        self.url = "https://www.rbc.ru/"
        self.title = None
        self.dict_news = dict()
        self.read_old_news()

    def get_title(self):
        
        page = urlopen(self.url)

        html_byte = page.read()
        html = html_byte.decode("utf-8")

        # print(html)

        #TODO переписать на re
        #TODO переписать на beateful soap
        css_class_index = html.find(__class__.name_css_class)
        start_title_index = css_class_index + len(__class__.start_title)
        end_title_index = html.find(__class__.end_title)
        self.title = html[start_title_index:end_title_index]
        _del = '-->'
        self.title = self.title.split(_del)[1]

        # raw_pattern = r'<class="main__big__title".*?>.*?<\/span>'
        # pattern = re.compile(raw_pattern)
        # for l, n in re.findall(pattern, raw_title):
        #     print(f"{l} -> {n}")

        # match_results = re.search(pattern, raw_title, re.IGNORECASE)
        # self.title = match_results.group()
        # self.title = re.sub("", "", self.title)
        # print(f'{time.ctime}->{self.title}')

        return self.title

    def read_old_news(self):
        #TODO add exist file.
        with open(OUT_FILE, '+r', encoding="UTF-8") as f:
            for line  in f.readlines():
                time, title, _ = line.split(';')
                if title not in self.dict_news:
                    self.dict_news[title] = time
        # pprint.pprint(self.dict_news)

    def write_to_log_file(self):
        print(f'{time.ctime()} -> {self.title}')
        logging.info(f"{self.title}")

    def add_to_base(self):
        if self.title not in self.dict_news:
            self.dict_news[self.title] = time.ctime
            title = ';'.join((time.ctime(), self.title, '\n'))
            with open(OUT_FILE, '+a', encoding="UTF-8") as f:
                f.write(title)
        else:
            logging.info(f"{self.title} already exist")
    
    def __str__(self) -> str:
         return f'{time.ctime()} -> {self.title}'


if __name__ == "__main__":
    title = MyTitle()
    while True:
        title.get_title()
        title.write_to_log_file()
        title.add_to_base()
        time.sleep(TIMEOUT)

