# Ecommerce Price Tracker (Amazon)
Description: This application is used for tracking price from an ecommerce product URL and send notification to the User by E-mail when price dropped.

Milestone in this application: In this application there are three milestones: -
1.	Extract the price from the given URL of product from amazon website.
2.	Check whether the price is low or high from the previous one.
3.	If low price found then send e-mail notification to the user about price Dropped.

Language and Libraries used in this application: -
1.	Python 3.11.2 (Language)
2.	Requests (Library)
3.	Beautiful Soup (Library)
4.	smptlib (library)

---------------------------------------------- How to Use---------------------------------------------------------
1. Install python version 3 above and create a virtual Environment.
2. Copy the requirement.txt file from the ecommerce_price_tracker folder to your virtal environment folder
3. Activate virtual environment and run command (pip install -r requirement.txt) in your command prompt. All libraries should install automatically which is used in this application.
4. Copy Main_program folder to your virtual environment.
5. Open amazon_price_tracker.py file in notepad or python IDLE
6. Change product URL on line 7. Enter any product URL from the amazon.
7. Change sender_email, sender_email_password and receiver_email on line 44, 45, 46 respectively and save the file.
8. Then run the amazon_price_tracker.py in the command prompt. All task would be done automatically.

---------------------------------------------- Working of application ----------------------------------------------
1.	When you run the file it will search url with the help of Beautiful Soup library and it will grab the price of the Product from the URL.
2.	After that the price was extracted, it will check for a save_price file in the same folder exist or not, if exist it get the price from file and store in Old_price variable and if not exists it will set Old_price to 0.
3.	After that it will write the current price grabbed from URL to the file and remove the old price if any, because old price was stored in variable.
4.	After that it will check the difference between the Old and Current price. If Current Price is lower than old price then it will send the mail to user as notification and if the current price is not lower then it will not send any mail to the user.



