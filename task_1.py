numbers  = [ 2 , - 93 , - 2 , 8 , None , - 44 , - 1 , - 85 , - 14 , 90 , - 22 , - 90 , - 100 , - 8 , 38 , - 92 , - 45 , 67 , 53 , 25 ]

# TODO заменить значение пропущенного элемента арифметическим
numbers_without_none  =  numbers [ 0 : 4 ] +  numbers [ 5 :]
average = sum(numbers_without_none) / len(numbers)
numbers[4] = average
print("Измененный список:", numbers)
