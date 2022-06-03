


def OpenFile(File):
        try:
            with open(File, "r", encoding='UTF-8') as ReadFile:
                return ReadFile.read()
        except FileNotFoundError:
            print("Nie znaleziono pliku")


FileName = input("Podaj nazwę pliku: ")
print(OpenFile(FileName))

