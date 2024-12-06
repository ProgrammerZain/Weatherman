from datetime import datetime

class weather_calculate:


    def __init__(self, list_of_weather_data, result, type):
        self.list_of_weather_data = list_of_weather_data
        self.result = result
        self.type = type

        self.max_temperature = 0
        self.min_temperature = 0
        self.most_humidity = 0

        self.max_average_temp = 0
        self.min_average_temp = 0
        self.mean_average_humid = 0

        self.full_date_for_highest_temp = ''
        self.full_date_for_lowest_temp = ''
        self.full_date_for_most_humidity = ''
        
        self.full_date_for_average_temp = ''
        self.full_date_for_average_temp = ''
        self.full_date_for_average_humidity = ''

        self.sum_max_temp = 0
        self.sum_min_temp = 0
        self.sum_humidity_temp = 0        

        self.no_of_max_temp = 0
        self.no_of_min_temp = 0
        self.no_of_humidity_temp = 0        

    def calculate(self):

        if 'e' in self.type:
            self.calculate_task_1()
            self.populate_result()

        elif 'a' in self.type:
            self.calculate_task_2()
            self.populate_result()
            
        elif 'c' in self.type:
            self.calculate_task_3()
        else:
            print('Enter either e, a, or c for the type')


    def calculate_task_1(self):
        for i in self.list_of_weather_data:
            full_date = i['full_date']
            max_temperature = i['max_temperature']
            min_temperature = i['min_temperature']
            most_humidity = i['most_humidity']
            
            if len(max_temperature) > 0:
               max_temp = int(max_temperature)
            if self.max_temperature < max_temp:
                self.max_temperature = max_temp
                self.full_date_for_highest_temp = self.convert_date(full_date)

            if len(min_temperature) > 0:
                min_temp = int(min_temperature)
                if self.min_temperature > min_temp:
                    self.min_temperature = min_temp
                    self.full_date_for_lowest_temp = self.convert_date(full_date)
            if len(most_humidity) > 0:
                humidity_temp = int(most_humidity)
                if self.most_humidity < humidity_temp:
                    self.most_humidity = humidity_temp
                    self.full_date_for_most_humidity = self.convert_date(full_date)

    def calculate_task_2(self):
        for i in self.list_of_weather_data:
            # full_date = i['full_date']
            max_temperature = i['max_temperature']
            min_temperature = i['min_temperature']
            most_humidity = i['mean_humidity']
            
            if len(max_temperature) > 0:
                self.sum_max_temp += int(max_temperature)
                self.no_of_max_temp += 1
            if len(min_temperature) > 0:
                self.sum_min_temp += int(min_temperature)
                self.no_of_min_temp += 1
            if len(most_humidity) > 0:
                self.sum_humidity_temp += int(most_humidity)
                self.no_of_humidity_temp += 1
        

    def calculate_task_3(self):
        pass

    def populate_result(self):
        if 'e' in self.type:
            self.result['max_temperature'] = self.max_temperature
            self.result['min_temperature'] = self.min_temperature
            self.result['most_humidity'] = self.most_humidity
            self.result['full_date_for_highest_temp'] = self.full_date_for_highest_temp
            self.result['full_date_for_lowest_temp'] = self.full_date_for_lowest_temp
            self.result['full_date_for_most_humidity'] = self.full_date_for_most_humidity
        elif 'a' in self.type:
            self.result['sum_max_temp']  =  int(self.sum_max_temp / self.no_of_max_temp)
            self.result['sum_min_temp']  =  int(self.sum_min_temp  / self.no_of_min_temp)
            self.result['sum_humidity_temp']  =  int(self.sum_humidity_temp / self.no_of_humidity_temp)
            
        elif 'c' in self.type:
            self.calculate_task_3()

    def convert_date(self,date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%B %d')