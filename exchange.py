# import neccessary libraries like- requests, sys
import sys
import requests

# if user do not enter valid data exit the program by some error message
if len(sys.argv) > 3:
    print("Too many command line arguments.")

if len(sys.argv) == 3:
    ammount = 0
# get a request from a API url
    responce = requests.get("https://v6.exchangerate-api.com/v6/2c712671cf6bc14583e3f7db/latest/USD")
    exchange_rates = responce.json()
    if sys.argv[1] in exchange_rates["conversion_rates"]:
        try:
            ammount = float(sys.argv[2])
        except ValueError:
            sys.exit("Value should be a number")
    else:
        sys.exit("Write valid currency")
# if user gives correct data then print the final output
print(f"{ammount*exchange_rates["conversion_rates"][sys.argv[1]]} {sys.argv[1]}")