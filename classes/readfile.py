import os

class ReadFile:


    def __init__(self, path, date):
        self.path = path
        self.date = date
              
    
    def readFile(self, list_of_weather_data):
        files_and_dirs = os.listdir(self.path)
        try:
            files = [file for file in files_and_dirs if os.path.isfile(os.path.join(self.path, file)) and self.date in file]
            
            for file in files:
                with open(f'{self.path}/{file}', 'r') as file_to_read:
                    for i, line in enumerate(file_to_read):
                        if i==0:
                            continue

                        
                        content = line.strip()
                        list_of_weather_data.append(self.readContent(content))
                    
        except FileNotFoundError:
            print(f'File does not exist for {self.date}')

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
            'most_humidity': most_humidity
        }
                
        
