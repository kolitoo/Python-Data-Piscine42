import time

secondes = time.time() #temps en secondes depuis 1970
struct_time = time.gmtime(secondes) #struct pour utiliser a la fin en fonction des secondes
formatted_secondes = "{:,.4f}".format(secondes)
scientificNotation = "{:.2e}".format(secondes)
print("Seconds since January 1, 1970: ", formatted_secondes, " or ", scientificNotation, " in scientific notation")
print(time.strftime("%B %d %Y", struct_time))