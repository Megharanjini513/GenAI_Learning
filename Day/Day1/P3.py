#pip, virtal environment,.env file
#pip:pip installs the pacakages.package manager

#  virtual environment: A 'venv' is  a directory that contains 
# 1.A copy of the python compiler 
# 2.its own 'pip'
# 3.its own site-packages directory. site-packages=default target location where python installs third party libraries 
#4.Activation script that modify PATH

#steps for entering virtual envi
python --version #windows

#to create virtual envi
python -m venv.venv

#activate the virtual environment 
.venv\Scripts\activate.bat 

# to come out of that we should run
deactivte

# pip instalation (install dependency or libraries)
pip install package_name # syntax

pip install python-dotenv 


.env and virtual one should not be send to repository it runs only in our system , so we create gitignore this files should not send to repo
