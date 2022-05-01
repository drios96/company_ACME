from functions.functions import read_file, generate_list, validate_coincidence


def main():
    print("ACME Schedule Comparative")
    file = input("Enter file name to read data: ")
    while(file == '' or file == ' '):
        print("You must enter file name to read data..")
        file = input("Enter file name to read data: ")
    data = read_file(file)
    if (len(data) != 0) :
        data_format = generate_list(data)
        result = validate_coincidence(data_format)
        print(*result, sep = "\n")
        print("These are all coincidences...\nBye")
    else :
        print("Sorry! Your file doesn't have data")


if __name__ == "__main__":
    main()
