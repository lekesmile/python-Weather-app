
try:
   series = input("Give a series of numbers: ")
   sliptSeries = series.split()
   result = list(map(int, sliptSeries))
   print(sliptSeries)
   print(result)
   print(sum(result))
except:
    print("Error: Some entries were not numbers!")
