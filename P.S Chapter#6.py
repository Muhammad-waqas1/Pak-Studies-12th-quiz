questions=["Q#1 International Cricket council granted permission to Pakistan to participate in cricket competitions in:",
"Q#2 The captain when Pakistan first became the international champion of hockey.",
"Q#3 Against which country Pakistan won its first International Cricket Cup?",
"Q#4 Pakistan Tourism Development came into being in:",
"Q#5 In 1962, Tumgha-e-Imtiaz was awarded by Government of Pakistan?",
"Q#6 Which capability of a child increases prominently to play a drama?",
"Q#7 The institution responsible of cricket at international level?",
"Q#8 King Qutab-ud-Din Aibaik died of fell from the horse while playing:",
"Q#9 The institution was established to develop tourism in Pakistan?",
"Q#10 Masjid Wazeer Khan is situated in:"]
answers=["(a)1951 \t\t(b)1952\n(c)1953 \t\t(d)1954",
"(a)Khalid Mehmood \t\t(b)Akhtar-ul-Islam\n(c)Sami Ullah \t\t(d)Hassan Sardar",
"(a)Australia \t\t(b)New Zealand\n(c)West Indies \t\t(d)England",
"(a)1970 \t\t(b)1972\n(c)1974 \t\t(d)1976",
"(a)Iman Bakhash \t\t(b)Jhara\n(c)Bholu \t\t(d)Gama",
"(a)Physical \t\t(b)Linguistics\n(c)Leadership \t\t(d)Decision making",
"(a)ICC \t\t(b)PCB\n(c)ICB \t\t(d)PFF",
"(a)Kabaddi \t\t(b)Horse riding\n(c)Polo \t\t(d)Football",
"(a)PTDC \t\t(b)PCB\n(c)PTCL \t\t(d)PMA",
"(a)Peshawar \t\t(b)Multan\n(c)Lahore \t\t(d)Sialkot"]
correct_answers=["b","a","d","b","c","b","a","c","a","c"]
#keyofquestions=["1","2","3","4","5","6","7","8","9","10"]
#keyofquestions        =["1","2","3","4","5","6","7","8","9","10"]
correct_answers_capital=["B","A","D","B","C","B","A","C","A","C"]
correct_answers_parenthesis=["(b)","(a)","(d)","(b)","(c)","(b)","(a)","(c)","(a)","(c)"]
#Parenthesis keyofquestions=["(1)","(2)","(3)","(4)","(5)","(6)","(7)","(8)","(9)","(10)"]  
correct_ans_cap_parenthesis=["(B)","(A)","(D)","(B)","(C)","(B)","(A)","(C)","(A)","(C)"]    
price=[50,100,200,400,600,800,1000,1500,2000,3000]
# print(len(questions))   (a)(b)(c)(d)
# print(len(answers))
# print(len(correct_answers))
# print(len(price))
print("*******************************\nChapter#6:Sports and Tourism:\n*******************************")
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