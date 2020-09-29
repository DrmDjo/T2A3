#!/usr/sbin/python


import csv
import random
import sys, time

from os import system

import json
import kanji
import news



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
        

# class Sentence:
#     def __init__(self,sentence,reading,meaning):
#         self.sentence = sentence
#         self.reading = reading
#         self.meaning = meaning


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
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="E":
            kanji_example(main_kanji_list,kanji_counter)
            
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
  
    print(main_kanji_list[kanji_counter].get_character())
    print(main_kanji_list[kanji_counter].get_kunyomi())
    print(main_kanji_list[kanji_counter].get_onyomi())
    
    user_input = ""
    while user_input not in ("N","n","R","r","M","m","E","e","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            kanji_counter +=1
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="E":
            kanji_example(main_kanji_list,kanji_counter)
            
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
  
    print(main_kanji_list[kanji_counter].get_character())
    print(main_kanji_list[kanji_counter].get_meaning())
    
    user_input = ""
    while user_input not in ("N","n","R","r","M","m","E","e","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            kanji_counter +=1
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="E":
            kanji_example(main_kanji_list,kanji_counter)
            
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
  
    print(main_kanji_list[kanji_counter].get_character())
    print(main_kanji_list[kanji_counter].get_jp_example())
    print(main_kanji_list[kanji_counter].get_eng_example())
    
    
    user_input = ""
    while user_input not in ("N","n","R","r","M","m","E","e","X","x","Q","q"):
            
        user_input = input("Make your choice - ")

        if user_input.upper() =="N":
            kanji_counter +=1
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="P":
            kanji_counter -=1
            kanji_menu(main_kanji_list,kanji_counter)
        elif user_input.upper() =="R":
            
            kanji_reading(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="M":
            kanji_meaning(main_kanji_list,kanji_counter)
            
        elif user_input.upper() =="E":
            kanji_example(main_kanji_list,kanji_counter)
            
        elif user_input.upper() == "X":
            start()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again ")
    


        


def sentence_menu():
    _ = system('clear')
    print("""

        
        You chose the Pracice Sentences
        
        The Enthusiast route is here to learn those words, kanji and the rest that is really hard to find in any mainstream book, and not in your usual daily conversation.

        CHOOSE FROM 

        1 - TECHNOLOGY
        2 - ENTERTAINMENT
        3 - BUSINESS
        4 - DIGITAL CREATIVE
        5 - MADE BY HAND
    
        X - EXIT TO MAIN MENU

        Q - QUIT PROGRAM
        
        """)

    # user_input = ""
    # while user_input not in ("1","2","3","4","5","X","x","Q","q"):
    
    #     user_input = input("Make your choice - ")

    #     if user_input == "1":
    #         tech_start()
    #     elif user_input == "2":
    #         entertainment_start()
    #     elif user_input == "3":
    #         biz_start()
    #     elif user_input == "4":
    #         digital_start()
    #     elif user_input == "5":
    #         handmade_start()        
    #     elif user_input.upper() == "X":
    #         start()
    #     elif user_input.upper() == "Q":
    #         sys.exit()
    #     else:
    #         print("Please try again ")
    
def news_menu():
    _ = system('clear')
    print("""

        
        You chose the News Headlines
        
        The Enthusiast route is here to learn those words, kanji and the rest that is really hard to find in any mainstream book, and not in your usual daily conversation.

        CHOOSE FROM 

        1 - TECHNOLOGY
        2 - ENTERTAINMENT
        3 - BUSINESS
        4 - DIGITAL CREATIVE
        5 - MADE BY HAND
    
        X - EXIT TO MAIN MENU

        Q - QUIT PROGRAM
        
        """)

    # user_input = ""
    # while user_input not in ("1","2","3","4","5","X","x","Q","q"):
    
    #     user_input = input("Make your choice - ")

    #     if user_input == "1":
    #         tech_start()
    #     elif user_input == "2":
    #         entertainment_start()
    #     elif user_input == "3":
    #         biz_start()
    #     elif user_input == "4":
    #         digital_start()
    #     elif user_input == "5":
    #         handmade_start()        
    #     elif user_input.upper() == "X":
    #         start()
    #     elif user_input.upper() == "Q":
    #         sys.exit()
    #     else:
    #         print("Please try again ")
        


def start():
    
    main_kanji_list = import_kanji()
    main_news_list = import_news()
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

  
        user_input = input("Make your choice - Press B or R ")

        if user_input.upper() == "K":
            kanji_menu(main_kanji_list,0)
        elif user_input.upper() == "S":
            sentence_menu()
        elif user_input.upper() == "N":
            news_menu()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again")

    


start()
