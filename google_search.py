import requests,urllib
from bs4 import BeautifulSoup as BS

def search(search_term,start_page=1,end_page=-1,no_of_results=-1):
    result_mode = 0
    if no_of_results > 0:
        result_mode = 1

    if end_page < start_page:
        end_page = start_page

    result = []
    
    while start_page <= end_page or len(result) < no_of_results:
        response = requests.get('https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10))

        soup = BS(response.text,'html.parser')

        if result_mode == 1:
            for links in soup.findAll('a'):
                if links.has_attr('href') and len(result) < no_of_results:
                    try:
                        link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                        if 'webcache' not in link and 'http' in link and not link in result:
                            result.append(link)
                    except:
                        pass

        else:
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

def search_image(search_term,start_page=1,end_page=-1,no_of_results=-1):
    result_mode = 0
    if no_of_results > 0:
        result_mode = 1

    if end_page < start_page:
        end_page = start_page

    result = {}
    
    while start_page <= end_page or len(result) < no_of_results:
        response = requests.get('https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10)+'&tbm=isch')

        soup = BS(response.text,'html.parser')

        if result_mode == 1:
            for source_url in soup.findAll('a'):
                if len(result) < no_of_results:
                    try:
                        img_url = source_url.find('img')['src']
                        result[img_url] = urllib.unquote(source_url['href'].split('url?q=')[1].split('&sa')[0])
                    except:
                        pass
        else:
            for source_url in soup.findAll('a'):
                try:
                    img_url = source_url.find('img')['src']
                    result[img_url] = urllib.unquote(source_url['href'].split('url?q=')[1].split('&sa')[0])
                except:
                    pass

        start_page += 1
        
    return result

def search_video(search_term,start_page=1,end_page=-1,no_of_results=-1):
    result_mode = 0
    if no_of_results > 0:
        result_mode = 1

    if end_page < start_page:
        end_page = start_page

    result = []
    
    while start_page <= end_page or len(result) < no_of_results:
        response = requests.get('https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10)+'&tbm=vid')

        soup = BS(response.text,'html.parser')

        if result_mode == 1:
            for links in soup.findAll('a'):
                if links.has_attr('href') and len(result) < no_of_results:
                    try:
                        link = urllib.unquote(links['href'].split('url?q=')[1].split('&sa')[0])
                        if 'webcache' not in link and 'http' in link and not link in result:
                            result.append(link)
                    except:
                        pass

        else:
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

def search_news(search_term,start_page=1,end_page=-1,no_of_results=-1):
    result_mode = 0
    if no_of_results > 0:
        result_mode = 1

    if end_page < start_page:
        end_page = start_page

    result = {}
    
    while start_page <= end_page or len(result) < no_of_results:
        response = requests.get('https://www.google.com/search?q='+search_term+'&start='+str((start_page-1)*10)+'&tbm=nws')

        soup = BS(response.text,'html.parser')

        if result_mode == 1:
            for headlines in soup.findAll('a'):
                if headlines.has_attr('href') and len(result) < no_of_results:
                    try:
                        url = urllib.unquote(headlines['href'].split('url?q=')[1].split('&sa')[0])
                        if 'webcache' not in url and 'http' in url and not url in result:
                            if not '...' in headlines.text and not headlines.text is u'':
                                result[url] = headlines.text
                    except:
                        pass

        else:
            for headlines in soup.findAll('a'):
                if headlines.has_attr('href'):
                    try:
                        url = urllib.unquote(headlines['href'].split('url?q=')[1].split('&sa')[0])
                        if 'webcache' not in url and 'http' in url and not url in result:
                            if not '...' in headlines.text and not headlines.text is u'':
                                result[url] = headlines.text
                    except:
                        pass
            

        start_page += 1

    return result


def get_summary(search_term):

    response = requests.get('https://www.google.com/search?q='+search_term)
    
    soup = BS(response.text,'html.parser')

    if 'what' in search_term:
        for result in soup.find('div',{'class':'g'}):
            return result.find('div').text
        
    else:
        for result in soup.findAll('span',{'class':'st'}):
            if not '...' in result.text and not result.text is u'':
                return result.text

    return None
