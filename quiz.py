import random
lines=[line.rstrip('\n') for line in open("sample.txt")]
length1=len(lines)
list1=[]
for i in range(0,length1,2):
	list1.append([lines[i],lines[i+1]])
#print(list1)
point=0
random.shuffle(list1)
for qu in list1:
	print(qu[0])
	answer=str(input("enter ur answer\n"))
	answer1=answer.capitalize()
	if answer1==qu[1]:
		point=point+1
		#print("correct")
grade='A'
if point<4:
	grade='D'
elif point<6:
	grade='C'
elif point<8:
	grade='B'
print("*******************************************************************")
print("end of quiz and ur grade is")
print(grade)
