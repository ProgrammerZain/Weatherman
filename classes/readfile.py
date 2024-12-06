import os
from datetime import datetime

files_and_dirs = os.listdir('weather_reports')

class ReadFile:


    def __init__(self, type, arg):
        self.type = type
        self.arg = arg
        self.max_temperature = 0
        self.min_temperature = 0
        self.most_humidity = 0
        self.full_date_for_highest = ''
        self.full_date_for_lowest = ''
        self.full_date_for_humidity = ''
        self.readFile()
    
    def readFile(self):
        try:
            files = [file for file in files_and_dirs if os.path.isfile(os.path.join('weather_reports',file)) and self.arg in file]
            
            for file in files:
                with open(f'weather_reports/{file}', 'r') as file_to_read:
                    for i, line in enumerate(file_to_read):
                        if i==0:
                            continue

                        content = line.strip()
                        self.readContent(content)
                       
            self.full_date_for_highest = self.convert_date(self.full_date_for_highest)
            self.full_date_for_lowest = self.convert_date(self.full_date_for_lowest)
            self.full_date_for_humidity = self.convert_date(self.full_date_for_humidity)

            print(f'Highest: {self.max_temperature} on {self.full_date_for_highest}')
            print(f'Lowest: {self.min_temperature} on {self.full_date_for_lowest}')
            print(f'Humidity: {self.most_humidity} on {self.full_date_for_humidity}')
        except FileNotFoundError:
            print(f'File does not exist for {self.arg}')

    def readContent(self,content):
        file_data = content.split(',')
        full_date = file_data[0]
        max_temperature = file_data[1]
        min_temperature = file_data[3]
        most_humidity = file_data[7]
        
        if len(max_temperature) > 0:
            max_temp = int(max_temperature)
            if self.max_temperature < max_temp:
                self.max_temperature = max_temp
                self.full_date_for_highest = full_date

        if len(min_temperature) > 0:
            min_temp = int(min_temperature)
            if self.min_temperature > min_temp:
                self.min_temperature = min_temp
                self.full_date_for_lowest = full_date
        if len(most_humidity) > 0:
            humidity_temp = int(most_humidity)
            if self.most_humidity < humidity_temp:
                self.most_humidity = humidity_temp
                self.full_date_for_humidity = full_date


    def convert_date(self,date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%B %d')
        
