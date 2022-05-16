"""
Zamienia małe litery na początku na duże np karol na Karol
"""
names = {"arkadiusz", "Wioletta", "karol", "bartłomiej", "Jakub", "Ania"}

names = {name.capitalize() for name in names}
print(names)