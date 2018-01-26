This utility can be used to get search results from Google.
### Google Search results:
Get results for Google Web search, Image search and Video search

**Usage:** 
- Web results: _search(query)_
- Image results: _search(query,'image')_
- Video results: _search(query,'video')_

**Example:** 
- Web results: _search('earth')_
- Image results: _search('dog','image')_
- Video results: _search('cat','video')_

The results will be returned as a dictionary where the key will be the title displayed for the search result and the value will be URL of the result. To get only the URLs of the search results, use:
_search(query).values()_

In the case of Image search, the key will be link of the image and the URL will be the website on which the image can be found. To get only the images, use:
_search(query).keys()_

The number of results returned can be controlled using the parameters **start_page**, **end_page** and **no_of_results**.

**Example:** 
- _search('god',no_of_results=100).values()_ will return the first 100 URLs on Google for the search term 'god'
- _search('god',start_page=2)_ will return the results on the second page of Google search for the search term 'god'
- _search('god',end_page=5)_ will return all results from the first page to the fifth page for the search term 'god'
- _search('god',start_page=2,end_page=3)_ will return all results from pages 2 and 3 for the search term 'god'
- _search('god',start_page=3,no_of_results=18)_ will return 18 results starting from page 2 for the search term 'god'

Note that _no_of_results_ holds precedence over other parameters. For instance, _search('god',start_page=1,end_page=2,no_of_results=25)_ will return 25 results even if it goes beyond the second page.

### News results:
Get results from Google news on a specific topic. Providing no argument will give you results for the breaking news.

**Usage:**
- Breaking news: _search_news()_
- Topical news: _search_news(topic)_

**Example:**
_search_news('obamacare')_

The results will be returned as a dictionary where the key will be the headlines and the value will be URL of the result. To get only the headlines, use:
_search_news(topic).keys()_

### Google Summary:
Get the summary of information provided by Google on any topic.

**Usage:**
_get_summary(query)_

**Example:**
_get_summary('what is the capital of Australia')_