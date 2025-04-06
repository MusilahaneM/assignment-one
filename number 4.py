temps_celsius = [0, 10, 20, 30, 40, 100]

temps_fahrenheit = list(map(lambda c: c * 9/5 + 32, temps_celsius))
print("Celsius temperatures:", temps_celsius)
print("Fahrenheit temperatures:", temps_fahrenheit)


