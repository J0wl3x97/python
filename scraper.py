import requests
from bs4 import BeautifulSoup
import time

#redmi_page=requests.get('https://www.flipkart.com/search?q=redmi+note+7+pro&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_7&otracker1=AS_QueryStore_OrganicAutoSuggest_0_7&as-pos=0&as-type=RECENT&as-backfill=on')
redmi_page=requests.get('https://www.flipkart.com/search?q=redmi+note+7+pro&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_5&otracker1=AS_QueryStore_OrganicAutoSuggest_0_5&as-pos=0&as-type=RECENT&as-backfill=on')

#print(redmi_page.text)

soup_page=BeautifulSoup(redmi_page.text,"html.parser")
#print(soup_page)

#getting phones names
redmi=soup_page.find_all(class_='_3wU53n')

redmi_prices=soup_page.find_all(class_="_1vC4OE _2rQ-NK")
#print(prices[0].text)

comingsoon=soup_page.find_all(class_="_3aV9Tq")
comingsoonnew=[]



for item in range(0,len(redmi)):
    print(redmi[item].text,end="            ")
    print(redmi_prices[item].text)

for every in range(0,len(comingsoon)):
    comingsoonnew.append(comingsoon[every].text)
    print(comingsoonnew[every])


#monitoring items
test=0
while test!=1:
    newpage=requests.get('https://www.flipkart.com/search?q=redmi+note+7+pro&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_5&otracker1=AS_QueryStore_OrganicAutoSuggest_0_5&as-pos=0&as-type=RECENT&as-backfill=on')
    
    newsoup=BeautifulSoup(newpage.text,"html.parser")
    phone=newsoup.find_all(class_="_3wU53n")
    newphone=[]
    for i in range(0,len(phone)):
        newphone.append(phone[i].text)
    prices=newsoup.find_all(class_="_1vC4OE _2rQ-NK")
    if len(redmi)<len(phone):
        print("some more phones are added")
    elif len(redmi)>len(phone):
        print("some phones are deleted")
    else:
        #print(redmi_prices)
        #print(prices)
        for i in range(0,len(redmi_prices)):
            print(redmi_prices[i].text,end="     ")
            print(prices[i].text)
        test=1
            #print("product prices have changed")
##        #monitoring prices
##        for every in range(0,len(redmi_prices)):
##            #print(redmi_prices[every])
##            #print(prices[every].text)
##            if redmi_prices[every].text==prices[every].text:
##                pass
##            else:
##                print("product prices have changed")
    #time.sleep(1)        
    

    
#print(comingsoon)







    
