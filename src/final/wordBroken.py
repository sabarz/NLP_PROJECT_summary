import json

ans = dict()
cnt = 0

f = open("./../../data/clean/clean.json", "r")
data = json.load(f)
f.close()

word_broken = []
for i, summery in enumerate(data['crime']):
    word_broken = summery.split()
    ans[cnt] = {
        "genre": 'crime',
        "summery": summery,
        "word_broken": word_broken
    }
    cnt += 1

word_broken = []
for i, summery in enumerate(data['romance']):
    word_broken = summery.split()
    ans[cnt] = {
        "genre": 'romance',
        "summery": summery,
        "word_broken": word_broken
    }
    cnt += 1

word_broken = []
for i, summery in enumerate(data['psychology']):
    word_broken = summery.split()
    ans[cnt] = {
        "genre": 'psychology',
        "summery": summery,
        "word_broken": word_broken
    }
    cnt += 1

f = open("./../../data/wordbroken/wordbroken.json", "w")
json.dump(ans, f)
f.close()
