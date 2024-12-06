import sys
from utils.checkArgs import checkArgs
from utils.customError import CustomError
from classes.readfile import ReadFileYear
from classes.readfile import ReadFileMonth
from classes.weather_calculate import weather_calculate
from classes.weather_report import weather_report


weather_folder_name = 'weather_reports'

def main():
    try:
        if len(sys.argv) > 1:
            list_of_operations = sys.argv[1:]
            
            #check if the passed cmd args are valid or not
            for i in range(0, len(list_of_operations), 2):
                checkArgs(list_of_operations[i], list_of_operations[i+1])
            
            list_of_weather_data = []
            calculation_result = {}
            for i in range(0, len(list_of_operations), 2):
                if 'a' in list_of_operations[i]:
                    list_of_weather_data = []
                    obj = ReadFileMonth(weather_folder_name, list_of_operations[i+1])
                    obj.readFile(list_of_weather_data)
                    
                    obj = weather_calculate(list_of_weather_data, calculation_result, list_of_operations[i])
                    obj.calculate()

                    obj = weather_report(calculation_result, list_of_operations[i])
                    obj.print()

                if 'e' in list_of_operations[i]:
                    #read files
                    list_of_weather_data = []
                    obj = ReadFileYear(weather_folder_name,list_of_operations[i+1])
                    obj.readFile(list_of_weather_data)

                    #calculate result base on data
                    obj = weather_calculate(list_of_weather_data, calculation_result, list_of_operations[i])
                    obj.calculate()

                    obj = weather_report(calculation_result, list_of_operations[i])
                    obj.print()
                if 'c' in list_of_operations[i]:
                    print('-c', list_of_operations[i+1])
            
            
                     
        else:
            print("No additional arguments provided.")
    except CustomError as e:
        print(e)
    except Exception as e:
        print(f"Python Exception: {e}")
    

if __name__ == "__main__":
    main()
