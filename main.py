#!/usr/sbin/python


import csv
import random
import sys, time

from os import system

import json
import kanji
import news
import google_translate

def read_json(filename):
   with open(filename) as file:
       return(json.load(file))

def import_kanji():
    
    kanji_list=[]
    example_list =[]

    if __name__ == "__main__":
        kanji_data = read_json('kanji_data.json')
       
    
    for idx,val in enumerate(kanji_data):
        del(kanji_data[idx]['kanji']['video'])
        del(kanji_data[idx]['kanji']['strokes'])
        del(kanji_data[idx]['radical'])
        del(kanji_data[idx]['references'])
    
    for idx, val in enumerate(kanji_data):
        temp_jp_ex_list =[]
        temp_eng_ex_list = []
        
        character = kanji_data[idx]['kanji']['character']
        kunyomi = kanji_data[idx]['kanji']['kunyomi']['hiragana']
        onyomi = kanji_data[idx]['kanji']['onyomi']['katakana']
        meaning = kanji_data[idx]['kanji']['meaning']['english']
        #example = kanji_data[idx]['examples'][0]['japanese']
        for ex_idx, ex_val in enumerate(kanji_data[idx]['examples']):
            temp_jp_ex_list.append(kanji_data[idx]['examples'][ex_idx]['japanese'])
            temp_eng_ex_list.append(kanji_data[idx]['examples'][ex_idx]['meaning']['english'])
            
        kanji_list.append(Kanji(character,kunyomi,onyomi,meaning,temp_jp_ex_list,temp_eng_ex_list))
    
        
    # for k in kanji_list:
    #     c= k.get_character()
    #     k= k.get_kunyomi()
    #     o= k.get_onyomi()
    #     m= k.get_meaning()
        
    #     #print(c,k,o,m) 
        
    return kanji_list


def import_news():
    
    news_list=[]
    
    if __name__ == "__main__":
        news_data = read_json('news_data.json')
    
    #print(news_data)
    
    #print(news_data["articles"][1]["description"])
    
    for idx, val in enumerate(news_data):
        author = news_data['articles'][idx]['author']
        title = news_data['articles'][idx]['title']
        publish_date = news_data['articles'][idx]['publishedAt']
        content = news_data['articles'][idx]['description']
        news_list.append(News(author,title,publish_date,content))
        
    # for n in news_list:
    #     a=n.get_author()
    #     t=n.get_title()
    #     pd=n.get_publish_date()
    #     c=n.get_content()
        
    #     #print(a,t,pd,c)
       
        
    return news_list
    
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
    
def import_sentence():
    sentence_dict = read_sentence_csv_file("japanese_sentences")
    sentence_list=[]
    
    for idx,val in enumerate(sentence_dict):
        sentence = sentence_dict[idx]['num']
        sentence_list.append(Sentence(sentence))
        
    return sentence_list
    


        
        

    
            

class Kanji:
    def __init__(self,character,kunyomi,onyomi,meaning,jp_example,eng_example):
        self.character = character
        self.kunyomi = kunyomi
        self.onyomi = onyomi
        self.meaning = meaning
        self.jp_example = jp_example
        self.eng_example = eng_example
        
    def get_character (self):
        return self.character
        
    def get_kunyomi (self):
        return self.kunyomi
    
    def get_onyomi (self):
        return self.onyomi
        
    def get_meaning (self):
        return self.meaning
    
    def get_jp_example (self):
        return self.jp_example
        
    def get_eng_example (self):
        return self.eng_example
    


class News:
    def __init__(self,author,title,publish_date,content):
        self.author = author
        self.title = title
        self.publish_date = publish_date
        self.content = content
        
    def get_author (self):
        return self.author
        
    def get_title (self):
        return self.title
    
    def get_publish_date (self):
        return self.publish_date
        
    def get_content (self):
        return self.content
        

class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
        
    
    def get_sentence (self):
        return self.sentence
        


