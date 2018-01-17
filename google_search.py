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

def get_urls(soup,start_page,end_page,no_of_results):
    result=[]
    
    result_mode = 0
    if no_of_results > 0:
        result_mode = 1
        
    while start_page <= end_page or len(result) < no_of_results:
        for links in soup.findAll('a'):
            if result_mode == 1 and len(result) < no_of_results:
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    if 'webcache' not in link and 'http' in link and not link in result:
                        result.append(link)
                except:
                    pass
            if result_mode == 0:
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    if 'webcache' not in link and 'http' in link and not link in result:
                        result.append(link)
                except:
                    pass
        start_page += 1

    return result

def get_img_urls(soup,start_page,end_page,no_of_results):
    result={}
    
    result_mode = 0
    if no_of_results > 0:
        result_mode = 1
        
    while start_page <= end_page or len(result) < no_of_results:
        for links in soup.findAll('a'):
            if result_mode == 1 and len(result) < no_of_results:
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    result[links.find('img')['src']] = link
                except:
                    pass
            if result_mode == 0:
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    result[links.find('img')['src']] = link
                except:
                    pass
        start_page += 1

    return result

def get_news_urls(soup,start_page,end_page,no_of_results):
    result={}
    
    result_mode = 0
    if no_of_results > 0:
        result_mode = 1
        
    while start_page <= end_page or len(result) < no_of_results:
        for links in soup.findAll('a'):
            if result_mode == 1 and len(result) < no_of_results:
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    if 'webcache' not in link and 'http' in link and not link in result:
                       if not '...' in links.text and not links.text is u'':
                                result[link] = links.text 
                except:
                    pass
            if result_mode == 0:
                try:
                    link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                    if 'webcache' not in link and 'http' in link and not link in result:
                        if not '...' in links.text and not links.text is u'':
                                result[link] = links.text
                except:
                    pass
        start_page += 1

    return result

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

    query = 'https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10)+cat

    response = requests.get(query)
    soup = BS(response.text,'html.parser')
    
    if '' in category or 'video' in category:
        res = []
        res = get_urls(soup,start_page,end_page,no_of_results)
    if 'image' in category:
        res = {}
        res = get_img_urls(soup,start_page,end_page,no_of_results)
    if 'news' in category:
        res = {}
        res = get_news_urls(soup,start_page,end_page,no_of_results)

    return res
