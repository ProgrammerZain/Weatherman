import os
from utils.customError import CustomError

class ReadFileYear:


    def __init__(self, path, date):
        self.path = path
        self.year = date
              
    
    def readFile(self, list_of_weather_data):
        files_and_dirs = os.listdir(self.path)
        
        files = [file for file in files_and_dirs if os.path.isfile(os.path.join(self.path, file)) and self.year in file]
        if len(files) < 1:
            raise CustomError(f'File does not exist for {self.year}')
        for file in files:
            with open(f'{self.path}/{file}', 'r') as file_to_read:
                for i, line in enumerate(file_to_read):
                    if i==0:
                        continue
                    
                    content = line.strip()
                    list_of_weather_data.append(self.readContent(content))
                    

    def readContent(self,content):
        file_data = content.split(',')
        full_date = file_data[0]
        max_temperature = file_data[1]
        min_temperature = file_data[3]
        most_humidity = file_data[7]

        return {
            'full_date': full_date,
            'max_temperature': max_temperature,
            'min_temperature': min_temperature,
            'most_humidity': most_humidity,
        }
                
        

class ReadFileMonth:


    def __init__(self, path, date):
        self.path = path
        self.year = date.split('/')[0]
        self.month = self.get_month(date)
        self.error = False
    
    def readFile(self, list_of_weather_data):
        if self.error:
            print('program stopped for monthly report')
        else:
            files_and_dirs = os.listdir(self.path)
            
            files = [file for file in files_and_dirs if os.path.isfile(os.path.join(self.path, file)) and self.year in file and self.month in file]
            if len(files) < 1:
                raise CustomError(f'File does not exist for {self.year} year and {self.month} month')
            for file in files:
                with open(f'{self.path}/{file}', 'r') as file_to_read:
                    for i, line in enumerate(file_to_read):
                        if i==0:
                            continue
                        
                        content = line.strip()
                        list_of_weather_data.append(self.readContent(content))
                    

    def readContent(self,content):
        file_data = content.split(',')
        full_date = file_data[0]
        max_temperature = file_data[1]
        min_temperature = file_data[3]        
        mean_humidity = file_data[8]
        return {
            'full_date': full_date,
            'max_temperature': max_temperature,
            'min_temperature': min_temperature,            
            'mean_humidity': mean_humidity
        }


    def get_month(self, num):
        
            if len(num.split('/')) < 2 or num.split('/')[1] == '' :
                self.error = True
                raise CustomError(f'Invalid No number was Provided. For month {self.year}, please provide a number between 1 and 12.')
                
            else:
                num = int(num.split('/')[1])
                # List of months from January to December
                months = [
                    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
                ]
                
                if 1 <= num <= 12:
                    return months[num - 1]  
                else:
                    return (f"Invalid number {num} for month, please provide a number between 1 and 12.")

