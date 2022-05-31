"""
a - Append
"""


with open ("Oceany.txt","a", encoding = "UTF-8") as file:
    file.write("\nPółnocny") # w ten sposób dopiszemy Północny linikę poniżej
    file.write("Oceany")  # a za razem w ten sposób dopiszemy do liniki na której zakończyliśmy nasz plik