from urllib.request import urlopen

url = "https://www.rbc.ru/"

page = urlopen(url)

# print(page)

html_byte = page.read()
html = html_byte.decode("utf-8")

print(html)

start_head = "<title>"
end_head = "</title>"

title_index = html.find(start_head)

start_index = title_index + len(start_head)
# print(start_index)

end_index = html.find(end_head)
# print(end_index)

title = html[start_index:end_index]
# print(title)




