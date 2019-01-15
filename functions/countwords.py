frequency={}
text=open('sample1.txt', 'r')
string=text.read().lower()
print string
string=string.replace('\n',' ')
split1=string.split(' ')
for word in split1:
    count=frequency.get(word,0)
    frequency[word]=count+1
keys=frequency.keys()
for words in keys:
    print words+"      : "+str(frequency[words])
