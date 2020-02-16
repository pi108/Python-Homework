#==========================================================================================================
# This block of logic imports the relevant Python Modules
#==========================================================================================================

import os 
import csv

import collections
import operator 
# from collections import OrderedDict
# from operator import itemgetter



#==========================================================================================================
# This block of logic create a Variable for the CSV File to be read
#==========================================================================================================

my_csv_read_from_file = os.path.join('C:/Users/firdo/Desktop/CSV_TEST','HW3_Python_budget_data.csv')



#==========================================================================================================
# This block of logic defines the variables to be used in the analysis
#==========================================================================================================

my_current_row_month = 0
my_total_months = 0

my_total_pnl_yest = 0
my_total_pnl_today = 0

my_monthly_pnl_today = 0
my_monthly_pnl_yest = 0
my_monthly_pnl_change_today = 0

my_total_monthly_pnl_change_yest = 0
my_total_monthly_pnl_change_today = 0
my_average_monthly_pnl_change = 0

my_greatest_increase_in_profits = 0
my_greatest_decrease_in_profits = 0
my_month_with_greatest_increase_in_profits = 0
my_month_with_greatest_decrease_in_profits = 0



#==========================================================================================================
# This block of logic does 3 things:
# 1. It uses the preferred and improved method of opening CSV files by using "with open" instead of just open 
# 2. It ensures that rows with bad unreadable characters will not be skipped by specifying "encoding="utf8" 
# 3. It reads the CSV file into a Dictionary by using csv.DictReader isntead of just csv.Reader
#==========================================================================================================

with open(my_csv_read_from_file, encoding="utf8", newline='') as budget_data:
    my_csv_reader = csv.DictReader(budget_data, delimiter=',')



#==========================================================================================================
# This block of logic does 6 things:
# 1. It identifies the current row of the csv reader that the loop is on in a variable called my_current_row_month
# 2. It calculates the Total number of Months
# 3. It calculates the Total Profit/Loss for all the months
# 4. It calculates the Average Change in the Profit/Loss from one month to the next
# 5. It calculates the Greatest Increase in the Profit/Loss from one month to the next and identifies the Month
# 6. It calculates the Greatest Decrease in the Profit/Loss from one month to the next and identifies the Month
#==========================================================================================================

    for row in my_csv_reader:
        
        my_current_row_month = row["Date"]    
        my_total_months = int(my_total_months) + 1

        if int(my_total_pnl_today) != 0: 
            my_total_pnl_yest = int(my_total_pnl_today) 
            my_total_pnl_today = int(my_total_pnl_today) + int(row["Profit/Losses"]) 
            my_monthly_pnl_yest = my_monthly_pnl_today
            my_monthly_pnl_today = int(row["Profit/Losses"])
            my_monthly_pnl_change_today = my_monthly_pnl_today - int(my_monthly_pnl_yest)
            my_total_monthly_pnl_change_yest = int(my_total_monthly_pnl_change_today)
            my_total_monthly_pnl_change_today = int(my_monthly_pnl_change_today) + int(my_total_monthly_pnl_change_yest)
            my_average_monthly_pnl_change = int ( int(my_total_monthly_pnl_change_today) / (int(my_total_months - int(1))) )
        else:
            my_total_pnl_today = int(row["Profit/Losses"]) 
            my_monthly_pnl_today = int(row["Profit/Losses"])


        if int(my_monthly_pnl_change_today) > int(my_greatest_increase_in_profits): 
            my_greatest_increase_in_profits = my_monthly_pnl_change_today
            my_month_with_greatest_increase_in_profits = row["Date"]  


        if int(my_monthly_pnl_change_today) < int(my_greatest_decrease_in_profits): 
            my_greatest_decrease_in_profits = my_monthly_pnl_change_today
            my_month_with_greatest_decrease_in_profits = row["Date"] 


           
        

    
#===========================================================================================================
# This block of logic prints the results of the analysis to the Terminal
#===========================================================================================================
  
 
    print()
    print()
    print()
    print("--------------------------------------------------------")
    print("Financial Analysis")
    print("--------------------------------------------------------")
    print("Total Months: " + str('{:,}'.format(my_total_months)))
    print("Total Profit/Loss: " + str('${:,}'.format(my_total_pnl_today)))
    print("Average Change: " + str('${:,}'.format(my_average_monthly_pnl_change)))
    print("Greatest Increase in Profits: " + my_month_with_greatest_increase_in_profits + " : " + str('${:,}'.format(my_greatest_increase_in_profits)))
    print("Greatest Decrease in Profits: " + my_month_with_greatest_decrease_in_profits + " : " + str('${:,}'.format(my_greatest_decrease_in_profits)))
    print("--------------------------------------------------------")


  
#===========================================================================================================
# This block of logic writes the output to a CSV file:
#===========================================================================================================
  

output_file = os.path.join('C:/Users/firdo/Desktop/CSV_TEST', 'budget_data_analysis_output.csv')
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile) 
    writer.writerow(["Total Months", "Total Profit/Loss", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"])
    writer.writerow(["","","",my_month_with_greatest_increase_in_profits,my_month_with_greatest_decrease_in_profits])
    writer.writerow([my_total_months,my_total_pnl_today,my_average_monthly_pnl_change,my_greatest_increase_in_profits,my_greatest_decrease_in_profits])



#===========================================================================================================
# This block of logic writes the output to a TXT file:
#===========================================================================================================
  

output_file = os.path.join('C:/Users/firdo/Desktop/CSV_TEST', 'budget_data_analysis_output.txt')

with open(output_file, "w") as datafile:
    datafile.write("--------------------------------------------------------")
    datafile.write("\n")
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("--------------------------------------------------------")
    datafile.write("\n")
    datafile.write("Total Months: " + str('{:,}'.format(my_total_months)))
    datafile.write("\n")
    datafile.write("Total Profit/Loss: " + str('${:,}'.format(my_total_pnl_today)))
    datafile.write("\n")
    datafile.write("Average Change: " + str('${:,}'.format(my_average_monthly_pnl_change)))
    datafile.write("\n")
    datafile.write("Greatest Increase in Profits: " + my_month_with_greatest_increase_in_profits + " : " + str('${:,}'.format(my_greatest_increase_in_profits)))
    datafile.write("\n")
    datafile.write("Greatest Decrease in Profits: " + my_month_with_greatest_decrease_in_profits + " : " + str('${:,}'.format(my_greatest_decrease_in_profits)))

