import os

logo = """██████╗░░█████╗░██╗░░░░░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗
██████╔╝██║░░██║██║░░░░░███████║
██╔═══╝░██║░░██║██║░░░░░██╔══██║
██║░░░░░╚█████╔╝███████╗██║░░██║
╚═╝░░░░░░╚════╝░╚══════╝╚═╝░░╚═╝
"""

def console(comment=None):
  if comment:
    i = input(f"[{comment}] pola~$ ")
  else:
    i = input("pola~$ ")
  return i

def obliczPola():
  os.system("clear")
  print("~ Oblicz pole")
  print("1. Kwadrat")
  print("2. Prostokąt")
  print("3. Romb")
  print("4. Trapez")
  print("5. Równoległobok")
  print("6. Trójkąt")
  print("7. Wróć")
  i = console("Podaj numer opcji")
  if i == "1":
    os.system("clear")
    print(" ----------")
    print("|          |")
    print("| a        |")
    print("|          |")
    print("|    a     |")
    print(" ----------\n")
    a = int(console("Podaj a"))
    P = a * a
    print(f"Pole = {P}")
    input("Naciśnij ENTER aby powrócić...")
    obliczPola()
  elif i == "2":
    os.system("clear")
    print(" --------------------")
    print("|                    |")
    print("| b                  |")
    print("|                    |")
    print("|         a          |")
    print(" --------------------\n")
    a = int(console("Podaj a"))
    b = int(console("Podaj b"))
    P = a * b
    print(f"Pole = {P}")
    input("Naciśnij ENTER aby powrócić...")
    obliczPola()
  elif i == "3":
    os.system("clear")
    print("   /\\")
    print("  / |\\")
    print(" /  | \\")
    print("/   |d1\\")
    print("\\------/")
    print(" \\d2| /")
    print("  \\ |/" )
    print("   \\/\n")
    d1 = int(console("Podaj d1"))
    d2 = int(console("Podaj d2"))
    P = (d1 * d2) / 2
    print(f"Pole = {P}")
    input("Naciśnij ENTER aby powrócić...")
    obliczPola()
  elif i == "4":
    os.system("clear")
    print(" --------------------")
    print(" \    b        |     /")
    print("  \            | h  /")
    print("   \           |   /")
    print("    \    a     |  /")
    print("     ------------- \n")
    a = int(console("Podaj a"))
    b = int(console("Podaj b"))
    h = int(console("Podaj h"))
    P = ((a + b) * h) / 2
    print(f"Pole = {P}")
    input("Naciśnij ENTER aby powrócić...")
    obliczPola()
  elif i == "5":
    os.system("clear")
    print("      /------------/")
    print("     /  |         /")
    print("    /   |        /")
    print("   /    | h     /")
    print("  /     |      /")
    print(" /      |     /")
    print("/____________/")
    print("      a\n")
    a = int(console("Podaj a"))
    h = int(console("Podaj h"))
    P = a * h
    print(f"Pole = {P}")
    input("Naciśnij ENTER aby powrócić...")
    obliczPola()
  elif i == "6":
    os.system("clear")
    print("    /\\")
    print("   / |\\")
    print("  /  | \\")
    print(" / h |  \\")
    print("/    |   \\")
    print("----------")
    print("      a\n")
    a = int(console("Podaj a"))
    h = int(console("Podaj h"))
    P = (a / 2) * h
    print(f"Pole = {P}")
    input("Naciśnij ENTER aby powrócić...")
    obliczPola()
  elif i == "7":
    menu()
  else:
    obliczPola()

def info():
  os.system("clear")
  print("~ Informacje")
  print("Autor: Jan Mi###### 6C")
  print("Data: 15.01.2022")
  print("Pełna Nazwa: Obliczanie pól POLA")
  print("Licencja: Apache License 2.0")
  print("Kod źródłowy: ")

def menu():
  os.system("clear")
  print(logo)
  print("~ Wybież opcję")
  print("1. Oblicz pole")
  print("2. Informacje")
  print("3. Wyjdź\n")
  i = console("Podaj numer opcji")
  if i == "1":
    obliczPola()
  elif i == "2":
    info()
  elif i == "3":
    exit()
  else:
    menu()

menu()
