ACME COMPANY

Goal
The goal for the present project is to obtain a list with schedules coincidences from all your employees.

Project structure
    src
    |
    |->data
    |    |-->Employees.txt
    |    |-->Employees.csv
    |->functions
    |    |-->functions.py
    |->main.py
    |->test_main.py

Libraries
    I used the pytest-7.1.2 library for the unit test

Version language
    Python 3.10.4

How to run
    *) Please, make sure you stay in the src folder before running the project
    *) You can run the project in console with this command
        python main.py
    *) If you need execute tests, insert this command in console
        pytest -v or pytest

How does it work?
    To have the list of matches you need to enter the file name in the console when the project ask for it.
    In the project directory you will find a folder (data) with test files that you can use.
    The system can read a file in "txt" or "csv" format. 
    Please note that the format of the information in the files should be as follows
    
    RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
    ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
    
    Solution explanation
    I used list and dictionaries structures for this project. 
    The lists were used to store the file information, as well as the information resulting from the methods that were responsible for processing the data.
    The dictionaries were used to store the schedules per employee with a unique identifier that would be used to compare the information and find the match.
    The project has 3 functions
        1) read_file()
            This function read a file and put the information in a new list.
                Considerations
                    If the information does not exist, it returns an empty list.
                    If the file is empty, return an empty list,
                    If the file does not exist, it returns an empty list with a message indicating the non-existence of the file
        2) generate_list()
            This function converts the list of data obtained from the file into a new list with a different structure, each employee is assigned a dictionary along with their work schedules.
                Considerations
                    If the received list is empty, it returns an empty list.
        3) validate_coincidence()
            This function processes the information from the previous list and generates a new list with the matches for each employee.
                Considerations
                    If no matches are found, the returned list is empty
    Results
        1) If the file is empty you will receive a message indicating that there is no information.
        2) If the file only has one employee, you will receive a message that there are no matches
        3) If the file only has more than one employee, you will receive a message with the possible matches.
        4) If the file does not exist or you entered the path wrong, you will receive a message that the file does not exist.

Testing
    I did 7 unit tests for the functions.py file.
    Each test had the objective of validating if the information received by each function allowed to obtain data.
    Tests were carried out to verify that when sending an empty list, one would also be obtained based on the aforementioned considerations.
    Tests were carried out to verify if the information could be read from a file and returned in a list.
    Tests were performed to verify if the data processing functions could return empty and non-empty lists.