import json

# print("Started Reading JSON file")
# with open("kanji_data.json", "r") as read_file:
#     print("Converting JSON encoded data into Python dictionary")
#     kanji_dict = json.load(read_file)

#     print("Decoded JSON Data From File")
#     for key, value in kanji_dict.items():
#         print(key, ":", value)
#     print("Done reading json file")

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
    
print(my_data)
