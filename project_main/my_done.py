"""
网易云基础爬虫（学习版）
功能：爬取网易云音乐排行榜页面 HTML 内容
作者：Astro
时间：2026.04
"""

import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin, urlparse
import json

class NeteaseMusicCrawler:
    """Netease music crawler (learning version)."""

    def __init__(self):
        self.session = requests.Session()
        # Ignore system proxy env vars (HTTP_PROXY/HTTPS_PROXY).
        self.session.trust_env = False
        # Use local proxy on port 7897.
        self.session.proxies.update(
            {
                "http": "http://127.0.0.1:7897",
                "https": "http://127.0.0.1:7897",
            }
        )
        self.base_url = "https://music.163.com/"

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        self.session.headers.update(self.headers)

    def get_page(self, url, params=None, retries=5):
        for attempt in range(retries):
            try:
                response = self.session.get(url, params=params, timeout=10)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"请求失败（尝试 {attempt + 1}/{retries}），错误反馈：{e}")
                if attempt < retries - 1:
                    time.sleep(random.uniform(1, 3))
                else:
                    raise

    def crawl_toplist(self):
        try:
            url = "https://music.163.com/discover/toplist"
            print(f"正在爬取排行榜页面：{url}")

            response = self.get_page(url)
            if response.status_code == 200:
                response.encoding = "utf-8"
                print(f"成功获取页面，状态码：{response.status_code}")
                print(f"页面大小：{len(response.text)} 字符")
                return response.text

            print(f"页面请求失败，状态码：{response.status_code}")
            return None
        except Exception as e:
            print(f"爬取失败，错误信息：{e}")
            return None

    def save_html(self, html_content, filename):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"HTML内容已经保存到：{filename}")
        except Exception as e:
            print(f"HTML内容保存失败：{e}")


if __name__ == "__main__":
    crawler = NeteaseMusicCrawler()
    html_content = crawler.crawl_toplist()
    if html_content:
        crawler.save_html(html_content, "wuhuohao.html")
        print("爬取成功")
    else:
        print("爬取失败")

