import re
from urllib.request import urlopen

# f = urlopen("http://www.yo-yoo.co.il/data/game/solutions/")
# objects = str(f.read())

for i in range(8):
    for l in range(40,50):
        
        f= urlopen('https://www.yo-yoo.co.il/data/game/c/'+str(i)+'/'+str(chr(l)))
        objects = str(f.read())
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