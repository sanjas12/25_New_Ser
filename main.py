import time
from urllib.request import urlopen

url = "https://www.rbc.ru/"

def get_title(url):
    
    page = urlopen(url)

    # print(page)

    html_byte = page.read()
    html = html_byte.decode("utf-8")

    # print(html)

    start_head = "<title>"
    end_head = "</title>"

    title_index = html.find(start_head)

    start_index = title_index + len(start_head)
    # print(start_index)

    end_index = html.find(end_head)
    # print(end_index)

    title = html[start_index:end_index]
    
    return title


if __name__ == "__main__":
    while True:
        title = get_title(url)
        print(title)
        time.sleep(1)
