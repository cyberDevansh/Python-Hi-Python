#venv means virtual environment 
#TO DOWNLAOD VIRTUAL ENVIRONMENT PACKAGE WE USE pip install virtualenv
# then create and name your own virtual environment by using {   python -m virtualenv dvn  }
# then go to powershell or cmd and activate the virtual environment by using { .\dvn\Scripts\activate } in the same project folder path where virtual environment have to create
#If it worked, you’ll see (dvn) appear before your prompt, like:  (dvn) PS C:\Users\ASTRA\Documents\dvnPython\Advanced Python> in the cmd 
# to deactivate in cmd type { deactivate} in same project path folder 


#SOME MORE THINGS TO LEARN EXCEPT THIS 
# To delete any package pip uninstall pandas
# to delete all the packages without removing the virtual environment and creating a txt file for what deleted pip uninstall -r requirements.txt -y
# to list all the packages use  {  pip list } or { pip freeze }
# If you want to remove all installed packages inside the venv in one go:  
        # pip freeze > requirements.txt
        # pip uninstall -r requirements.txt -y



#more thing i gain is if i use {   .\dvn\Scripts\activate.ps1  }
# activate.bat → for Command Prompt (cmd.exe)
# activate.ps1 → for PowerShell
# activate → for bash/zsh (Linux/Mac)  and this work on all the things
# Activate.csh / Activate.fish → for other shells


# so if we want to download all the packages required in project just we first make file requirements.txt using { pip freeze > requirements.txt } then file will we created then to download all requirements just use { pip install -r .\requirements.txt } and this will downlaod all the requirements 