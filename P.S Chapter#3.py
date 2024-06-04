questions=["Q#1 Federation performs its duties in the name of :",
"Q#2 For the performance of provincial duties the organization makes laws:",
"Q#3 The number of Kashmir Council members is:",
"Q#4 The number of Gilgit-Baltistan Council members is:",
"Q#5 The number of judges in the Supreme Court of Azad Jammu and Kashmir is:",
"Q#6 Presides over the National Security Council of Pakistan:",
"Q#7 The provision of the 1973 constitution under which local governments are protected:",
"Q#8 Change in the system of local govenment in Pakistan was brought in:",
"Q#9 The levels of local govenment rural areas are:",
"Q#10 The head of the Metropolian Corporation is:"]
answers=["(a)Governor(b)President\n(c)Lord Mayor(d)Mayor",
"(a)National Assembly(b)Senate\n(c)Provincial Assembly(d)Local Govenments",
"(a)12(b)14\n(c)16(d)18",
"(a)12(b)14\n(c)16(d)18",
"(a)3(b)4\n(c)5(d)6",
"(a)President(b)Prime Minister\n(c)Cheif of Army Staff (d)Cheif of Air Staff",
"(a)140-A(b)140-B\n(c)140-C(d)140-D",
"(a)2001(b)2003\n(c)2005(d)2007",
"(a)One(b)Two\n(c)Three(d)Four",
"(a)Chairmen(b)Chairperson\n(c)Lord Mayor(d)Mayor"]
correct_answers=["b","c","b","a","a","b","a","c","b","c"]
#keyofquestions=["1","2","3","4","5","6","7","8","9","10"]
correct_answers_parenthesis=["(b)","(c)","(b)","(a)","(a)","(b)","(a)","(c)","(b)","(c)"]
correct_answers_capital=["B","C","B","A","A","B","A","C","B","C"]    
correct_ans_cap_parenthesis=["(B)","(C)","(B)","(A)","(A)","(B)","(A)","(C)","(B)","(C)"]    
price=[50,100,200,400,600,800,1000,1500,2000,3000]
# print(len(questions))   (a)(b)(c)(d)
# print(len(answers))
# print(len(correct_answers))
# print(len(price))
print("*****************************************\nChapter#3:Administrative System:\n*****************************************")
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