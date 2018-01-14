import requests,urllib
from bs4 import BeautifulSoup as BS

def search(search_term):

    response = requests.get('https://www.google.com/search?q='+search_term+'&start=0')

    result = []

    soup = BS(response.text,'html.parser')

    for links in soup.findAll('a'):
        if links.has_attr('href'):
            try:
                link = links['href'].split('url?q=')[1].split('&sa')[0]
                if 'webcache' not in link and 'http' in link and not link in result:
                    result.append(urllib.unquote(link))
            except:
                pass

    return result


def get_summary(search_term):

    response = requests.get('https://www.google.com/search?q='+search_term+'&start=0')

    results = []

    soup = BS(response.text,'html.parser')

    for result in soup.findAll('span',{'class':'st'}):
        if not '...' in result.text and not result.text is u'':
            results.append(result.text)

    try:
        return results[0]
    except:
        return None
    
