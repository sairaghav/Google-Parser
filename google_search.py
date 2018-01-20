import requests,urllib
from bs4 import BeautifulSoup as BS

def get_summary(search_term):
    response = requests.get('https://www.google.com/search?q='+search_term)
    
    soup = BS(response.text,'html.parser')

    if 'what' in search_term:
        for result in soup.find('div',{'class':'g'}):
            try:
                return result.find('div').text
            except:
                return result.text
    else:
        for result in soup.findAll('span',{'class':'st'}):
            if not '...' in result.text and not result.text is u'':
                return result.text

    return None

def search(search_term,category='',start_page=1,end_page=-1,no_of_results=-1):
    if end_page < start_page:
        end_page = start_page

    cat = ''
    if 'image' in category:
        cat = '&tbm=isch'
    if 'video' in category:
        cat = '&tbm=vid'
    if 'news' in category:
        cat = '&tbm=nws'

    result={}
        
    while start_page <= end_page or len(result) < no_of_results:
        query = 'https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10)+cat

        response = requests.get(query)
        soup = BS(response.text,'html.parser')

        for links in soup.findAll('a'):
            if 'image' in category:
                try:
                    key = links.find('img')['src']
                except:
                    pass
            else:
                key = links.text

            if (no_of_results > 0 and len(result) < no_of_results) or (no_of_results < 0):
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    if 'webcache' not in link and 'http' in link:
                        if not '...' in key and not key is u'':
                            result[key] = link
                except:
                    pass

        start_page += 1

    return result
