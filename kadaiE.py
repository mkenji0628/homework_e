import time
import requests


def info_top():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'  # New, Top and Best Stories
    news = requests.get(url)
    title = news.json()
    for i in title:
        try:
            news2 = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty').json()
            print('{ title:' + news2['title'], ', Link:' + news2['url'], '}')
            time.sleep(1)
        except KeyError:
            pass


def main():
    info_top()


if __name__ == '__main__':
    main()
