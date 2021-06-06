# In[21]:
from os import system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Gpu:
    def __init__(self, upperLimit,lowerLimit, name, offer1, offer2):
        print("gpu const")
        self.upperLimit = upperLimit
        self.lowerLimit = lowerLimit
        self.name = name
        self.offer1 = offer1
        self.offer2 = offer2


class Offer():
    def __init__(self, zustand, price):
        print("offer const")
        self.zustand = zustand
        self.price= price


options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\shiar\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
wd = webdriver.Chrome(executable_path="C:\\Program Files\\chromedriver_win32\\chromedriver.exe", options=options)
wd.implicitly_wait(10)

wd.get("https://www.amazon.de/gp/product/B08LNPPCWJ")


angebot_liste = wd.find_element_by_id("buybox-see-all-buying-choices")
angebote_liste_button = wd.find_element_by_class_name("a-button-inner")
angebote_liste_button.click()


# In[26]:
# Angebot Liste__________MSI RTX 3070 Gaming X Trio________________________
offer_list = wd.find_element_by_id('all-offers-display')
time.sleep(2)

#Print Offer details__________________ Offer 1

article_1 = offer_list.find_element_by_id('aod-price-1')
price_1= article_1.find_element_by_class_name('a-price-whole')
zustand_1 = wd.find_element_by_xpath('//*[@id="aod-offer-heading"]')
title_1 = wd.find_element_by_xpath('//*[@id="productTitle"]') 
print(title_1.text + "\n" + zustand_1.text + "\n" + price_1 .text + "\n")
offer1 = Offer(zustand_1, price_1)


#Print Offer details__________________ Offer 2

article_2 = offer_list.find_element_by_id('aod-price-2')
price_2= article_2.find_element_by_class_name('a-price-whole')
zustand_2 = wd.find_element_by_xpath('//*[@id="aod-offer-heading"]')
title_2 = wd.find_element_by_xpath('//*[@id="productTitle"]') 
print(title_2.text + "\n" + zustand_2.text + "\n" + price_2.text )
offer2= Offer(zustand_2, price_2)

# GPU Object
rtx3070 = Gpu(700, 400,  "rtx 3070", offer1, offer2)

preise = [float(offer1.price.text), float(offer2.price.text)]
password = None
adresse = None
        

# In[2]:
for i in preise:
    if rtx3070.lowerLimit < i < rtx3070.upperLimit : #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FIXME
        print("buy")
        Id1 = wd.find_element_by_id("a-autoid-2")
        Id1.click()
        Id2 = wd.find_element_by_id("hlb-ptc-btn-native")
        Id2.click()
        
        password = wd.find_elements_by_xpath('//*[@id="ap_password"]')
        if len(password) > 0:
            type(password)
            password.send_keys("Shiar&31amazon")
        else:
            pass           
        
        adresse = wd.find_elements_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a')
        if len(adresse) > 0: 
            adresse[0].click()
        else:
            pass
            
        
        Id3 = wd.find_element_by_class_name("a-button-inner")
        Id3.click()
        pass
    else: 
        print("teuer ya 5ra")


# In[35]:

