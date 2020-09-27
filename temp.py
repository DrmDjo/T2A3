import csv
import random
import sys, time

from os import system



# EVERYTHING BELOW HERE ARE ALL MENUS WITH THE SAME STRUCTURE, THEY ALL HAVE APPROPRIATE CHOICES, USER INPUT AND INPUT VALIDATION

def kanji():
    _ = system('clear')
    breadcrumb = "<HOME><KANJI>"
    print(breadcrumb)
    print("""

        You chose the Kanji Only

        *** CURRENT CHOICES ***

        1 - JAPANESE LANGUAGE PROFICIENCY TEST (JLPT) <<< 


       
    
        X - EXIT TO MAIN MENU

        Q - QUIT PROGRAM


        """)

    
    # user_input = ""
    # while user_input not in ("1","2","3","4","5","X","x","Q","q"):
            
    #     user_input = input("Make your choice - ")

    #     if user_input == "1":
    #         jlpt_start()
                            
    #     elif user_input.upper() == "X":
    #         start()
    #     elif user_input.upper() == "Q":
    #         sys.exit()
    #     else:
    #         print("Please try again ")
           


        


def sentence():
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
    
def news():
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
    _ = system('clear')
    
    
    
    print("""
Welcome to your Japanese Reader



    K - Kanji only
    S - Sentences
    N - News Headlines

    Q - QUIT PROGRAM

    """)

    user_input = ""
    while user_input not in ("K","k","S","s","N","n","Q","q"):

  
        user_input = input("Make your choice - Press B or R ")

        if user_input.upper() == "K":
            kanji()
        elif user_input.upper() == "S":
            sentence()
        elif user_input.upper() == "N":
            news()
        elif user_input.upper() == "Q":
            sys.exit()
        else:
            print("Please try again")

    


start()





