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
* `python3 automation.py --driver_path ./chrome_driver --url https://platform.worldquantbrain.com/simulate --neutralizations None Market Sector Industry Subindustry --decays 1 2 3 4 5 --truncations 0.01 0.02 0.03 0.04 0.05`