'''
    @Author: Y.Mani Theja
    @Date: 17-07-2024
    @Last Modified by:
    @Last Modified time: 
    @Title : Python program to Convert temperature between Celsius and Fahrenheit.

'''
def temperature_conversion(temperature, scale):

    """
    Convert temperature between Celsius and Fahrenheit.

    Parameters:
        temperature (float): The temperature to convert
        scale (str): The scale to convert to ('C' for Celsius, 'F' for Fahrenheit)

    Returns:
        float: Converted temperature
    """

    if scale.upper() == 'C':
        # Fahrenheit to Celsius
        return (temperature - 32) * 5 / 9
    elif scale.upper() == 'F':
        # Celsius to Fahrenheit
        return (temperature * 9 / 5) + 32
    else:
        return None


if __name__ == "__main__":
    temperature = float(input("Enter temperature: "))
    scale = input("Convert to (C/F): ").strip().upper()
    
    converted_temp = temperature_conversion(temperature, scale)
    
    if converted_temp is not None:
        if scale == 'C':
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif scale == 'F':
            print(f"{temperature}°C is {converted_temp:.2f}°F")
    else:
        print("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")
