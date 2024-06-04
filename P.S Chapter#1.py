questions=["Q#1 Nazria is a translation of the word \"ideologie\" which is the word of:",
"Q#2 Name of the Prime Minister who presented Objectives Resolution 1949:",
"Q#3 First demanded for separate electorate in the subcontinent:",
"Q#4 Lahore Resolution was presented in:",
"Q#5 Literal meaning of justice is:",
"Q#6 Allama Muhammad Iqbal(R.A) delivered his famous presidential address in 1930:",
"Q#7 Quaid-e-Azam(R.A) addressed the students in Peshawar:",
"Q#8 \"ksy araby ko ksy ajmy par or ksy ajmy ko ksy araby par, ksy gory ko ksy kaly par or ksy kaly ko ksy gory par koi fokiat hasil nahi hy.\"\nThe Holy Prophet(P.B.U.H) saidon the occasion of:",
"Q#9 Objectives Resolution was passed in:",
"Q#10 Allah Almighty Said \"Translation: beshak(pasandida) deen Allah ky nazdik seraf Islam hy\" in Surah:"]
answers=["(a)Urdu(b)Arabic\n(c)French(d)Greek",
"(a)Khawaja Nazimuddin(b)Muhammad Ali Bogra\n(c)Chaudry Muhammad Ali(d)Liaqat Ali Khan",
"(a)Allama Muhammad Iqbal(R.A)(b)Sir Syed Ahmad Khan\n(c)Chaudry Muhammad Ali(d)Quaid-e-Azam(R.A)",
"(a)1930(b)1940\n(c)1945(d)1950",
"(a)Peaceful and prosperous society(b)Collective improvement\n(c)Character building(d)Putting the right thing, on the right place",
"(a)In Delhi(b)In Lahore\n(c)In karachi(d)In Allahabad",
"(a)1945(b)1947\n(c)1946(d)1948",
"(a)Immediately after the Prophethood(b)The migration to Medina\n(c)Hujjat-ul-Vida(d)Treaty of Hudaybiyya",
"(a)1948(b)1949\n(c)1951(d)1950",
"(a)Al-Baqarah(b)Ale-Imran\n(c)Al-Nisa(d)Al-Maida"]
correct_answers=["c","d","b","b","d","d","a","c","b","b"]
#keyofquestions=["1","2","3","4","5","6","7","8","9","10"]
correct_answers_parenthesis=["(c)","(d)","(b)","(b)","(d)","(d)","(a)","(c)","(b)","(b)"]
correct_answers_capital=["C","D","B","B","D","D","A","C","B","B"]    
correct_ans_cap_parenthesis=["(C)","(D)","(B)","(B)","(D)","(D)","(A)","(C)","(B)","(B)"]    
price=[50,100,200,400,600,800,1000,1500,2000,3000]
# print(len(questions))   (a)(b)(c)(d)
# print(len(answers))
# print(len(correct_answers))
# print(len(price))
print("*************************************\nChapter#1:Islam and Pakistan:\n*************************************")
for i in range(0,len(questions)):
    print(questions[i])
    option=input(answers[i]+"\nEnter the option letter only:\n")    
    if(option=="o")or(option=="O")or(option=="cls"):
        break
    if (option==correct_answers[i]) or (option== correct_answers_capital[i]) or (option== correct_answers_parenthesis[i]) or (option== correct_ans_cap_parenthesis[i]):
        l=[]
        l.append(i)
        print("The answer is \"correct\"\n------------------------------------------press o to exit\n------------------------------------------")     # you won Rs",price[i]
        if(i+1==len(questions)):
                print(f"MCQS session is over.\nYour total Scrore is {len(l)}/{len(questions)}")
    elif(i==0):
        print(f"The correct answer was \"{correct_answers_parenthesis[i]}\"\n-------------------------------------------press o to exit\n------------------------------------------")
    else:
        print(f"The correct answer was \"{correct_answers_parenthesis[i]}\"\n------------------------------------------press o to exit\n------------------------------------------")       # "You earn Rs",price[i-1],