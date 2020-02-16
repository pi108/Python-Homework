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

my_csv_read_from_file = os.path.join('C:/Users/firdo/Desktop/CSV_TEST','HW3_Python_houston_election_data.csv')




#==========================================================================================================
# This block of logic defines the variables to be used in the analysis
#==========================================================================================================

my_current_row_candidate = 0
my_candidate_list = []
my_candidate_votes = {}

my_final_results = {}
my_total_votes_final_results = 0

my_candidate_name_final_results = ()
my_candidate_votecount_final_results = ()
my_candidate_percentage_final_results = ()
my_combined_final_results = ()



#==========================================================================================================
# This block of logic does 3 things:
# 1. It uses the preferred and improved method of opening CSV files by using "with open" instead of just open 
# 2. It ensures that rows with bad unreadable characters will not be skipped by specifying "encoding="utf8" 
# 3. It reads the CSV file into a Dictionary by using csv.DictReader isntead of just csv.Reader
#==========================================================================================================

with open(my_csv_read_from_file, encoding="utf8", newline='') as election_data:
    my_csv_reader = csv.DictReader(election_data, delimiter=',')




#==========================================================================================================
# This block of logic does 3 things:
# 1. It identifies the current row of the csv reader that the loop is on in a variable called my_current_row_candidate
# 2. It creates the list of all candidates in the LIST called my_candidate_list
# 3. It calculates for each distinct Candidate (KEY): the Total Votes (VALUE) in the DICTIONARY called my_candidate_votes
#==========================================================================================================

    for row in my_csv_reader:
        
        my_current_row_candidate = row["Candidate"]        
       
        if row["Candidate"] not in my_candidate_list:
            
            my_candidate_list.append(row["Candidate"])

            my_candidate_votes[row["Candidate"]] = 1
            
        else:
            my_candidate_votes[row["Candidate"]] = my_candidate_votes[row["Candidate"]] + 1

            my_candidate_list.sort()
           
       

#==========================================================================================================
# This block of logic does 6 things:
# 1. It creates a new DICTIONARY called final_results which sorts based on the Total Votes (VALUE) from my_candidate_votes 
# 2. It then calculates the Total Votes cast for all candidates
# 3. It cretaes a new list just with the Candidate Names (sorted based on Total Vote Count).
# 4. It creates a new list just with the Total Vote Count (sorted based on Total Vote Count).
# 5. It craetes a new list just with the Percentage of the Total Vote Cpount (sorted based on Total Vote Count).
# 6. It then combines the 3 lists mentioned above into one combined list using the zip feature. 
#===========================================================================================================

    my_final_results = sorted(my_candidate_votes.items(), key=operator.itemgetter(1),reverse=True)

    for x in my_final_results:
        my_total_votes_final_results += x[1]
    

    my_candidate_name_final_results = [n[0] for n in my_final_results] 

    my_candidate_votecount_final_results = [v[1] for v in my_final_results] 

    my_candidate_percentage_final_results = [y[1]/my_total_votes_final_results for y in my_final_results] 

    my_combined_final_results = zip(my_candidate_name_final_results,my_candidate_votecount_final_results,my_candidate_percentage_final_results)


#===========================================================================================================
# This block of logic prints the results of the analysis to the Terminal
#===========================================================================================================
  
 
    print()
    print()
    print()
    print("--------------------------------------------------------")
    print("Houston Mayoral Election Results")
    print("--------------------------------------------------------")
    print("Total Cast Votes: " + str('{:,}'.format(my_total_votes_final_results)))
    print("--------------------------------------------------------")

    for r in my_combined_final_results:
        print(str(r[0]) + " : " + str('{0:.2%}'.format(r[2])) + "  (" + str('{:,}'.format(r[1])) + ")" )
    
    print("--------------------------------------------------------")

       
    print ("1st Advancing Candidate: " + str(my_candidate_name_final_results[0]) + "\n" "2nd Advancing Candidate: "+ str(my_candidate_name_final_results[1])) 

    print("--------------------------------------------------------")




#===========================================================================================================
# This block of logic does 3 things to write the output to a CSV File:
# 1. It re-zips 3 lists into the combined list. 
# For some reason when the original zipped list was printed, it was no longer available to be used.
# 2. It creates a variable for the output CSV File
# 3. It reads from the re-zipped list and writes to the output CSV file.
#===========================================================================================================
  

my_combined_final_results = zip(my_candidate_name_final_results,my_candidate_votecount_final_results,my_candidate_percentage_final_results)


output_file = os.path.join('C:/Users/firdo/Desktop/CSV_TEST', 'election_data_analysis_output.csv')
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile) 
    writer.writerow(["Candidate Name", "Total Votes Received", "Percentage of Votes Received"])
    writer.writerows(my_combined_final_results)




#===========================================================================================================
# This block of logic writes the output to a TXT file:
#===========================================================================================================
  
my_combined_final_results = zip(my_candidate_name_final_results,my_candidate_votecount_final_results,my_candidate_percentage_final_results)

output_file = os.path.join('C:/Users/firdo/Desktop/CSV_TEST', 'election_data_analysis_output.txt')

with open(output_file, "w") as datafile:
    datafile.write("--------------------------------------------------------")
    datafile.write("\n")
    datafile.write("Houston Mayoral Election Results")
    datafile.write("\n")
    datafile.write("--------------------------------------------------------")
    datafile.write("\n")
    datafile.write("Total Cast Votes: " + str('{:,}'.format(my_total_votes_final_results)))
    datafile.write("\n")    
    datafile.write("--------------------------------------------------------")
    datafile.write("\n")  
    for r in my_combined_final_results:
        datafile.write((str(r[0]) + " : " + str('{0:.2%}'.format(r[2])) + "  (" + str('{:,}'.format(r[1])) + ")" ))
        datafile.write("\n")  
    
    


