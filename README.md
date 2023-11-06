Steps to generate the Custom Python wheel file 

- Create the libraries or the code need to be included in teh package - create the __init__ file as wel to consider that module as a package 
- After that install the setuptools using command " pip install setuptools"
- Also install the wheel package using "pip install wheel"
- After that create the setup.py file and add the respected details 
  - File Name 
  - Author
  - Description
  - Package included
  - Libraries added as a part of this wheel
    - You can read and add the packages dynamically form the requirements.txt file as well
- After that create the wheel file using command "python3 setup.py bdist_wheel"