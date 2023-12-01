import time
from urllib.request import urlopen

class MyTitle():
    url = "https://www.rbc.ru/"
    start_title = "main__big__title"
    end_title = "</title>"
    file_name = ""

    def __init__(self):
        self.title = None

    def get_title(url):
        
        page = urlopen(url)

        # print(page)

        html_byte = page.read()
        html = html_byte.decode("utf-8")

        print(len(html))

        title_index = html.find(start_title)

        start_index = title_index + len(start_title)
        print(start_index)

        end_index = html.find(end_title)
        # print(end_index)

        title = html[start_index:]
        
        return title

    def write_to_file():
        pass

    def __str__(self) -> str:
         return f'{self.title}'


if __name__ == "__main__":
    title = MyTitle()
    while True:
        print(title)
        time.sleep(1)
