import datetime
from datetime import datetime
import os
import time
import smtplib
import imghdr
from email.message import EmailMessage
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

login_url = 'https://www.daraz.pk'

driver = webdriver.Chrome('C://chromedriver//chromedriver')
driver.get(login_url)
driver.maximize_window()

def main():


#Sometimes Google Duplicates That Input Field So we have to iterate...

    inputElems = driver.find_elements_by_css_selector('input[name=q]')

    for inputElem in inputElems:
        inputElem.send_keys('jewellery for girls')
        inputElem.send_keys(Keys.ENTER)
  
    elem=driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a')
    for elem in elem:
        elem.send_keys(Keys.ENTER)

    element = driver.find_element_by_tag_name('body')
    element_png = element.screenshot_as_png
    with open("test2.png", "wb") as file:
        file.write(element_png)  

# Page Down 
    time.sleep(2)
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    
    element_png = element.screenshot_as_png
    with open("customer_reviews.png", "wb") as file:
        file.write(element_png) 
    
    ## Writing Index Html File
    current_url_record=driver.current_url
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  
    text = '''
        
<!DOCTYPE html>
<html>
    <body>
        
        <h3 style="color:black;">I am a Daraz Bot and i got one of the best product for you </h3>
        <h3 style="color:black;">Please see the following attachment</h3>
        <h3 style="color:black;"> Congratulations! We've successfully fetching product record</h3>
        Go to the page: <a href="{current_url_record}">click here</a>
        <h3 style="color:black;"> Time is {now} </h3>
        <h3 style="color:black;"> Date is {dt_string} </h3>
        <h3 style="color:blue;"> Regards Adil  </h3>
      
        

    </body>
    </html>

    '''.format(current_url_record=current_url_record,now=now,dt_string=dt_string)
    file = open("index.html","w")
    file.write(text)
    file.close()
    time.sleep(3)
<<<<<<< HEAD


=======


>>>>>>> c2251c5 (Adding the CC Option)
    
#   ## Add to Cart Product
#     elem=driver.find_elements_by_xpath('//*[@id="module_add_to_cart"]/div/button[2]')
#     for elem in elem:
#         elem.send_keys(Keys.ENTER)
#         webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
       

# EMail
    FROM_EMAIL_ADDRESS = ""
    EMAIL_PASSWORD = ""

    contacts = []
    carbon_copy=[]

    files = ['C://Users//Windows 10//Desktop//Daraz Automation//index.html','C://Users//Windows 10//Desktop//Daraz Automation//customer_reviews.png','C://Users//Windows 10//Desktop//Daraz Automation//test2.png']

    msg = EmailMessage()
    msg['Subject'] = 'A Daraz Bot'
    msg['From'] = FROM_EMAIL_ADDRESS
    msg['To'] = ', '.join(contacts)
    msg['CC']= ','.join(carbon_copy)
    msg_body = 'Please check if you have received {}attachments'.format(len(files))
# The email body displays this text only if it cannot display the HTML content
# add in the enxt line
    msg.set_content(msg_body)
# The email is received with this HTML data as the email body
    msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        
        <h3 style="color:black;">I am a Daraz Bot and i got one of the best product for you </h3>
        <h3 style="color:black;">Please see the following attachment</h3>

        <h3 style="color:black;"> Congratulations! We've successfully fetched Product records.</h3>
        Go to the page: <a href="{current_url_record}">click here</a>
        <h3 style="color:black;"> Time is {now} </h3>
        <h3 style="color:black;"> Date is {dt_string} </h3>
        <h3 style="color:blue;"> Regards Adil  </h3>
        

    </body>
    </html>

""".format(current_url_record=current_url_record,now=now,dt_string=dt_string), subtype='html')
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()



     
        
        # Determines what the file type of the image is
    if 'jpg' in f.name or 'png' in f.name:

        file_type = imghdr.what(f.name)
        file_name = f.name
        file_name = file_name.split('/')
        filename = file_name[-1]
    if 'jpg' in filename or 'png' in filename:

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=filename)
        
    else:
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login(FROM_EMAIL_ADDRESS, EMAIL_PASSWORD)
         smtp.send_message(msg)
    print("Email has been sent")
    time.sleep(2)
    
if __name__== '__main__':
    main()
    
