import json
import csv
cnt = 0

f = open("./../data/raw/raw.json", "r")
before_data = json.load(f)
f.close()
f = open("./../data/clean/clean.json", "r")
after_data = json.load(f)
f.close()
f = open("./../data/sentencebroken/sentencebroken.json", "r")
snt_broken = json.load(f)
f.close()
f = open("./../data/wordbroken/wordbroken.json", "r")
word_broken = json.load(f)
f.close()


table_csv = []

# before = 0
# after = 0

# before = len(before_data['crime']) + len(before_data['romance']) + len(before_data['psychology'])
# after = len(after_data['crime']) + len(after_data['romance']) + len(after_data['psychology'])

# print("all data:")
# print(before)
# print(after)
table_csv.append(['' , 'crime' , 'romance' , 'psychology'])
print("number of summeries raw data:")
print(len(before_data['crime']))
print(len(before_data['romance']))
print(len(before_data['psychology']))
table_csv.append(['number of summeries raw data:',len(before_data['crime']) , len(before_data['romance']) , len(before_data['psychology'])])

print("number of summeries clean data:")
print(len(after_data['crime']))
print(len(after_data['romance']))
print(len(after_data['psychology']))
table_csv.append(['number of summeries clean data',len(after_data['crime']) , len(after_data['romance']) , len(after_data['psychology'])])


c = 0
r = 0
p = 0
for i in snt_broken:
    #print(i)
    if snt_broken[i]["genre"] == "crime":
        c += len(snt_broken[i]['sent_broken'])
    elif snt_broken[i]['genre'] == "romance":
        r += len(snt_broken[i]['sent_broken'])
    else:
        p += len(snt_broken[i]['sent_broken'])
print("number of sentences:")
print(c)
print(r)
print(p)
table_csv.append(['number of sentences',c, r, p])



c = 0
r = 0
p = 0
for i in word_broken:
    if word_broken[i]['genre'] == "crime":
        c += len(word_broken[i]['word_broken'])
    elif word_broken[i]['genre'] == "romance":
        r += len(word_broken[i]['word_broken'])
    else:
        p += len(word_broken[i]['word_broken'])
print("number of words:")
print(c)
print(r)
print(p)
table_csv.append(['number of words',c, r, p])

c = set()
r = set()
p = set()
for i in word_broken:
    if word_broken[i]['genre'] == "crime":
        c.update(word_broken[i]['word_broken'])
    elif word_broken[i]['genre'] == "romance":
        r.update(word_broken[i]['word_broken'])
    else:
        p.update(word_broken[i]['word_broken'])

print("number of unique words:")
print(len(c))
print(len(r))
print(len(p))
table_csv.append(['number of unique words' , len(c), len(r), len(p)])

cr = set()
rp = set()
pc = set()

for w in c:
    if w in r:
        cr.update(w)
    if w in p:
        pc.update(w)
for w in r:
    if w in p:
        rp.update(w)
table_csv2 = []
table_csv2.append(['','number'])
print("number of unique common words of romance and crime:")
print(len(cr))
print("number of unique common words of romance and psychology:")
print(len(rp))
print("number of unique common words of sychology and crime:")
print(len(pc))
table_csv2.append(['number of unique common words of romance and crime' , len(cr)])
table_csv2.append(['number of unique common words of romance and psychology', len(rp)])
table_csv2.append(['number of unique common words of sychology and crime' ,len(pc)])


print("number of unique uncommon words of romance and crime :")
print(len(r) + len(c) - 2 * len(cr))
print("number of unique uncommon words of romance and psychology:")
print(len(r) + len(c) - 2 * len(cr))
print("number of unique uncommon words of sychology and crime:")
print(len(p) + len(c) - 2 * len(pc))
table_csv2.append(['number of unique uncommon words of romance and crime' ,len(r) + len(c) - 2 * len(cr)])
table_csv2.append(['number of unique uncommon words of romance and psychology',len(r) + len(c) - 2 * len(cr)])
table_csv2.append(['number of unique uncommon words of sychology and crime',len(p) + len(c) - 2 * len(pc)])

d_r = dict()
d_c = dict()
d_p = dict()

for i in word_broken:
    if word_broken[i]['genre'] == "crime":
        for w in word_broken[i]['word_broken']:
            if (w not in r) and (w not in p):
                if w not in d_c:
                    d_c[w] = 1
                else:
                    d_c[w] += 1

for i in word_broken:
    if word_broken[i]['genre'] == "romance":
        for w in word_broken[i]['word_broken']:
            if (w not in c) and (w not in p):
                if w not in d_r:
                    d_r[w] = 1
                else:
                    d_r[w] += 1

for i in word_broken:
    if word_broken[i]['genre'] == "psychology":
        for w in word_broken[i]['word_broken']:
            if (w not in r) and (w not in c):
                if w not in d_p:
                    d_p[w] = 1
                else:
                    d_p[w] += 1

print("10 common most used words:")
h1 = dict(sorted(d_c.items(), key=lambda x: x[1])[:10])
print(h1.keys())
h2 = dict(sorted(d_r.items(), key=lambda x: x[1])[:10])
print(h2.keys())
h3 = dict(sorted(d_p.items(), key=lambda x: x[1])[:10])
print(h3.keys())
table_csv.append(['10 common most used words' , list(h1.keys()) , list(h2.keys()) , list(h3.keys())])

file_name = './stats.csv'
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in table_csv:
        writer.writerow(row)

file_name = './stats2.csv'
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in table_csv2:
        writer.writerow(row)