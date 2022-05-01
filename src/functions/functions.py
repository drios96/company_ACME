import os


def read_file(file):
    """
        Function to read file in format txt or csv
        Args:
            file (string): file name
        return: new List with data or empty -> []
    """
    employeeList = []
    if (exist_file(file)) :
        with open(file) as f:
            for line in f:
                line = line.strip()
                line = line.replace(' ', '')
                employeeList.append(line)
        if (len(employeeList) == 0):
            print("File is empty")
            return []
        else :
            return employeeList
    else:
        print("File doesn't exist")
        return employeeList
        
def generate_list(content = []):
    """
        Function to read a list and create new format with dictionaries
        Args:
            file (list): list with data
        return: new List 
    """
    if(len(content) == 0):
        return content
    else :
        new_list = []
        for emp in content:
            employeesFile = emp.split('=')
            employee = employeesFile[0].capitalize()
            schedules = employeesFile[1].split(',')
            dictionary = {'employee':employee,'schedule':schedules}
            new_list.append(dictionary)
        return new_list


def validate_coincidence(new_list = []):
    """
        Function to read the list employees and find coincidences
        Args:
            file (list): employee's list
        return: new List with coincidences
    """
    result = []
    for num,employee in enumerate(new_list):
        for next_employee in new_list[num + 1:]: 
            coincidence = 0
            for schedule in employee['schedule']:
                for schedule2 in next_employee['schedule']:
                    if (schedule == schedule2):
                        coincidence += 1
            if coincidence > 0:
                text = "{emp1} - {emp2} : {value} ".format(emp1 = employee['employee']
                        ,emp2 = next_employee['employee']
                        ,value = coincidence)
                result.append(text)                    
    if len(result) == 0:
        print("No matches")
    return result

def exist_file(file):
    return os.path.exists(file)