# ICT2101-2201-Team-Project
Group Members: 

  1. Suhaimi Bin Roslan (2001684)
  2. Sim Kai Ching (2001759)
  3. Khairul Anuwar (2001093)
  4. Erin Chee Hwee Kah (2001418)
  5. Lee Cheng Hao (2001657)

# How to run
1. Download MySQL Installer (https://dev.mysql.com/downloads/installer/)
2. Run & install MySQL Installer
  - "Choosing Set up Type" section - select custom
  - “Select Products” section - select MySQL Server, Connector/Python 8.0.27, MySQL Documentation 
  - "Installation" section - select execute
  - "Product Configuration" section - leave as default (username and password should be "root")
3. Open MySQL Workbench and click on Local Instance under MySQL Connection
4. Insert the statements given in dbcreate.txt and execute
5. Refresh Database
6. Copy URL and download from the **Main** branch of our GITHUB repository
7. Unzip project folder
8. Run Python Command Line Terminal
9. If terminal shows a different directory as the project you created, change directory into it by using cd <directory to project>
10. Type "pip install flask" in terminal
  ```
  pip install flask
  ```
11. Type "pip install mysql-connector-python" in terminal
  ```
  pip install mysql-connector-python
  ```
12. To run the project, type "python flask1.py" and click on URL that show up
  ```
  python flask1.py
  ```

For more information, please refer to our User Manual Here: https://github.com/Team01-2/ICT2101-2201-Team-Project/blob/main/User%20Manual.pdf
# Development Workflow
Using Git, we have created:
1) main branch - baseline versions that are developed and tested are pushed here, not to be changed unless all group members verified and agreed on the new baseline version.
2) dev branch - where we store our development build
3) individual branches - each developer develops features assigned to them in their own branch
4) Github Project Board feature to track our progress and tasks allocated during our meetings (https://github.com/Team01-2/ICT2101-2201-Team-Project/projects/1)
  - Backlog (For tracking and documentation purposes)
  - Current To-Do List (List of tasks we have come up with after every meeting, with a deadline)
  - To-Do List (Tasks related to Website ONLY)
  - To-Do List (Tasks related to Others, E.g Database, Documentations)
  - In Progress (Tasks that are currently on-going)
  - Completed (Completed Tasks)
  - Diagrams & Calculations (All the latest diagrams and calculations goes here)
5) Github Issues feature to track major development changes during our project 
 
# UAT 
## Use Case Diagram
<img src="https://github.com/Team01-2/ICT2101-2201-Team-Project/blob/main/wiki_images/UseCaseDiagram.png" width="700" height="450">

## System State Diagram
<img src="https://github.com/Team01-2/ICT2101-2201-Team-Project/blob/main/wiki_images/SystemStateDiagram.png" width="700" height="450">

## System Test Cases Video
![](https://github.com/Team01-2/ICT2101-2201-Team-Project/blob/main/wiki_images/ICT2101-P1-2-UAT.gif)

 Or view this at https://drive.google.com/file/d/1xGjjpOblQPOlJRw5hZVAjBe_Hd7VzMq8/view?usp=sharing
  
# Whitebox Testing
## Chosen Class: Challenge Map Builder
The challenge map builder control class is mainly responsible for the creating, loading, deleting and saving of maps in the application. Thus, the team has decided to test functions that reside within the class (line 279 to 377 of flask1.py) as well as the interaction with the database entity class (CRUDdbFunc.py).

![](https://github.com/Team01-2/ICT2101-2201-Team-Project/blob/main/wiki_images/ICT2101_P1-2_WhiteboxTesting.gif)
  
Or view this at https://drive.google.com/file/d/15bIUUUl_7MFW9nE8cq0G4d9ymnI1s2p1/view?usp=sharing
  
## How statistics are generated
The test cases were ran and automated with the help of unittest library. This library is included at the top of the test files and functions are tested by making use of the assert function. The team also ensured a complete coverage by asserting the different possible paths in the functions tested. As for generation of coverage statistics, we have made use of the coverage library that was installed.
  
## Test cases
 List of Test Cases (Total 9 test cases)
  - test_saveMap
  - test_loadMap
  - test_deleteMap
  - test_createMap
  - test_insertMap
  - test_selectMap
  - test_insertCmdHistory
  - test_selectCmdHistory
  - test_deleteMap (database delete)
  
 ## How to run
  1. pip install coverage on terminal
  ```
  pip install coverage
  ```
  2. To run the coverage test on test_challengeMapBuilder.py and test_CRUD.py, type "coverage run test_challengeMapBuilder.py/test_CRUD.py"
  ```
  coverage run test_challengeMapBuilder.py #replace test_challengeMapBuilder.py with test_CRUD.py for testing on test_CRUD.py
  ```
  3. Follow by "coverage report -m" to view the code coverage
  ```
  coverage report -m
  ```
  4. Type "coverage html" on terminal to generate coverage statistics to be viewed on browser
  ```
  coverage html
  ```
