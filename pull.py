import re
from urllib.request import urlopen


# f = urlopen("http://www.yo-yoo.co.il/data/game/solutions/")
# objects = str(f.read())

for i in range(1,8):
    for l in ["א","ב","ג","ד","ה","ו","ז","ח","ט","י","כ","ל","מ","נ","ס","ע","פ","צ","ק","ר","ש","ת"]:
        url='https://www.yo-yoo.co.il/data/game/c/'+str(i)+'/'+l.decode('UTF-8')
        f= urlopen(url)
        objects = str(f.read())
        # p=re.compile("(?i)<td[^>]*>")
        a=re.match("(?i)<td[^>]*>",objects)
        print(a)
# print(objects)
#for obj in list(objects):
   # article = obj['content']
ret = re.findall("(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})", objects) # question here
# print(ret)
for r in ret:
    print(r)
    # article = article.replace(r, "")
    # print(article)



# import urllib
# f=urllib.urlopen("http://www.yo-yoo.co.il/data/game/solutions/")
# print (f.read())