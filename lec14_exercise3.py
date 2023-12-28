# Create a KBC type game.
questions = ["who is the main protagnist of code geass?","what is the full name of the protagnist of death note?","in fmab, what stone every alchemist desires?","what is midoriya's hero name?","what is the name of midoriya's quirk?","in season 5 who was the number 2 ranked hero in mha?","what is the naame of midoriya's second activated power?","what was the name of japan in code geass?","what is the name of the cat in code geass?","What is the name of this Shinigami, who is the original owner of the Death Note that Light uses?"]
answers = ["lelouch","light yagami","philosophers stone","deku","one for all","hawks","black whip","area 11","arthur","sidoh"]
prize = 0
for count in range(len(questions)):
    print("Question ",count+1,": ",questions[count])
    answer=input("Answer: ")
    if(answer == answers[count]):
        print("Correct Answer! You have won 10000 Taka!")
        prize+=10000
    elif(answer == "skip"):
        print("You have skipped this question.")
    else:
        print("Wrong Answer! You have lost 5000 Taka!")   
        prize-=5000

print("Congratulaions you have earned ",prize," Taka.")             
        
        
    