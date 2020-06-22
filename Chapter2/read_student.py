from filereader import StudentFileReader

def main():
    file_reader = StudentFileReader('file.txt')
    file_reader.open()
    record_list = file_reader.fetchAll()
    print(record_list[0].firstName)

if __name__ == '__main__':
    main()
