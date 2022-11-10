from filesorterFun import *
s = "/CSCI 3329"
p = "TEST"


y = folder_creation(s, p)
#y.create_all_folders()
x = file_moving(s, p)
x.initialize_file_sorting()

#print(x.get_files_from_source())