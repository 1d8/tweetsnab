from bs4 import BeautifulSoup
from requests import get
#add functionality to avoid error messages if user does not exist:
#method 1: If response code is 200: continue with process, else: print acc not found
#method 2: try & except statement
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
username = input("Username: >")
url = "https://twitter.com/" + username
response = get(url, headers=headers)
if response.status_code == 404:
    print('Account not found')
else:
    html_soup = BeautifulSoup(response.text, 'html.parser')
    tweet = html_soup.find_all('div', class_='js-tweet-text-container')
    bio = html_soup.find_all('p', class_='ProfileHeaderCard-bio u-dir')
    bio2 = html_soup.find_all('div', class_='ProfileHeaderCard-joinDate')
    bio3 = html_soup.find_all('div', class_='ProfileHeaderCard-location')
    bio4 = html_soup.find_all('div', class_='ProfileHeaderCard-birthdate')
    bio5 = html_soup.find_all('div', class_='ProfileHeaderCard-url')
    print('TWEETS')
    #cycles through the scraped tweets from tweet var
    print('----------------------------------------------')
    for i in tweet:
        first = tweet[0]
        first = first.text
        print(first)
        tweet.pop(0)
    print('----------------------------------------------')
    #stripping uglyness from scraped elements
    second = bio[0]
    second = second.text
    third = bio2[0]
    third = third.text
    third = third.replace('\n', '')
    third = third.replace('Joined','')
    fourth = bio3[0]
    fourth = fourth.text
    fourth = str(fourth)
    fourth = fourth.replace(' ', '')
    fourth = fourth.replace('\n', '')
    fifth = bio4[0]
    fifth = fifth.text
    fifth = fifth.replace('\n', '')
    fifth = fifth.replace(' ', '')
    fifth = fifth.replace('Born', '')
    sixth = bio5[0]
    sixth = sixth.text
    sixth = sixth.replace('\n', '')
    sixth = sixth.replace(' ', '')

    if int(len(second)) == 0:
        print('Bio: Not Provided')
    else:
        print('Bio:', second)

    if int(len(third)) == 0:
        print('Joined: Not Provided')
    else:
        print('Joined:', third)

    if int(len(fourth)) == 0:
        print('Alleged Location: Not Provided')
    else:
        print('Alleged Location:', fourth)

    if int(len(fifth)) == 0:
        print('Birthdate: Not Provided')
    else:
        print('Birthdate:', fifth)

    if int(len(sixth)) == 0:
        print('Site: Not Provided')
    else:
        print('Linked Site:', sixth)
