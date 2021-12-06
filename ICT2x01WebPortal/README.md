# ICT2101-2201-Team-Project
Group Members: 

  1. Suhaimi Bin Roslan (2001684)
  2. Sim Kai Ching (2001759)
  3. Khairul Anuwar (2001093)
  4. Erin Chee Hwee Kah (2001418)
  5. Lee Cheng Hao (2001657)

# How to run
1. Copy URL of git repository
2. Open Pycharm IDE
3. Create new project in your local machine
4. Click on VCS tab on top side of Pycharm IDE -> Import into Version Control -> Create Git Repository
5. Locate the new project you just created and click on OK.
6. Click on Terminal tab at the bottom of Pycharm IDE
7. If terminal shows a different directory as the project you created, change directory into it by using cd <directory to project>
8. Type "pip install flask" in terminal
9. To run the project, type "python flask1.py" and click on URL that show up

# Development Workflow
(provide a brief yet sufficiently comprehensive description of your team’s workflow using git and GitHub features)

Using Git, we have created:
1) main branch - the version that is finished developing and tested is pushed to here, Not allowed to be changed unless all group members verified and agreed on the version.
2) dev branch - where we do our development.
3) individual branches - each developer developed and work on thier own personal features in thier own branch

Our Current Structure in Github

Main
- Dev
  - kai ching
  - Erin
  - Khairul
  - cheng hao


# UAT 
## Use Case Diagram
<img src="https://github.com/Team01-2/ICT2101-2201-Team-Project/blob/main/wiki_images/UseCaseDiagram.png" width="700" height="450">

## System State Diagram
<img src="https://github.com/Team01-2/ICT2101-2201-Team-Project/blob/main/wiki_images/SystemStateDiagram.png" width="700" height="450">

## System Test Cases Video
- an embedded video that runs through all the system test cases you have created (and refined) from M2
- ~3 mins long to cover all system tests

# Whitebox Testing
# Chosen Class: Challenge Map Builder
  ## The challenge map builder control class is mainly responsible for the creating, loading, deleting and saving of maps in the application. Thus, the team has decided to test on functions that resides within the class(line 279 to 377 of flask1.py) as well as the interaction with the database entity class(CRUDdbFunc.py).
  
# How statistics are generated
 ## The test cases were ran and automated with the help of unittest library provided. This library is included at the top of the test files and functions are tested by making use of the assert function provided. The team also ensured a complete coverage by asserting the different possible paths in the functions tested. As for generation of coverage statistics, we have make use of the coverage library that was installed.

# Test cases
 ## List of Test Cases (Total 9 test cases)
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
  2. To run the coverage test on test_challengeMapBuilder.py and test_CRUD.py, type "coverage run test_challengeMapBuilder.py/test_CRUD.py"
  3. Follow by "coverage report -m" to view the code coverage
  4. Type "coverage html" on terminal to generate coverage statistics to be viewed on browser
