# WorldQuant-Brain
## 0824 
for loops include input strategies and parameters of settings  
Finally the simulate button
## further issue
How to record and save the Insample data which pass the IS test

## Automation Steps
1. Connect to webpage
2. Login webpage ~ simulate page
3. Search alpha
    * Give input command and adjustable parameters
        * Iterate each parameter and settings
        * Click simulate button
        * return & save check information

## Sample command
* For Abner
  * `python3 automation.py -d ./chromeDriver -n Subindustry Industry Sector Market --decays 4 10 -t 0.01 0.08 --your_email abnerteng16@gmail.com --your_password teng1234 -c ./price_to_volume.csv`
* For Tim
  * `python3 automation.py -d ./chromedriver104 -n Subindustry Industry Sector Market --decays 4 10 -t 0.01 0.08 --your_email hsutim2000@gmail.com --your_password Kingkasermin -c ./price_to_volume.csv`
* General
  * `python3 automation.py -d your Chrome Driver -n Subindustry Industry Sector Market --decays 4 10 -t 0.01 0.08 --your_email email --your_password  password -c ./price_to_volume.csv`