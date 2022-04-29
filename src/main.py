from functions.functions import read_file, generate_list, validate_coincidence


def main():
    print("ACME Schedule Comparation")
    file = input("Enter file name to read data: ")
    while(file == '' or file == ' '):
        print('You must enter file name to read data..')
        file = input("Enter file name to read data: ")
    data = read_file(file)
    data_format = generate_list(data)
    result = validate_coincidence(data_format)
    print(*result, sep = "\n")
    print('These are all coincidences...\nBye')
    


if __name__ == "__main__":
    main()
