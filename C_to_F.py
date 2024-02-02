def c_to_f(c):
    return (c * 9 / 5) + 32


temp_celsius = [0, 25, 50, 100]
temp_fahrenheit = list(map(c_to_f, temp_celsius))
print(f"Temp C: {temp_celsius}")
print(f"Temp F: {temp_fahrenheit}")
