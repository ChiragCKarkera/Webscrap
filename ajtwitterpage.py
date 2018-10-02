
import urllib2
import re
from bs4 import BeautifulSoup

ajtwitter = urllib2.urlopen( "https://twitter.com/arunjaitley")
soup = BeautifulSoup(ajtwitter, 'html.parser')
all_links=soup.find_all('a', attrs={'href': re.compile("^http://")})
#all_tags=soup.find_all('b', attrs={'href': re.compile("^hashtag")})
#soup.fetch('td', {'valign':re.compile('top')})

#input_raw=()
#attach with below website
#http://www.purgomalum.com/service/xml?text=this is some test input
for link in all_links:
	a= open ('arunjaitley.csv','a+')
	a.write(str(link.get('href'))+'\n')
	a.close()		
