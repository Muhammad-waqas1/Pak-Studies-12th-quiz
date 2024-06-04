questions=["Q#1 Constitution of 1956 remained in force in the country:",
"Q#2 After the formation of Bangladesh,General Muahmmad Yahya Khan handed over power in (West) Paksitan to:",
"Q#3 Dismissed the government of Ms.Benazir Bhutto in August 1990:",
"Q#4 To run the system of the country, an interim constitution was drafted in 1972 and for the future contitution, a committee consisting of the newly elected members of the National Assembly was formed:",
"Q#5 The year when the first general elections were held in the country:",
"Q#6 Consitution of 1973 was  enforced on:",
"Q#7 Administrative head of federal ministry is:",
"Q#8 Head of the provincial government is:",
"Q#9 Consitutional Amendment defines Muslim:",
"Q#10 Consitutional Amendment in which NWFP was named as Khyber Pakhtunkhwa:"]
answers=["(a)Two years(b)Two and a half years\n(c)Three years(d)Four years",
"(a)Fazal Elahi Chaudhry(b)Z.A. Bhutto\n(c)Feroz Khan noon(d)Chaudhry Zahoor Elahi",
"(a)Ghulam Ishaq Khan(b)Farooq Ahmad Leghari\n(c)Balkh Sher Mazari(d)Wasim Sajjad",
"(a)10(b)15\n(c)20(d)25",
"(a)1964(b)1968\n(c)1970(d)1972",
"(a)11-August(b)12-August\n(c)13-August(d)14-August",
"(a)Minister(b)Secretary\n(c)Additional Secretary(d)Joint Secretary",
"(a)President(b)Governor\n(c)Cheif Minister(d)Speaker",
"(a)Second(b)Fifth\n(c)Eighteenth(d)Eight",
"(a)Fourteenth(b)Eighteenth\n(c)Twentieth(d)Twenty Second"]
correct_answers=["b","b","a","d","c","d","b","b","a","b"]
#keyofquestions       =["1","2","3","4","5","6","7","8","9","10"]
correct_answers_parenthesis=["(b)","(b)","(a)","(d)","(c)","(d)","(b)","(b)","(a)","(b)"]
correct_answers_capital=["B","B","A","D","C","D","B","B","A","B"]    
correct_ans_cap_parenthesis=["(B)","(B)","(A)","(D)","(C)","(D)","(B)","(B)","(A)","(B)"]    
price=[50,100,200,400,600,800,1000,1500,2000,3000]
# print(len(questions))   (a)(b)(c)(d)
# print(len(answers))
# print(len(correct_answers))
# print(len(price))
print("****************************************************\nChapter#2:Polictical and Consitutional Development:\n****************************************************")
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