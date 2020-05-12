from datetime import datetime

#Global Variables

AppName = "acme weather data app"   #App's name
dataList = []
datetimeObj=''
count = 5
sum = 0
sum2 = 0
sum3 = 0

#Functions 

def openFile():
    try:
        filename = input("Give name of the file: " )
        with open(filename, "r") as temps:
           temps.readline()        #skip the first line = header
           for row in temps:
              row = row.strip().replace('"', '').replace('"', '')
              data = row.split(";") 
              dataList.append(data)
              #print(data)
           print("Loaded weather data from", filename[:-4].capitalize() )
        return data
    except OSError:
        print('Error accessing file. Check file name and path and try again.')
        
def print_temperature_line(daymonth, temp): 
    print(daymonth + " ", end="")
    print("   "*(temp+5) + "-", end="")
    print()


def print_temperature_axis():
    print("      ", end="")
    for i in range(-5,16):
        print("{:02d} ".format(i), end="")
    print()

#End of Functions
#**********************************************************
#Loop start
while count > 0:

   print(AppName.upper())
   case1 = "1) Choose weather data file "
   print (case1)
   case2 = "2) See data for selected day"
   print (case2)
   case3 = "3) Calculate average statistics for the data"
   print (case3)
   case4 = "4) Print a scatterplot of the average temperatures"
   print (case4)
   quitCase = "0) Quit program"
   print(quitCase)
   question = input("Choose what to do: ")
   
   
   if question == "0":
       break
   
   elif question == "1":
       openFile()
       print(" ")
    
   
   elif question == "2":
        dateGiven = input("Give a date (dd.mm): ")
        for row in dataList:
            datetimeobject = datetime.strptime(row[0],'%Y-%m-%d')
            newformat = datetimeobject.strftime('%d.%m.%Y')
            
            if dateGiven in newformat[:5]:
                 print("The weather on", dateGiven,"was on average", row[2] ,"centigrade")
                 print("The lowest temperature was", row[3] ,"and the highest temperature was" , row[4])
                 print("There was", row[1] ,"mm rain")        
        print(" ")   
              
   elif question == "3":
       for avg in dataList:
           
            sum += float(avg[2])
            avgTemp = sum/len(dataList)
            
            sum2 +=float(avg[3])
            avgLow = sum2/len(dataList)
             
            sum3 += float(avg[4])
            avgHigh = sum3/len(dataList)
          
       print("The average temperature for the 25 day period was", round(avgTemp, 1))  
       print("The average lowest temperature was", round(avgLow, 1))     
       print("The average highest temperature was", round(avgHigh, 1))
       print(" ")

   elif question == "4":
       for row in dataList:
           temps = round(float(row[2]))
           datetimeobject = datetime.strptime(row[0],'%Y-%m-%d')
           newformat = datetimeobject.strftime('%d.%m.%Y')
           print_temperature_line(newformat[:5], int(temps))
       print_temperature_axis()
       print(" ")
        
       