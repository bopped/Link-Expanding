# Cause fuck grabify
# Any buys let me know
# Python 2
import requests
from bs4 import BeautifulSoup
req = requests.session()

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
}
req.headers.update(headers)
POSTURL = 'http://www.linkexpander.com/get_url.php'
REDIRECTURL = raw_input("ENTER URL\t")
if 'http' not in REDIRECTURL:
    print 'Please have HTTP / HTTPS in front of the URL'
    exit()
URLpayload = {
    'url':REDIRECTURL
}
response = req.post(POSTURL,data=URLpayload)
soup = BeautifulSoup(response.text, "html.parser")
for REDURL in soup:
    REDIRECTEDURL = REDURL
    break
PAGE_SOUP = BeautifulSoup(response.text, "lxml").find('td')
for TITLE in PAGE_SOUP:
    PAGETITLE = TITLE
try:
    print 'Title of the Redirected Page: [ {} ] \nRedirected from: [ {} ] to [ {} ] '.format(PAGETITLE,REDIRECTURL,REDIRECTEDURL)
except NameError:
    print 'Title Not Received from LinkExpander\n'
    print 'Redirected from: [ {} ] to [ {} ] \n'.format(REDIRECTURL, REDIRECTEDURL)