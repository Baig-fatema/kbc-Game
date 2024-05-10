print("----------------------- WELCOME TO KBC ------------------")
print("TOTAL LEVELS :  3 ")
print("LEVEL 1 :- 3 QUESTIONS :- AMOUNT (10000)")
print("LEVEL 1 :- 6 QUESTIONS :- AMOUNT (175000)")
print("LEVEL 1 :- 9 QUESTIONS :- AMOUNT (725000)")

print(" ************ START ***********")
Questions=[["Q1.what is the national game of india? "," A . Hockey "," B . FootBall "," C .  Cricket "," D. VallyBall" , "A"],
           ["Q2.who is prime minister of india? "," A . G.Rahul "," B . Modi "," C .  Fadnavis "," D. Shinde" , "B"],
           ["Q3.who is  President of india? "," A . Mayawati "," B . Indra Gandhi "," C .  Ramnath "," D. Durpadi murmo" , "D"],
           ["Q4.what is the national bird of india? "," A . Sparrow "," B . Peacock "," C .  Eagle "," D. Parrot" , "B"],
           ["Q5.what is the national Flower of india? "," A . Lotus "," B . Rose "," C .  sunlfower "," D. Jasmine" , "A"],
           ["Q6.what is the Animal  of india? "," A . Deer "," B . Beer "," C .  Lion "," D. Tiger" , "D"],
           ["Q7.what is the national Currency of india? "," A . Dollar "," B . Riyal "," C .  Rupees "," D. Deenar" , "C"],
           ["Q8.what is the national Fruit of india? "," A . Banana "," B . Mango "," C .  Apple "," D. Papaya" , "B"],
           ["Q9.what is the national game of india? "," A . Hockey "," B . FootBall "," C .  Cricket "," D. VallyBall" , "A"]]
money=0
levels=[1000,2000,7000,25000,50000,90000,125000,200000,225000]
for i in range(len(Questions)):
    question=Questions[i]
    print(question[0])
    print(f"{question[1]}             {question[2]}")
    print(f"{question[3]}             {question[4]}")
    reply=input(("Enter Option Or Press (Q) to quit."))
    reply=reply.upper()
    if(i==2):
        money=10000
    elif(i==5):
        money=175000   
    elif(i==8):
        money=725000     
    if(reply=="Q"):
        if(i==0):
            print("Your Winning Amount is: 0")
            break
        else:            
            print("Your Winning Amount is: ",levels[i-1])
            break
    if(reply==question[5]):
        if(i==8):
            print(f"Write Answer: you win Rs. {levels[i]}") 
            print(f"7 LAKHPATI : ALL LEVELS COMPLETED SUCCESSFULLY ....... Rs. {money}")
            break
        else:
           print(f"Write Answer: you win Rs. {levels[i]}")        
    else:
        print("Wrong Answer.. ")
        print("Your Winning Amount is: Rs. ",money)
        break






