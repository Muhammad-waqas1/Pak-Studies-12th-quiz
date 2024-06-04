questions=["Q#1 The English word Education means:",
"Q#2 The levels of education in Pakistan are:",
"Q#3 The discipline of education holds the basic place in industrial development of a country?",
"Q#4 The duration of elementary education is:",
"Q#5 Another name for higher secondary education:",
"Q#6 Free education is provided from elementary to higher education is:",
"Q#7 The duration of secondary education is:",
"Q#8 How many years does it take to do LLB after intermediate:",
"Q#9 Allama Iqbal Open Universicy teaching method is:",
"Q#10 Considered man a social animal:"]
answers=["(a)Developing(b)Learning\n(c)Examining(d)Moving forward",
"(a)Two(b)Three\n(c)Four(d)Five",
"(a)Science education(b)Engineering education\n(c)Business and Commerce education(d)Religious education",
"(a)Six years(b)Seven years\n(c)Eight years(d)Nine years",
"(a)Graduation(b)Intermediate\n(c)Post-graduation(d)Professional",
"(a)Govt. Institutes(b)Private institutes\n(c)Religious Madrassas(d)Industrial educational institutes",
"(a)Two years(b)Three years\n(c)Four years(d)Five years",
"(a)Two(b)Three\n(c)Four(d)Five",
"(a)Informal(b)Distance\n(c)Complex(d)None of these",
"(a)Aristotle(b)Socrates\n(c)Hippocrates(d)Plato"]
correct_answers=["a","c","b","c","b","c","a","d","b","a"]
correct_answers_capital=["A","C","B","C","B","C","A","D","B","A"]
#keyofquestions=["1","2","3","4","5","6","7","8","9","10"]
#Parenthesis keyofquestions=["(1)","(2)","(3)","(4)","(5)","(6)","(7)","(8)","(9)","(10)"]
correct_answers_parenthesis=["(a)","(c)","(b)","(c)","(b)","(c)","(a)","(d)","(b)","(a)"]
correct_ans_cap_parenthesis=["(A)","(C)","(B)","(C)","(B)","(C)","(A)","(D)","(B)","(A)"]    
price=[50,100,200,400,600,800,1000,1500,2000,3000]
# print(len(questions))   (a)(b)(c)(d)
# print(len(answers))
# print(len(correct_answers))
# print(len(price))
print("*****************************************\nChapter#5:Education System in Pakistan:\n*****************************************")
for i in range(0,len(questions)):
    print(questions[i])
    option=input(answers[i]+"\nEnter the option letter only:\n")    
    if(option=="o")or(option=="O")or(option=="cls"):
        break
    if (option==correct_answers[i]) or (option== correct_answers_capital[i]) or (option== correct_answers_parenthesis[i]) or (option== correct_ans_cap_parenthesis[i]):
        print("The answer is \"correct\"\n------------------------------------------press o to exit\n------------------------------------------")     # you won Rs",price[i]
        # if(i+1==len(questions)):
        #         print(f"MCQS session is over.\nYour total Scrore is {i+1}/{len(questions)}")
    elif(i==0):
        print(f"The correct answer was \"{correct_answers_parenthesis[i]}\"\n-------------------------------------------press o to exit\n------------------------------------------")
    else:
        print(f"The correct answer was \"{correct_answers_parenthesis[i]}\"\n------------------------------------------press o to exit\n------------------------------------------")       # "You earn Rs",price[i-1],