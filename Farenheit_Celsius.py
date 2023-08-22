def print_temp_in_Farenheit(temp_in_Celsius):
    temp_in_Farenheit = int(temp_in_Celsius) * 1.8 + 32
    print("The temperature in Farenheit is " + str(int(temp_in_Farenheit)) + " degrees.")

temperature = input("Enter the temperature in Celsius: ")
temp_in_C = print_temp_in_Farenheit(temperature)

again = input("Do you wish to convert another temperature? y/n ")
while again == "y":
    temperature = input("Enter the temperature in Celsius: ")
    temp_in_C = print_temp_in_Farenheit(temperature)
    again = input("Do you wish to convert another temperature? y/n ")
if again == "n":
    print("Maybe it's time to learn metric, my friend. ")

    



