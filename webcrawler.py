import bs4
from urllib.request import urlopen
import re
from sys import argv


def get_number(text):
    regex = re.compile(r'\d+')
    num = regex.findall(text)
    num = [int(i) for i in num]
    return max(num)


def crawler(keyword, number=None):
    if number == None:
        url = 'http://www.shopping.com/products?KW=%s' % (keyword)
        html = urlopen(url)
        soup = bs4.BeautifulSoup(html)
        try:
            spans = soup.find_all('span', attrs={'class': 'numTotalResults'})
            return get_number(spans[0].getText())
        except:
            return "No matches "
    else:
        url = 'http://www.shopping.com/products~PG-%s?KW=%s' % (number, keyword)
        html = urlopen(url)
        soup = bs4.BeautifulSoup(html)
        try:
            spans = soup.find_all('span', attrs={'class': 'quickLookGridItemFullName hide'})
            items = []
            for i in spans:
                items.append(i.getText())
            return items
        except:
            return "No matches "


if __name__ == '__main__':

    if len(argv) == 2:
        name, keyword = argv
        print(crawler(keyword))
    elif len(argv) == 3:
        name, keyword, number = argv
        lis = crawler(keyword, number)
        for i in lis:
            print(i)
    else:
        print("pass keyword or pagenumber as first and second argument")