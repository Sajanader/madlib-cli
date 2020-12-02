import re

print('you are welcome in madlib game')

noun = input('Please enter a noun: ')
verb= input('Please enter a past verb: ')
verb2= input('Please enter a past verb: ')
adj= input('Please enter an adjective: ')
verb3= input('Please enter a past verb: ')
adverb = input('Please enter an adverb: ')
medlib=[noun,verb,verb2,adj,verb3,adverb]
print('yesterday I cooked a' , noun , 'I ',verb, ' my dish then ',verb2, 'in the oven after that the meal was',adj,' and we' ,verb3,'it' ,adverb,)

def read_template():

    with open('assets/madlib.txt','r') as file:
        content=file.read().strip()
      

read_template()
def parse():
    with open('assets/madlib.txt','r') as file:
         content=file.read().strip()
         x= re.sub('{[^}]+}','{}',content)
   
         print(x)
         y= re.findall('\{(.*?)\}', content)
         y=medlib
         c=str(y).strip('[]')
         print(y[0])
      
         print(len(y))
         for v in y:
             j=re.sub('{}',v,x)
            
             print(j)
    
     

parse()
