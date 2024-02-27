
inputFahrenheitString = input(" Enter the temperature in F: ")
tempInF = float(inputFahrenheitString)

tempInC = (tempInF - 32)*(5/9)

print( "The temperature in C is" , tempInC )