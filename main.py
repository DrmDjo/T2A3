#!/usr/sbin/python


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

    

def start():
    
    
    main_kanji_list = import_kanji()
    main_news_list = import_news()
    
    print(main_kanji_list[2].get_character())
    print(main_kanji_list[2].get_kunyomi())
    print(main_kanji_list[2].get_onyomi())
    print(main_kanji_list[2].get_jp_example())
    print(main_kanji_list[2].get_eng_example())
    


start()