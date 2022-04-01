# chemical-search-engine


ieee iNTUition v7.0: A web application which takes in a list of chemicals provided by a client and searches for a match within HP’s internal database, which is then translated into English. There is code to find the HP's pdf using google search and web scraping, and there is code to scan the HP PDF document and getting the required row for chemicals.
This is to aid sustainability efforts and to help solve the problem statement.

googlesearch uses beautiful soup and selenium to web scrape - beautiful soup does only static scraping and ignores JavaScript. The combination of beautiful soup & selenium will help to do dynamic scraping, as selenium automates web browser interaction from python. So, data rendered by JavaScript links can be made available by automating button clicks with selenium, and data, can be extracted by beautiful soup.
googlesearch will be able to lead us to the document containing the list of chemicals (extracting tables and data, as well as translation, is done by chemical-search-engine).
