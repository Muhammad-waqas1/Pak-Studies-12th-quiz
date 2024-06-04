questions=["Q#1 The Holy Prophet Hazrat Muhammad(P.B.U.H) addressed the last sermon in:",
"Q#2 In Britain, the king signed the Magna Carta document in:",
"Q#3 Translation:\"Deen my koi zabrdasty nahi hy.\"\nVerse is found in the Surah:",
"Q#4 The right to purchase property and hold a private property comes under the category:",
"Q#5 Translation:\"Or jo Allah ky Nazil karda Hukam ky mutabik fisla na kary to wohe loog kafir hain.\"\nVerse comes in the Surah:",
"Q#6 Which comes under the category of political rights?",
"Q#7 Every year, on which date United Nations celebrates the birthday of Univeral Declaration of Human Rights:",
"Q#8 In case of arrest, a citizen is presented in the court of magistrate within:",
"Q#9 The Universal Declaration of Human Rights was approved in United Nations in:",
"Q#10 Mothers gave them birth free and how did you make them your slave? It is saying of:"]
answers=["(a)9thA.H.(b)10thA.H.\n(c)11thA.H.(d)12thA.H.",
"(a)1015(b)1115\n(c)1215(d)1315",
"(a)Al-Baqra(b)Aal-e-Imran\n(c)Al-Nissa(d)Al-Maaida",
"(a)Social(b)Economic\n(c)Religious(d)Cultural",
"(a)Al-Baqra(b)Al-Fatiha\n(c)Al-Nissa(d)Al-Maaida",
"(a)right ot vote(b)to adopt a profession\n(c)religious freedom(d)to get education",
"(a)1st December(b)5th December\n(c)8th December(d)10th December",
"(a)20 hours(b)22 hours\n(c)24 hours(d)26 hours",
"(a)1946(b)1947\n(c)1948(d)1949",
"(a)Hazrat Abu-Bakr(R.A)(b)Hazrat Umar(R.A)\n(c)Hazrat Usman(R.A)(d)Hazrat Ali(Krm-Allah-vjah-alkarim)"]
correct_answers=["b","c","a","b","d","a","d","c","c","b"]
#keyofquestions=["1","2","3","4","5","6","7","8","9","10"]
correct_answers_capital=["B","C","A","B","D","A","D","C","C","B"]    
correct_answers_parenthesis=["(b)","(c)","(a)","(b)","(d)","(a)","(d)","(c)","(c)","(b)"]
#Parenthesis keyofquestions=["(1)","(2)","(3)","(4)","(5)","(6)","(7)","(8)","(9)","(10)"]
correct_ans_cap_parenthesis=["(B)","(C)","(A)","(B)","(D)","(A)","(D)","(C)","(C)","(B)"]    
price=[50,100,200,400,600,800,1000,1500,2000,3000]
# print(len(questions))   (a)(b)(c)(d)
# print(len(answers))
# print(len(correct_answers))
# print(len(price))
print("********************************\nChapter#4:Human Rights:\n********************************")
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