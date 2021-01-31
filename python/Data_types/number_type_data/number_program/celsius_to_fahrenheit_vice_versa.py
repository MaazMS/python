class CelsiusFahrenheitConveraio:

    def convert_celsius_to_fahrenheit(self):

        celsius = float (input("Enter celsius"))
        fahrenheit = celsius * 1.8 + 32
        print(' celsius to fahrenheit',celsius , "           " ,  fahrenheit)


    def convert_fahrenheit_to_celsius(self):

        fahrenheit = float (input("Enter fahrenheit"))
        celsius = fahrenheit - 32 / 1.8
        print(' celsius to fahrenheit',celsius , "           " ,  fahrenheit)

obj = CelsiusFahrenheitConveraio()
obj.convert_celsius_to_fahrenheit()
obj.convert_fahrenheit_to_celsius()