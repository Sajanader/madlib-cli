import re

print('you are welcome in madlib game')
noun = input('Please enter a noun: ')
verb= input('Please enter a past verb: ')
verb2= input('Please enter a past verb: ')
adj= input('Please enter an adjective: ')
verb3= input('Please enter a past verb: ')
adverb = input('Please enter an adverb: ')
medlib=[noun,verb,verb2,adj,verb3,adverb]
# print('yesterday I cooked a' , noun , 'I ',verb, ' my dish then ',verb2, 'in the oven after that the meal was',adj,' and we' ,verb3,'it' ,adverb,)

def read_template():

    with open('assets/madlib_template.txt','r') as file:
        content=file.read().strip()
    return content   


def parse(content):
    x= re.sub('{[^}]+}','{}',content)
    print(x)
    y= re.findall('\{(.*?)\}', content)
    y=medlib 
    return y,x 


def merge(y,x):
    w=x.format(*y)
    print(w)
    return w

def copyFile(w):
    file = open('assets/print.txt','w')
    file.write(w)

if __name__ == "__main__":
    content = read_template()
    y,x=parse(content)
    w=merge(y,x)
    copyFile(w)