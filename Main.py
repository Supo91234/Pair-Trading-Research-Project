from ProgramGui import StocksWithNookGUI

def main():
    with open('StockData/Coca-Cola Stocks - Feb.csv', 'r') as file:
        StockOneContent = file.readlines()

        StocksWithNook = StocksWithNookGUI(StockOneContent)
        StocksWithNook.MainProgram.mainloop()
        

        # ADADADADADDAD
        # while True:
        #     num1 = input("Enter your first numer (or 'q' to quit): ")
        #     if num1.lower() == 'q':
        #         print("Closing program...")
        #         break

        #     num2 = input("Enter your first numer (or 'q' to quit): ")
        #     if num2.lower() == 'q':
        #         print("Closing program...")
        #         break

        #     try:
        #         result = float(num1) * float(num2)

        #         equation = f"{num1} * {num2} = {result}"
        #         print(equation)
        #         file.write(equation + "\n")
        #     except ValueError:
        #         print("Invalid input, please enter valid numbers.")

main()