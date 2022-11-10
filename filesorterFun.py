import os
import shutil as st

class folder_creation:
    def __init__(self, source_folder, prefix): # include file_types is we want the user to sort only certain extensions
        #self.names = file_types
        if prefix == "":
            self.prefix = source_folder
        else:
            self.prefix = prefix
        self.source = source_folder
            

    def is_folder_present(self, path):
        return os.path.exists(path)

    def create_folders(self, path):
        #for exts in self.names:
           # path = self.source + '/' + self.prefix + ' ' + exts
        if self.is_folder_present(path) is False:
            os.makedirs(path)


class file_moving:
    def __init__(self, source_folder, prefix): # include file_types is we want the user to sort only certain extensions
        #self.names = file_types
        if prefix == "":
            self.prefix = source_folder
        else:
            self.prefix = prefix
        self.source = source_folder 
        self.folders = folder_creation(self.source, self.prefix)

    def find_extension(self, file_name):
        file, file_extention = os.path.splitext(self.source + '/' + file_name)
        return file_extention

    def get_files_from_source(self):
        obj = os.scandir(self.source)
        files = []
        for entry in obj :
            if entry.is_file():
                files.append(entry.name)
        return files

    def initialize_file_sorting(self):
        #self.folders.create_all_folders()
        for i in self.get_files_from_source():
            ext = self.find_extension(i)
            new_path = self.source +  '/' + self.prefix + ' ' + ext
            if self.folders.is_folder_present(new_path) is False:
                self.folders.create_folders(new_path)
            st.move(self.source + '/' + i, new_path)
