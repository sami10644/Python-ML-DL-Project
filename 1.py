q1=input('question 1:')
q2=input('question 2:')
with open('aa.txt','w+') as f:
    f.writelines(q1+'\n')
    f.writelines(q2+'\n')
f = open('aa.txt','r')
f.close()
