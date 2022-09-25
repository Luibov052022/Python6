# Задача 41: Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

import re
string = '5*3+6*3/2-10'

  
def Counting(string):
    numbers_str = re.findall(r'\d+', string)
    numbers = [int(i) for i in numbers_str]
    expr = re.findall(r'[+, --, /, *]', string)
    resault = 0
      
    for i, item in enumerate(expr): 
        if item == '*':
                resault += numbers[i] * numbers[i+1]
                numbers.insert((i+1), resault)
                numbers.remove(numbers[i])
                numbers.remove(numbers[i+1])
                expr.remove(item)
                resault = 0
                
    for i, item in enumerate(expr):
        if item == '/':
                resault += numbers[i] / numbers[i+1]
                numbers.insert((i+1), resault)
                numbers.remove(numbers[i])
                numbers.remove(numbers[i+1])
                expr.remove(item)
                resault = 0
    for i, item in enumerate(expr):            
        if item == '+':
                resault += numbers[i] + numbers[i+1]
                numbers.insert((i+1), resault)
                numbers.remove(numbers[i])
                numbers.remove(numbers[i+1])
                expr.remove(item)
                resault = 0
    for i, item in enumerate(expr):            
        if item == '-':
                resault += numbers[i] - numbers[i+1]
                numbers.insert((i+1), resault)
                numbers.remove(numbers[i])
                numbers.remove(numbers[i+1])
                expr.remove(item)
                resault = 0
    answer = numbers[0]
    return answer    
    
print(f'{string} = {Counting(string)}')
print(eval(string))