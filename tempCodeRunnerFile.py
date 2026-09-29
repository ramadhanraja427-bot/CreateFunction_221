import math

def convert_temperature(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return "Unit tidak dikenali, gunakan 'C' atau 'F'"

luas_lingkaran = lambda jari_jari: math.pi * jari_jari ** 2

# Testing
print("25°C ke Fahrenheit:", convert_temperature(25, 'C'))
print("77°F ke Celsius:", convert_temperature(77, 'F'))
print("Luas lingkaran jari-jari 7:", luas_lingkaran(7))