class Lesson:
    def __init__(self,kanji,max_kanji,news):
        self.kanji = kanji
        self.max_kanji = max_kanji
        self.news = news
        self.kanji_lesson_list = []
        
    def add_kanji (self,kanji):
        if len(self.kanji_lesson_list) < self.max_kanji:
            self.kanji_lesson_list.append(kanji)
            
    def add_sentence (self,sentence):
        pass

    







# EVERYTHING BELOW HERE ARE ALL MENUS WITH THE SAME STRUCTURE, THEY ALL HAVE APPROPRIATE CHOICES, USER INPUT AND INPUT VALIDATION

def kanji_menu(main_kanji_list,count):
    kanji_list = main_kanji_list
    kanji_counter = count
    
    _ = system('clear')
    breadcrumb = "<HOME><KANJI>"
    print(breadcrumb)
    
    print("""

        LEARNING KANJI MENU
        
        R - Reading <<<
        M - Meaning <<<
        E - Examples <<<
        
        N - NEXT KANJI
        P - PREVIOUS KANJI
    
        X - EXIT TO MAIN MENU
        Q - QUIT PROGRAM


        """)
  
    print(main_kanji_list[kanji_counter].get_character())
    
    user_input = ""
    while user_input not in ("N","n","R","r","M","m","E","e","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            kanji_counter +=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(kanji_list,kanji_counter)
            
        elif user_input.upper() =="E":
            kanji_example(kanji_list,kanji_counter)
            
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")
            
            
           


def kanji_reading(main_kanji_list,count):
    kanji_list = main_kanji_list
    kanji_counter = count
    
    _ = system('clear')
    breadcrumb = "<HOME><KANJI><READING>"
    print(breadcrumb)
    
    print("""

        LEARNING KANJI MENU
        
        R - Reading <<<
        M - Meaning <<<
        E - Examples <<<
        
        N - NEXT KANJI
        P - PREVIOUS KANJI
    
        X - EXIT TO MAIN MENU
        Q - QUIT PROGRAM


        """)
  
    print(kanji_list[kanji_counter].get_character())
    print(kanji_list[kanji_counter].get_kunyomi())
    print(kanji_list[kanji_counter].get_onyomi())
    
    user_input = ""
    while user_input not in ("N","n","R","r","M","m","E","e","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            kanji_counter +=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(kanji_list,kanji_counter)
        
        elif user_input.upper() =="E":
            kanji_example(kanji_list,kanji_counter)
            
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")
    
    
    


def kanji_meaning(main_kanji_list,count):
    kanji_list = main_kanji_list
    kanji_counter = count
    
    _ = system('clear')
    breadcrumb = "<HOME><KANJI><MEANING>"
    print(breadcrumb)
    
    print("""

        LEARNING KANJI MENU
        
        R - Reading <<<
        M - Meaning <<<
        E - Examples <<<
        
        N - NEXT KANJI
        P - PREVIOUS KANJI
    
        X - EXIT TO MAIN MENU
        Q - QUIT PROGRAM


        """)
  
    print(kanji_list[kanji_counter].get_character())
    print(kanji_list[kanji_counter].get_meaning())
    
    user_input = ""
    while user_input not in ("N","n","R","r","M","m","E","e","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            kanji_counter +=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(kanji_list,kanji_counter)
            
        elif user_input.upper() =="E":
            kanji_example(kanji_list,kanji_counter)
            
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")
    
    
    
def kanji_example(main_kanji_list,count):
    kanji_list = main_kanji_list
    kanji_counter = count
    
    _ = system('clear')
    breadcrumb = "<HOME><KANJI><EXAMPLES>"
    print(breadcrumb)
    
    print("""

        LEARNING KANJI MENU
        
        R - Reading <<<
        M - Meaning <<<
        E - Examples <<<
        
        N - NEXT KANJI
        P - PREVIOUS KANJI
    
        X - EXIT TO MAIN MENU
        Q - QUIT PROGRAM


        """)
  
    print(kanji_list[kanji_counter].get_character())
    print(kanji_list[kanji_counter].get_jp_example())
    print(kanji_list[kanji_counter].get_eng_example())
    
    
    user_input = ""
    while user_input not in ("N","n","R","r","M","m","E","e","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            kanji_counter +=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(kanji_list,kanji_counter)
            
        elif user_input.upper() =="E":
            kanji_example(kanji_list,kanji_counter)
            
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")
    


        


def sentence_menu(main_sentence_list,count):
    sentence_list = main_sentence_list
    sentence_counter = count
    
    _ = system('clear')
    breadcrumb = "<HOME><SENTENCE>"
    print(breadcrumb)
    
    print("""

        SENTENCE MENU
        
       
        M - Meaning <<<
        
        
        N - NEXT KANJI
        P - PREVIOUS KANJI
    
        X - EXIT TO MAIN MENU
        Q - QUIT PROGRAM


        """)
  
    print(sentence_list[sentence_counter].get_sentence())
    
    
    
    user_input = ""
    while user_input not in ("N","n","M","m","P","p","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            sentence_counter +=1
            sentence_menu(sentence_list,sentence_counter)
        elif user_input.upper() =="P":
            sentence_counter -=1
            sentence_menu(sentence_list,sentence_counter)
        
            
        elif user_input.upper() =="M":
            sentence_meaning(sentence_list,sentence_counter)
            
       
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")
            
            
            
def sentence_meaning(main_sentence_list,count):
    sentence_list = main_sentence_list
    sentence_counter = count
    
    _ = system('clear')
    breadcrumb = "<HOME><SENTENCE>"
    print(breadcrumb)
    
    print("""

        SENTENCE MENU
        
       
        M - Meaning <<<
        
        
        N - NEXT KANJI
        P - PREVIOUS KANJI
    
        X - EXIT TO MAIN MENU
        Q - QUIT PROGRAM


        """)
    current_sentence =sentence_list[sentence_counter].get_sentence()
    print(current_sentence)
    sentence_meaning = google_translate.get_translation(current_sentence)
    print(sentence_meaning)
    
    
    user_input = ""
    while user_input not in ("N","n","M","m","P","p","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            sentence_counter +=1
            sentence_menu(sentence_list,sentence_counter)
        elif user_input.upper() =="P":
            sentence_counter -=1
            sentence_menu(sentence_list,sentence_counter)
        
            
        elif user_input.upper() =="M":
            sentence_meaning(sentence_list,sentence_counter)
            
       
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")            
            
            
            
            
    
def news_menu(main_news_list, count):
    news_list = main_news_list
    news_counter = count
    _ = system('clear')
    print("""

        
        You chose the News Headlines
        
        N - NEXT KANJI
        P - PREVIOUS KANJI
        
    
        X - EXIT TO MAIN MENU

        Q - QUIT PROGRAM
        
        """)
        
    print(news_list[news_counter].get_author())
    print(news_list[news_counter].get_title())
    print(news_list[news_counter].get_content())
    print(news_list[news_counter].get_publish_date())
    
    user_input = ""
    while user_input not in ("N","n","P","p","X","x","Q","q"):
    
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            news_counter +=1
            news_menu(news_list,news_counter)
        elif user_input.upper() =="P":
            news_counter -=1
            news_menu(news_list,news_counter)
            
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")
        


def start():
    
    main_kanji_list = import_kanji()
    main_news_list = import_news()
    main_sentence_list = import_sentence()
    _ = system('clear')
    
    
    
    print("""
Welcome to your Japanese Reader



    K - LEARNING KANJI
    S - Sentences
    N - News Headlines

    Q - QUIT PROGRAM

    """)

    user_input = ""
    while user_input not in ("K","k","S","s","N","n","Q","q"):

  
        user_input = input("Make your choice - ")

        if user_input.upper() == "K":
            kanji_menu(main_kanji_list,0)
        elif user_input.upper() == "S":
            sentence_menu(main_sentence_list,0)
        elif user_input.upper() == "N":
            news_menu(main_news_list,0)
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again")

    


start()
