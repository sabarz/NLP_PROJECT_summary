import json

ans = dict()
cnt = 0

f = open("./../../data/clean/clean.json", "r")
data = json.load(f)
f.close()

sent_broken = []
for i, summery in enumerate(data['crime']):
    sent_broken = [s.lstrip() for s in summery.split('.') if s.strip()]
    ans[cnt] = {
        "genre": 'crime',
        "summery": summery,
        "sent_broken": sent_broken
    }
    cnt += 1

sent_broken = []
for i, summery in enumerate(data['romance']):
    sent_broken = summery.split('.')
    ans[cnt] = {
        "genre": 'romance',
        "summery": summery,
        "sent_broken": sent_broken
    }
    cnt += 1

sent_broken = []
for i, summery in enumerate(data['psychology']):
    sent_broken = summery.split('.')
    ans[cnt] = {
        "genre": 'psychology',
        "summery": summery,
        "sent_broken": sent_broken
    }
    cnt += 1

f = open("./../../data/sentencebroken/sentencebroken.json", "w")
json.dump(ans, f)
f.close()
