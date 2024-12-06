from utils.customError import CustomError
from classes.readfile import ReadFile

def checkArgs(arg1, arg2):
    obj = {'a':'a','e':'e','c':'c'}
    if '-' in arg1:
        if '-' in arg2:
            raise CustomError('Arguments provided must be -option and a valid date.')
        if 'a' in arg1:
            print('-a', arg2)
        if 'e' in arg1:
            print('-e', arg2)
            obj = ReadFile(obj['e'], arg2)
        if 'c' in arg1:
            print('-c', arg2)