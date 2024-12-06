from utils.customError import CustomError

def checkArgs(op, date):
    if '-' in op:
        if '-' in date:
            raise CustomError('Arguments provided must be -option and a valid date.')
    else:
        raise CustomError(f"Argument provided {op} must contain '-' followed by option and a valid date.")