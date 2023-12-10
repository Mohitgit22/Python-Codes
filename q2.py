import q2module as m1
while True:
    print("1 for dislaying data 2.Reinitializing data 3. Calculating Contra 0.Exit")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        print("a = ",m1.a,"b= ",m1.b,"c= ",m1.c,"d= ",m1.d, "e= ",m1.e)
    elif(ch==2):
        m1.take_input()
        print("a = ",m1.a,"b= ",m1.b,"c= ",m1.c,"d= ",m1.d , "e= ",m1.e)
    elif(ch==3):
        contra=m1.a + 10*m1.b*m1.c + 5*m1.d/m1.e
        print("Contra = ",contra)
    elif(ch==0):
        exit()
    else:
        print("Invalid choice")