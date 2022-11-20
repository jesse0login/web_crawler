import re

import requests
from bs4 import BeautifulSoup


def get_novel_chapters():
    root_url = "https://www.hetushu.com/book/3631/index.html"
    r = requests.get(root_url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue
        href = link['href']
        pattern = '^/book/3631/\d+.html$'
        if re.match(pattern, href):
            data.append(("https://www.hetushu.com/%s" % link['href'], link.get_text()))

    return data


def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find("div", id='content').get_text()

novel_chapters = get_novel_chapters()
total_cnt = len(novel_chapters)
idx = 0
for chapter in get_novel_chapters():
    idx += 1
    print(idx,total_cnt)
    url, title = chapter
    with open("%s.txt" % title, "w") as fout:
        fout.write(get_chapter_content(url))
        fout.flush()
    if idx == 5:#只爬前5章
        break
