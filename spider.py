#!/usr/bin/env python
import requests
import re
import urlparse

target_url = "https://www.megabank.com.tw/"
target_links = []


def extract_links_from(target_url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    href_links = extract_links_from(url)

    for link in href_links:
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#")[0]

        # exclude all other domains link
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)