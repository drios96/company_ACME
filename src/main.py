from functions.functions import read_file, generate_list, validate_coincidence


def main():
    print("ACME Schedule Comparation")
    data = read_file('Employees.txt')
    data_format = generate_list(data)
    result = validate_coincidence(data_format)
    print(*result, sep = "\n")
    


if __name__ == "__main__":
    main()
