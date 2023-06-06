import re
import json
import string
import unicodedata


def delete_rubbish(text):
    text = text.replace(". . .", "")
    text = text.replace("..", "")
    text = text.replace(". .", "")
    text = text.encode("ascii", "ignore")
    text = text.decode()
    return text


def delete_punctuation(text):
    punctuation = r"""!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"""
    text = text.translate(str.maketrans('', '', punctuation))
    return text


def delete_word_with_number(text):
    stext = re.sub(r'\b\w*\d\w*\b', '', text)
    return text


def delete_white_space(text):
    text = text.replace("   ", "")
    text = text.replace("     ", "")
    text = text.rstrip()
    text = text.lstrip()
    return text


def delete_final(text):
    text = text.replace(".     ...", '')
    text = text.replace("\n", '')
    text = text.replace(" .", ".")
    text = text.replace(". ", ".")
    return text


f = open("./../../data/raw/raw.json", "r")
data = json.load(f)
f.close()

new_data = dict()
new_data['crime'] = []
new_data['romance'] = []
new_data['psychology'] = []
x = 0

#print(len(data['romance']))
clean_summery = None
for summery in data['crime']:
    if summery != "":
        clean_summery = delete_final(delete_white_space(delete_rubbish(delete_punctuation(delete_word_with_number(summery)))))
    if clean_summery is not None:
        if clean_summery != '':
            new_data['crime'].append(clean_summery)
            clean_summery = None

clean_summery = None
for summery in data['romance']:
    if summery != "":
        clean_summery = delete_final(delete_white_space(delete_rubbish(delete_punctuation(delete_word_with_number(summery)))))
    if clean_summery is not None:
        if clean_summery != '':
            new_data['romance'].append(clean_summery)
            clean_summery = None

clean_summery = None
for summery in data['psychology']:
    if summery != "":
        clean_summery = delete_final(delete_white_space(delete_rubbish(delete_punctuation(delete_word_with_number(summery)))))
        x+=1
    if clean_summery is not None:
        if clean_summery != '':
            new_data['psychology'].append(clean_summery)
            clean_summery = None

#print(len(new_data['crime']))
#print(x)
length = min(len(new_data['crime']), len(new_data['romance']), len(new_data['psychology']))
new_data['crime'] = new_data['crime'][0:length]
new_data['romance'] = new_data['romance'][0:length]
new_data['psychology'] = new_data['psychology'][0:length]


f = open("./../../data/clean/clean.json", "w")
json.dump(new_data, f)
f.close()



