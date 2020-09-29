#!/usr/sbin/python


import csv




#Generic Re useable READ KANJI function which will read in the relevant information and create a dictionary with the appropriate keys
def read_sentence_csv_file(file_name):
    temp_file = file_name
    temp_dict = {}
    try:
        with open(f"{temp_file}.csv", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0



            for row,val in enumerate(csv_reader):
                
                temp_dict[row]= val

                line_count += 1
        #print(f"Processed {line_count} kanji.")
        return temp_dict

    except FileNotFoundError:
        print("This file does not exist")
        
        
sentence_dict = read_sentence_csv_file("japanese_sentences")
        


