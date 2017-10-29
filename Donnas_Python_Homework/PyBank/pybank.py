import os
import csv

filepath = os.path.join('raw_data','budget_data_2.csv')

with open(filepath, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    Total_months = len(list(csvreader))

    data = []
    for row in csvreader:
        date = (row[0])
        revenue = float(row[1])
        data.append([date, revenue]) + 1

    total_revenue = []
    for revenue in csvreader:
        total_revenue += revenue +1
    #print(total_revenue)    
    
    monthly_average = []
    for i in range(len(data) - 1):   
        month_row = data[i]
        this_month = month_row[0]
        month_price = month_row[-1]
        last_month = data[i-1]
        last_price = last_month[-1]
        monthly_average.append((month_price - last_price) / last_price) +1
        #print(monthly_average)
        
    Greatest_increase = 0    
    for j in range(0, len(monthly_average), 1):
        if float(Greatest_increase) < monthly_average[j]:
            Greatest_increase = monthly_average[j]
    #print(Greatest_increase)

    Greatest_decrease = 0    
    for k in range(0, len(monthly_average), 1):
        if float(Greatest_decrease) > monthly_average[j]:
            Greatest_decrease = monthly_average[j]

print("Financial Analysis")
print("================================")
print(f"Total Months: {Total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${monthly_average}")
print(f"Greatest Increase in Revenue: (${Greatest_increase})")
print(f"Greatest Decrease in Revenue: (${Greatest_decrease})")  


text_file = open("budget.txt", "w")

text_file.write("Financial Analysis\n")
text_file.write("================================\n")
text_file.write(f"Total Months: {Total_months}\n")
text_file.write(f"Total Revenue: ${total_revenue}\n")
text_file.write(f"Average Revenue Change: ${monthly_average}\n")
text_file.write(f"Greatest Increase in Revenue: (${Greatest_increase})\n")
text_file.write(f"Greatest Decrease in Revenue: (${Greatest_decrease})\n")       

text_file.close()
