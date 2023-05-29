#7 task
import re
def remove_vowels(sentence):
    return re.sub('[aeiouAEIOU]', '', sentence)

print(remove_vowels("hjdshsdhjs sdjhdssd aasasowq wwocsdsd dd FFhguhjjh AASD BBUUBN jhjhoUIs"))
