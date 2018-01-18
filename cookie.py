import requests , time
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

"""
# cookie
params = {'username': 'Ryan', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print( r.cookies.get_dict())
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies= r.cookies)
print( r.text)


# session
session = requests.session()
params = {'username': 'R', 'password': 'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print( s.cookies.get_dict())
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print( s.text)


#basic auth
auth = HTTPBasicAuth('rr','ppp')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php",auth=auth)
print(r.text)

"""
PJ = 'C:\\bk\\_tool\\'
driver = webdriver.PhantomJS(executable_path=PJ)
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'
driver.get(url)
time.sleep(3)
print(driver.find_elements_by_id('content').text)
driver.close()
#


"""
driver = webdriver.PhantomJS( executable_ path='< Path to Phantom JS>')
driver.get("http://pythonscraping.com")
driver.implicitly_wait( 1)
print(driver.get_cookies())

savedCookies = driver.get_cookies()

driver2 = webdriver.PhantomJS( executable_ path='< Path to Phantom JS>')
driver2.get("http://pythonscraping.com")
driver2.delete_all_cookies()
for cookie in savedCookies:
    driver2.add_cookie(cookie)

driver2.get("http://pythonscraping.com")
driver2.implicitly_wait( 1)
print(driver2.get_cookies())



# trap

driver = webdriver.PhantomJS( executable_path='')
driver.get(" http://pythonscraping.com/pages/itsatrap.html")
links = driver.find_elements_by_tag_name("a")
for link in links:
    if not link.is_displayed():
        print("The link "+link.get_attribute("href")+" is a trap")

fields = driver.find_elements_by_tag_name("input")
for field in fields:
    if not field.is_displayed():
        print("Do not change value of "+field.get_attribute("name"))
"""
