#----Imported Libraries---
import requests
from bs4 import BeautifulSoup
import smtplib, ssl


URL = "https://www.amazon.in/Redmi-inches-Ultra-Smart-L43R8-FVIN/dp/B0CG5STQFQ/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.d980e9f6-d3ec-4916-9717-3b447a6dedc7&crid=3LFOOA0EHKFX3&keywords=TVs&pd_rd_r=55abd52c-538f-4e43-8f70-9c8666097305&pd_rd_w=2ffW8&pd_rd_wg=w6mH0&pf_rd_p=d980e9f6-d3ec-4916-9717-3b447a6dedc7&pf_rd_r=5C5CKA2SBVB9JTRX361K&qid=1696835905&refinements=p_n_size_browse-bin%3A11962149031&rnid=1485065031&s=electronics&sprefix=tvs%2Celectronics%2C273&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"


#---function to extract price from URL---
def extract_price(URL):
    page = requests.get(URL, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = float(soup.find(attrs={'class':'a-price-whole'}).text.split('.')[0].replace(",", ""))
    return price


#---function to check if price saving txt file exist---
def is_price_file_exists():
    try:
        f = open("save_price.txt", "r")
        Old_price = float(f.read())
        print(f"\nOld Price Existing Rs. {Old_price}.")
    except:
        Old_price = 0
        print("\nOld Price does not Exist!!")
    return Old_price

Old_price = is_price_file_exists() #---if exist then price from file set to Old price else Old price set to 0---
print("\n\nPlease Wait....")

#---Creating/Overwriting price txt fle---
def wcp_tofile():
    f = open("save_price.txt", "w")
    Current_price = extract_price(URL)
    f.write(str(Current_price))
    f.close()
    return float(Current_price)

Current_price = wcp_tofile()


#---Defining Criteria for sending mail----
sender_email = "parvezalamp2@gmail.com"
sender_email_password = "onli pjld fggk pqdx"
receiver_email = "parvezalamp22@gmail.com"

subject = "BUY Now !!"
body = f"Price has fallen on your viewed item to Rs. {round(Current_price)}"
msg = f"Subject: {subject} \n\n {body}"


#----function to send mail----
def notify_via_mail():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, sender_email_password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, msg)
        print(f"\nSending Email to {receiver_email}. Please Wait....")
    except Exception as e:
        # Print any error messages
        print(e)
    finally:
        server.quit()

#---Condition to check if price dropped---
if Current_price < Old_price:
    notify_via_mail()
    print(f"\nHurray! Email Send Successful as Price Dropped to Rs. {Current_price} !")
else:
    print("\nSorry! Email not Sent as Price not dropped.")

