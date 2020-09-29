#!/usr/sbin/python


import json


def read_json(filename):
   with open(filename) as file:
       return(json.load(file))

def import_kanji():
    
    kanji_list=[]

    if __name__ == "__main__":
        kanji_data = read_json('kanji_data.json')
       
    
    example_dict = {}
    
    for idx,val in enumerate(kanji_data):
        del(kanji_data[idx]['kanji']['video'])
        del(kanji_data[idx]['kanji']['strokes'])
        del(kanji_data[idx]['radical'])
        example_dict[idx]= kanji_data[idx]['examples']
        del(kanji_data[idx]['examples'])
        del(kanji_data[idx]['references'])
    
    for idx, val in enumerate(kanji_data):
        character = kanji_data[idx]['kanji']['character']
        kunyomi = kanji_data[idx]['kanji']['kunyomi']
        onyomi = kanji_data[idx]['kanji']['onyomi']
        meaning = kanji_data[idx]['kanji']['meaning']
        kanji_list.append(Kanji(character,kunyomi,onyomi,meaning))
    
        
    for k in kanji_list:
        c= k.get_character()
        k= k.get_kunyomi()
        o= k.get_onyomi()
        m= k.get_meaning()
        
        print(c,k,o,m)    


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
        
    for n in news_list:
        a=n.get_author()
        t=n.get_title()
        pd=n.get_publish_date()
        c=n.get_content()
        
        print(a,t,pd,c)
       
        
    

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
        




#import_kanji()
import_news()
    





