import requests,urllib
from bs4 import BeautifulSoup as BS

def search(search_term,start_page=1,end_page=-1):

    if end_page < start_page:
        end_page = start_page

    result = []
    
    while start_page <= end_page:
        response = requests.get('https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10))

        soup = BS(response.text,'html.parser')

        for links in soup.findAll('a'):
            if links.has_attr('href'):
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    if 'webcache' not in link and 'http' in link and not link in result:
                        result.append(link)
                except:
                    pass

        start_page += 1

    return result

def search_image(search_term,start_page=1,end_page=-1):

    if end_page < start_page:
        end_page = start_page

    result = []
    
    while start_page <= end_page:
        response = requests.get('https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10)+'&tbm=isch')

        soup = BS(response.text,'html.parser')

        for links in soup.findAll('img'):
            if links.has_attr('src'):
                result.append(links['src'])

        start_page += 1

    return result

def search_video(search_term,start_page=1,end_page=-1):

    if end_page < start_page:
        end_page = start_page

    result = []
    
    while start_page <= end_page:
        response = requests.get('https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10)+'&tbm=vid')

        soup = BS(response.text,'html.parser')

        for links in soup.findAll('a'):
            if links.has_attr('href'):
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    if 'webcache' not in link and 'http' in link and not link in result:
                        result.append(link)
                except:
                    pass

        start_page += 1

    return result


def get_summary(search_term):

    response = requests.get('https://www.google.com/search?q='+search_term+'&start=0')
    
    soup = BS(response.text,'html.parser')

    for result in soup.findAll('span',{'class':'st'}):
        if not '...' in result.text and not result.text is u'':
            return result.text

    return None
