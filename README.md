** Behave BDD Automation Framework **
  BDD framework built using Python language with behave to support web application automation on various browsers.
  
  ** What are all implemented in Framework **
    1. Page Object Design Pattern.
    2. Behave BDD feature and step definition to design scenario.
    3. Utility functions to handle Driver methods, Fetching test data and handle OS methods.
    4. Allure reports for test execution details.

**Getting Started: **
    ** Prerequisites **
      Python version > 3
      
** Setup using Pycharm IDE **

       Download and install Python as per your OS from here https://www.python.org/downloads/

       Clone the repository using git clone "<repository url>"

       Install Pycharm IDE : https://www.jetbrains.com/pycharm/download

       Open the Cloned project and Go to project settings. Select the Python version from the Python interpreter.

       Add packages behave, selenium, allure-behave.

 ** How to run the tests **

       behave features --tags=profile_submission (tags are added as part of feature files.)

** How to generate Allure Report **

        Install Node latest version.
        
        npm install -g allure-commandline
        
        allure --version
        
        pip3 install allure-behave or add from pycharm package.

        behave -f allure_behave.formatter:AllureFormatter -o Reports/ features --tags=profile_submission --no-capture

        allure server Reports
        
 ** Built with **

        Python 3.12

        Selenium 4.20.0

        Behave  1.2.6

        Allure-behave 2.13.5

        

        
    
       
