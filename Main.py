# from ProgramGui import StocksWithNookGUI
import os
import math
import numpy as np

def is_number(s):
    try:
        float(s)  # Try converting to a float
        return True
    except ValueError:
        return False

def CalculateMean(SumOfClosingPrice):
    return SumOfClosingPrice / 618

def CalculateRange(ListOfClosingPrices):
    return max(ListOfClosingPrices) - min(ListOfClosingPrices)

def CalculateVariance(ListOfClosingPrices, SumOfClosingPrices):
    Mean = SumOfClosingPrices / 618
    return sum((x - Mean) ** 2 for x in ListOfClosingPrices) / 618

def CalculateStandardDeviation(ClosingVariance):
    return math.sqrt(ClosingVariance)

def CalculateIQR(ListOfClosingPrices):
    return np.percentile(ListOfClosingPrices, 75) - np.percentile(ListOfClosingPrices, 25)

def main():
    with open('StockData/TotalAMDStockData.csv', 'r') as File:
        AMDClosingPrices = []
        SumOfAMDClosing = 0.0
        
        StockOneContent = File.readlines()

        for DataForDay in StockOneContent:
            Entry = DataForDay.split(",")

            if is_number(Entry[4]):
                AMDClosingPrices.append(float(Entry[4]))
                SumOfAMDClosing += float(Entry[4])

        AMDVariance = CalculateVariance(AMDClosingPrices, SumOfAMDClosing)

        print("-----------------------------------------")
        print("Stock: AMD")
        print("Time Period: January 3, 2023 - June 20, 2025")
        print("-----------------------------------------")
        print(f"Trading Days: 618")
        print(f"Mean: ${CalculateMean(SumOfAMDClosing):.2f}")
        print(f"Range: ${CalculateRange(AMDClosingPrices):.2f}")
        print(f"Variance: ${AMDVariance:.4f}")
        print(f"Standard Deviation: ${CalculateStandardDeviation(AMDVariance):.2f}")
        # print(f"Min: ${close.min():.2f}")
        # print(f"Max: ${close.max():.2f}")
        print(f"IQR: ${CalculateIQR(AMDClosingPrices):.2f} \n")
                      
    with open('StockData/TotalNvidiaStockData.csv', 'r') as File:
        NvidiaClosingPrices = []
        SumOfNvidiaClosing = 0.0
        
        StockTwoContent = File.readlines()

        for DataForDay in StockTwoContent:
            Entry = DataForDay.split(",")

            if is_number(Entry[4]):
                NvidiaClosingPrices.append(float(Entry[4]))
                SumOfNvidiaClosing += float(Entry[4])

        NvidiaVariance = CalculateVariance(NvidiaClosingPrices, SumOfNvidiaClosing)

        print("-----------------------------------------")
        print("Stock: Nvidia")
        print("Time Period: January 3, 2023 - June 20, 2025")
        print("-----------------------------------------")
        print(f"Trading Days: 618")
        print(f"Mean: ${CalculateMean(SumOfNvidiaClosing):.2f}")
        print(f"Range: ${CalculateRange(NvidiaClosingPrices):.2f}")
        print(f"Variance: ${NvidiaVariance:.4f}")
        print(f"Standard Deviation: ${CalculateStandardDeviation(NvidiaVariance):.2f}")
        # print(f"Min: ${close.min():.2f}")
        # print(f"Max: ${close.max():.2f}")
        print(f"IQR: ${CalculateIQR(NvidiaClosingPrices):.2f} \n")


        # StocksWithNook = StocksWithNookGUI(StockOneContent)
        # StocksWithNook.MainProgram.mainloop()

main()