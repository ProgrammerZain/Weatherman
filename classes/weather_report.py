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
            while True:
                user_input = input("Would you like to see the result in 1 line: (y/n): ").strip().lower()  
                if user_input == 'y':
                    self.print_task_4()
                    break  
                elif user_input == 'n':
                    self.print_task_3()
                    break  
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")


        else:
            print("Enter either e, a, or c for the type")
        
    def print_task_1(self):
        print(f'Highest: {self.result['max_temperature']} on {self.result['full_date_for_highest_temp']}')
        print(f'Lowest: {self.result['min_temperature']} on {self.result['full_date_for_lowest_temp']}')
        print(f'Humidity: {self.result['most_humidity']} on {self.result['full_date_for_most_humidity']}')
        
    def print_task_2(self):
        print(f'Highest Average: {self.result['sum_max_temp']}C')
        print(f'Lowest Average: {self.result['sum_min_temp']}C')
        print(f'Average Mean Humidity: {self.result['sum_humidity_temp']}%')

        
    def print_task_3(self):
        if isinstance(self.result['result'], list):
            for i in range(len(self.result['result'])):
                max = int(self.result['result'][i]['max_temperature'])
                min = int(self.result['result'][i]['min_temperature'])
                print(i+1, "\033[31m+\033[0m" * max, f'{max}C')
                print(i+1, "\033[34m+\033[0m" * min, f'{min}C')

    def print_task_4(self):
        if isinstance(self.result['result'], list):
            for i in range(len(self.result['result'])):
                max = int(self.result['result'][i]['max_temperature'])
                min = int(self.result['result'][i]['min_temperature'])
                print(i+1, "\033[31m+\033[0m" * max, "\033[34m+\033[0m" * min, f'{min}C  - {max}C')

        
