import sys
from utils.checkArgs import checkArgs
from utils.customError import CustomError
def main():
    try:
        if len(sys.argv) > 1:
            all_args = sys.argv[1:]
            print(len(all_args))
            
            for i in range(0, len(all_args), 2):
                checkArgs(all_args[i], all_args[i+1])
            print("Arguments:", all_args)
        else:
            print("No additional arguments provided.")
    except CustomError as e:
        print(e)
    except Exception as e:
        print(f"Python Exception: {e}")
    

if __name__ == "__main__":
    main()
