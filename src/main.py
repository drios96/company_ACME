from functions.functions import read_file, generate_list, validate_coincidence


def main():
    print("ACME Schedule Comparative")
    option = 0
    file = ""
    while( option < 1 or option > 3):
        print("Files...")
        print("1: data/Employees.txt")
        print("2: data/Employees.csv")
        print("3: Exit")
        try:
            option = int(input("Please select an option to read data: "))
            if option == 1:
                file = "data/Employees.txt"
            elif option == 2:
                file = "data/Employees.csv"   
        except:
            print("That's not a number!") 
    if option != 3:         
        data = read_file(file)
        if (len(data) != 0) :
            data_format = generate_list(data)
            result = validate_coincidence(data_format)
            print(*result, sep = "\n")
            print("These are all coincidences...\nBye")
        else :
            print("Sorry! Your file doesn't have data")
    else :
        print("Bye")

if __name__ == "__main__":
    main()
