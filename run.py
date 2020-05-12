from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.parse import quote   

from time import sleep

#update css selector if you have any issues
css_selector = "#main > footer > div._3pkkz.V42si.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text"

# message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys
msg = '''
Hey!!
This message is sent by automation.
'''     
driver = webdriver.Chrome()

phone = []                                                      #enter comma separated 10 digit phone numbers here or read them from the numbers_file
with open ('numbers.txt') as numbers_file:                    #uncomment these three three lines to read input from numbers.txt file
    for line in numbers_file:
    	line=line.strip()
    	if len (line)==10:								   		#skip numbers of length not equal to 10
    		phone.append(str(line))
        


msg = quote(msg)  # url-encode the message, use other functios for handling dictionaries, not recommended
driver.get("https://web.whatsapp.com")  
sleep(60) #update your time  of delay incase internet is slow
for number in phone:
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    sleep(3)  
    for i in range(100):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            break
        except:
            print("not yet")
            sleep(1)
    print ('Last Number '+ str(number))
print ("Done")
# driver.quit()                                                 #uncomment to close chrome window as scoon as program ends
