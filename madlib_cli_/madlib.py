import re
def welcome():
    print('welcome in madlib game/n just enter the answer and wait to see the result')


def read_template():
    with open('assets/madlib_template.txt', 'r') as file:
        content = file.read()
    return content

def parse(content):
    y=[]
    x = re.findall(r'\{.*?\}',content) 
    print(x)
    answers = re.sub("{[^}]*}", " {}", content)
    print(answers)
    for i in x:
        y.append(i.strip("{ }"))
    return y,answers  

def merge(answers,m):
  
    z = answers.format(*m)
    return z

def copyFile(answers):
    print()
    print(answers)
    file = open('assets/print.txt','w')
    file.write(answers)




if __name__ == "__main__":
    welcome()
   
    content = read_template()
    y =parse(content)
    
    m =[]
    for v in y[0]:
        q=input("please enter a:   " +v + " : " )
        m.append(q)
    copy = merge(y[1],m)
    copyFile(copy)