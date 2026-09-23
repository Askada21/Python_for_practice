print("IBM 1401 OPERATOR CONSOLE")
print("=========================")

menu = [
    "Card reader check",
    "Payroll batch run",
    "Job time estimate",
    "Core memory calculator",
    "Two-digit date check",
    "GCD (converted from FORTRAN)",
    "Interest table (converted from FORTRAN)",
]

for i in range(1, 8):
    print(i, ".", menu[i - 1])
print("0. Power down")

option = int(input("\n Select: _"))

if option == 1:
    print("Card reader check")

elif option == 2:
    print("Payroll batch run")

elif option == 3:
    print("Job time estimate")

elif option == 4:
    print("Core memory calculator")

elif option == 5:
    print("Two-digit date check")

elif option == 6:
    print("GCD (converted from FORTRAN)")

elif option == 7:
    print("Interest table (converted from FORTRAN)")

elif option == 0:
    print("Power down")

else:
    print("Invalid option")
