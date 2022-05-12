# Download Script Python
Wrote this script in Python to download all the photos from my friends wedding. Uses the following libraries:

* Selenium - Used to simulate scrolling so that the photos are loaded into the site.
* Time - Sleeps for 1 second when scrolling to make sure it loads, also sleeps for 1 sec when downloading files. 
* Urllib - to download the images from the html src. 


To run this script you will need to make sure you have selenium installed. Please read the documentation since yyou need to install the driver.

![example](./example.gif)


**NOTE** : to use this on your personal site, you will have to change the following lines in the script
```
url = {{Replace this variable with your url}}
no_of_page_downs = {{replace this with the number of key downs you need to reach the end of the page}}
```