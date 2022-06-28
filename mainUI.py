from INS368_IDS345_KataRangePackage import Range

print("'''Chose options:\n1.Contain Equals\n2.Contain Containrange\n3.Contain endpoints\n4.Contains allpoints'''")

userInput=int("\nInsert your option: ")
validated = False

while validated == False:
    if userInput == 1:
        ar=input("Insert your first interval")
        br=input("Insert your second interval")
        
        aR=Range(ar)
        bR=Range(br)
        
        print(aR.Equals(bR))
    elif userInput == 2:
        ar=input("Insert your first interval")
        br=input("Insert your second interval")
        
        aR=Range(ar)
        bR=Range(br)
        
        print(aR.containsRange(bR))
    elif userInput == 3:
        ar=input("Insert your first interval")
        aR=Range(ar)
        
        print(aR.endPoints())
    elif userInput == 4:
        ar=input("Insert your first interval")
        aR=Range(ar)
        
        print(aR.getAllPoints())
    else:
        print("Invalid option. Try again.")
    
    opt = input("Do you want to make another operation? ('y' for yes/'n' for no)")
    if opt == 'n':
        validated = True