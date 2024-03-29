def read_Userfile(fileName):
    file_name = open(fileName,'r')
    file_contenet = file_name.readlines()
    print(file_contenet)

name = "test.txt"
read_Userfile(name)