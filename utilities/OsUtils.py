import os


class OsUtils:

    @staticmethod
    def get_file_path(path, file_name):
        os.chdir(os.getcwd() + path)
        path = os.getcwd()
        file_path = os.path.join(path, file_name)
        return file_path
