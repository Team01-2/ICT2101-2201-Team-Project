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
  - "Product Configuration" section - leave as default
3. Open MySQL Workbench and click on Local Instance under MySQL Connection
4. Insert the statements given in dbcreate.txt and execute
5. Refresh Database
6. Copy URL and download from the Main branch of our GITHUB repository
7. Unzip project folder
8. Run Python Command Line Terminal
9. If terminal shows a different directory as the project you created, change directory into it by using cd <directory to project>
10. Type "pip install flask" in terminal
11. To run the project, type "python flask1.py" and click on URL that show up

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
- <Insert video here>

# Whitebox Testing
# Class
- choose one meaningful class to demonstrate your test code. “Meaningful” here means 2 or more interactions with other classes, e.g., a Control class. 
- Please do not use an entity class.

# Test cases
- list the test cases for this test suite (for this one class) and where they reside in your repo
- show code coverage statistics for each test case, including an explanation of how you have generated these statistics (whether manual, through a lib, or via the IDE)
- provide instructions how to run the test suite
- embed an animated gif or another short video (~1 min) of the test case being ran
