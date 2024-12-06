class weather_report:


    def __init__(self, result, type):
        self.result = result
        self.type = type
        pass


    def print(self):
        if 'e' in self.type:
            self.print_task_1()
        elif 'a' in self.type:
            self.print_task_2()
            
        elif 'c' in self.type:
            self.print_task_3()
        
    def print_task_1(self):
        print(f'Highest: {self.result['max_temperature']} on {self.result['full_date_for_highest_temp']}')
        print(f'Lowest: {self.result['min_temperature']} on {self.result['full_date_for_lowest_temp']}')
        print(f'Humidity: {self.result['most_humidity']} on {self.result['full_date_for_most_humidity']}')
        
    def print_task_2(self):
        print(f'Highest Average: {self.result['sum_max_temp']}C')
        print(f'Lowest Average: {self.result['sum_min_temp']}C')
        print(f'Average Mean Humidity: {self.result['sum_humidity_temp']}%')

        
    def print_task_3(self):
        pass