"""

    
else:  


offer_list = wd.find_element_by_id('all-offers-display')
article_2 = offer_list.find_element_by_id('aod-price-2')
price_1 = article_2.find_element_by_class_name('a-price-whole')
price_1.text


# In[36]:


zustand_1 = wd.find_element_by_xpath('//*[@id="aod-offer-heading"]')
zustand_1.text


# In[37]:


offer_list = wd.find_element_by_id('all-offers-display')
article_3 = offer_list.find_element_by_id('aod-price-3')
price_2 = article_3.find_element_by_class_name('a-price-whole')
price_2.text


# In[38]:


zustand_2 = wd.find_element_by_xpath('//*[@id="aod-offer-heading"]')
zustand_2.text


# In[39]:


offer_list = wd.find_element_by_id('all-offers-display')
article_4 = offer_list.find_element_by_id('aod-price-4')
price_3 = article_4.find_element_by_class_name('a-price-whole')
price_3.text


# In[40]:


zustand_3 = wd.find_element_by_xpath('//*[@id="aod-offer-heading"]')
zustand_3.text


# In[41]:


offer_list = wd.find_element_by_id('all-offers-display')
article_5 = offer_list.find_element_by_id('aod-price-5')
price_4 = article_5.find_element_by_class_name('a-price-whole')
price_4.text


# In[42]:


offer_list = wd.find_element_by_id('all-offers-display')
article_6 = offer_list.find_element_by_id('aod-price-6')
price_5 = article_6.find_element_by_class_name('a-price-whole')
price_5.text


# In[43]:


offer_list = wd.find_element_by_id('all-offers-display')
article_7 = offer_list.find_element_by_id('aod-price-7')
price_6 = article_7.find_element_by_class_name('a-price-whole')
price_6.text


# In[44]:


offer_list = wd.find_element_by_id('all-offers-display')
article_8 = offer_list.find_element_by_id('aod-price-8')
price_7 = article_8.find_element_by_class_name('a-price-whole')
price_7.text


# In[ ]:


offer_list = wd.find_element_by_id('all-offers-display')


# In[ ]:


#random_wait_time = random.randrange(3.0, 6.0)
#print(random_wait_time)
#time.sleep(random_wait_time)

time.sleep(1)
#in_den_einkaufswagen = wd.find_element_by_xpath('//*[@id="a-autoid-2"]/span/input')
#in_den_einkaufswagen.click() 


# In[ ]:


#random_wait_time = random.randrange(3.0, 6.0)
#print(random_wait_time)
#time.sleep(random_wait_time)

#proceed_to_checkout = wd.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
#proceed_to_checkout.click()


# In[ ]:


#random_wait_time = random.randrange(3.0, 6.0)
#print(random_wait_time)
#time.sleep(random_wait_time)
#zur_kasse_gehen = wd.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]/span/input')
#zur_kasse_gehen.click()


# In[ ]:


#random_wait_time = random.randrange(3.0, 6.0)
#print(random_wait_time)
#time.sleep(random_wait_time)

email = wd.find_element_by_xpath('//*[@id="ap_email"]')
if email == None: 
    sys.exit()
else:
    type(email)
    email.send_keys("shosh.hs1999@outlook.com")
    
    #random_wait_time = random.randrange(3.0, 6.0)
    #print(random_wait_time)
    #time.sleep(random_wait_time)
    
    weiter = wd.find_element_by_xpath('//*[@id="continue"]')
    weiter.click()
    
    #random_wait_time = random.randrange(3.0, 6.0)
    #print(random_wait_time)
    #time.sleep(random_wait_time)
    
    passwort = wd.find_element_by_xpath('//*[@id="ap_password"]')
    type(passwort)
    passwort.send_keys("Sh89599699@@99@@")
    
    #random_wait_time = random.randrange(3.0, 6.0)
    #print(random_wait_time)
    #time.sleep(random_wait_time)
    
    anmelden = wd.find_element_by_xpath('//*[@id="signInSubmit"]')
    anmelden.click()


# In[ ]:


#random_wait_time = random.randrange(3.0, 6.0)
#print(random_wait_time)
#time.sleep(random_wait_time)

weiter = wd.find_element_by_xpath('//*[@id="continue"]')
weiter.click()


# In[ ]:


#random_wait_time = random.randrange(3.0, 6.0)
#print(random_wait_time)
#time.sleep(random_wait_time)
#passwort = wd.find_element_by_xpath('//*[@id="ap_password"]')
#type(passwort)
#passwort.send_keys("Sh89599699@@99@@")


# In[ ]:


#random_wait_time = random.randrange(3.0, 6.0)
#print(random_wait_time)
#time.sleep(random_wait_time)
#anmelden = wd.find_element_by_xpath('//*[@id="signInSubmit"]')
#anmelden.click()


# In[ ]:


#id = aod-price-1
#class = a-offscreen

angebot = wd.find_element_by_id("aod-price-2")

 """