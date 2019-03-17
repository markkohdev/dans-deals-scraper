import bs4 as bs
import urllib.request


def convert_html_to_dict(flight_item_html) -> dict:
    parsed = {
        'title': flight_item_html.find('h3', {'class': 'entry-title'}).find('a').text,
        'link': flight_item_html.find('h3', {'class': 'entry-title'}).find('a').get('href'),
        'description': flight_item_html.find('div', {'class': 'td-excerpt'}).contents[0].strip().replace('\r\n', ' '),
        'posting_time': flight_item_html.find('time',{'class':'entry-date'}).attrs.get('datetime'),
        'category': flight_item_html.find('a',{'class':'td-post-category'}).text
    }

    return parsed


def main():
    sauce = urllib.request.urlopen('https://www.dansdeals.com/category/airfare-deals/').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    flight_items = soup.find_all('div', {'class': 'td_module_10'})

    parsed = [convert_html_to_dict(item) for item in flight_items]

    pass


main()
