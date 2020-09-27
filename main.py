#!/usr/sbin/python


import json


def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

if __name__ == "__main__":
    my_data = js_r('kanji_data.json')
    #print(my_data)
example_dict = {}
    
for idx,val in enumerate(my_data):
    del(my_data[idx]['kanji']['video'])
    del(my_data[idx]['kanji']['strokes'])
    del(my_data[idx]['radical'])
    example_dict[idx]= my_data[idx]['examples']
    del(my_data[idx]['examples'])
    del(my_data[idx]['references'])
    
#print(my_data)



class Lesson:
    def __init__(self,kanji,max_kanji,sentence):
        self.kanji = kanji
        self.max_kanji = max_kanji
        self.sentence = sentence
        self.kanji_lesson_list = []
        
    def add_kanji (self,kanji):
        if len(self.kanji_lesson_list) < self.max_kanji:
            self.kanji_lesson_list.append(kanji)
            
    def add_sentence (self,sentence):
        pass
    
kanji_list=[]            

class Kanji:
    def __init__(self,character,kunyomi,onyomi,meaning):
        self.character = character
        self.kunyomi = kunyomi
        self.onyomi = onyomi
        self.meaning = meaning
        
    def get_character (self):
        return self.character
        
    def get_kunyomi (self):
        return self.kunyomi
    
    def get_onyomi (self):
        return self.onyomi
        
    def get_meaning (self):
        return self.meaning
    
class Sentence:
    def __init__(self,sentence,reading,meaning):
        self.sentence = sentence
        self.reading = reading
        self.meaning = meaning



for idx, val in enumerate(my_data):
    character = my_data[idx]['kanji']['character']
    kunyomi = my_data[idx]['kanji']['kunyomi']
    onyomi = my_data[idx]['kanji']['onyomi']
    meaning = my_data[idx]['kanji']['meaning']
    kanji_list.append(Kanji(character,kunyomi,onyomi,meaning))
    
    
for k in kanji_list:
    a= k.get_character()
    b= k.get_kunyomi()
    c= k.get_onyomi()
    d= k.get_meaning()
    
    print(a,b,c,d)
    
    





