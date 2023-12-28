letter = input("Enter a letter:")
match letter:
    case 'A':
        print("vowel")
    case 'E':
        print("vowel")
    case 'I':
        print("vowel")
    case 'O':
        print("vowel") 
    case 'U':
        print("vowel")
    case _ if(letter>'a' and letter<'z'):
        print("lower case")
    case _:
        print("consonant")    
                                      