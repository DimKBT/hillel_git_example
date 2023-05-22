import urllib
from urllib.pars import urlparse

def parse(query: str) -> dict:
    query_part = urllib.parse.urlparse(query).query
    if not query_part:
        return {}
    else:
        devided_result = query_part.strip('&').split('&')
        devided_result_parts_list = [item.split('=') for item in devided_result]
        devided_result_dict = {item: value for item, value in devided_result_parts_list}

    return devided_result_dict

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://flyandlure.org/articles/fly_fishing/fly_fishing_diary_july_2020?q=word&b=something#anchor') == {'q': 'word', 'b': 'something'}
    assert parse('https://www.google.com/search?q=how+to+dispose+of+a+corpse&oq=how+to+dispose+of+a+corpse&aqs=chrome') == {'q': 'how+to+dispose+of+a+corpse', 'oq': 'how+to+dispose+of+a+corpse', 'aqs': 'chrome'}
    assert parse('https://example.com/path/to/page?name=file') == {'name': 'file'}
    assert parse('https://https://practicaldatascience.co.uk/data-science?') == {}
    assert parse('https://books.com/path/to/page?reader=stylish+book&page=11') == {'reader': 'stylish+book', 'page': '11'}
    assert parse('https://exercises.com/page?name=math') == {'name': 'math'}
    assert parse('https://exercises.com/page?tag=quality') == {'tag': 'quality'}
    assert parse('https://worldofbooks.com/index?name=admin&password=123') == {'name': 'admin', 'password': '123'}
    assert parse('https://worldofbooks.com/index?') == {}
    assert parse('https://example.com/path/to/page?lang=eng') == {'lang': 'eng'}



def parse_cookie(query: str) -> dict:
    return {}

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
