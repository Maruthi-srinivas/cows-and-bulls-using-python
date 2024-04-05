from tkinter import *
from tkinter import messagebox as mb
import random
import tkinter.font as f
outer=Tk()
font=f.Font(size=20)
L1=Label(outer,text="The Cow-Bull game",font=font,bg="#242424",fg="#F2F2F2").grid(row=0,column=1,pady=30)


def f1():
    a1=str(random.randint(1000,9999))
    print("Randomly generated number:",a1)
    x=0#guesses counter
    global root1
    root1=Tk()
    L2=Label(root1,text="Enter a 4 digit number",font="10",bg="#242424",fg="#F2F2F2").grid(row=0,padx=30,pady=20)
    e=Entry(root1,width=25,font="10",bg="#4D4D4D",borderwidth=5,fg="#F2F2F2")
    e.grid(row=1,padx=30,pady=10)
    root1.title("Level 1")

    def level1():
        win1=Tk()
        win1.title("Stats")
        nonlocal a1,x
        a2=e.get()
        l=list(a2)
        if len(l)!=0:#in case blank is enterned
            while (len(l) and l[0]=="0"):#len(l) when only zeros is entered
                l.pop(0)
        a2="".join(l)
        x+=1
        c=b=0
        l1=list(str(a1))#in lvl1 only 3 lists as final case we check a1==a2
        l2=list(str(a2))
        l3=list(l1)
        if (len(a2)!=4 or not(a2.isdigit())):#invalid cases
            L32=Label(win1,text="Invalid number entered, try again",bg="#242424",fg="#F2F2F2",font="10").grid(padx=10,pady=10)
            x-=1
        else:
            for i in range(len(l1)):
                if l1[i]==l2[i]:
                    c+=1
                    l3.pop(i)
                    l3.insert(i,"x")#to prevent index error and remove extra bulls or cows
                    l2.pop(i)
                    l2.insert(i,"!")
            for i in range(len(l1)):
                if l2[i] in l3:
                    b+=1
            if a1==a2:
                L16=Label(win1,text="You guessed the number!!!!!"+"\n"+"Number of guesses you took: "+str(x),bg="#242424",fg="#F2F2F2",font="10").grid(row=1,padx=20,pady=20)
            elif x==15:
                L17=Label(win1,text="You ran out of guesses",bg="#242424",fg="#F2F2F2",font="10").grid(row=1,padx=20,pady=20)
            else:
                L3=Label(win1,text="Number of bulls: "+str(b),bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                L4=Label(win1,text="Number of cows: "+str(c),bg="#242424",fg="#F2F2F2",font="10").grid(row=1,pady=5,padx=10)
                L5=Label(win1,text="Number of guesses left: "+str(15-x),bg="#242424",fg="#F2F2F2",font="10").grid(row=2,pady=5,padx=20)
        def close():
            win1.destroy()
            if a1==a2:
                root1.destroy()
                if mb.askyesno("You guesses the number!!!!!","Do you want to proceed the the next level?"):                   
                    f2()
                    exit()
                else:
                    mb.showinfo("Exit","Bye")
                    exit()
            elif x==15:
                root1.destroy()
                if mb.askyesno("You ran out of guesses","play again?"):
                    f1()
                    exit()
                else:
                    mb.showinfo("Exit","Bye")
                    exit()
        b5=Button(win1,text="Okay",command=close,bg="#4D4D4D",fg="#F2F2F2",font="10",width=7,cursor="hand2").grid(row=3,pady=10,padx=20)
        win1.configure(bg="#242424")
        win1.geometry("+1000+310")
        win1.mainloop()

    b6=Button(root1,text="Submit",command=level1,font="10",bg="#4D4D4D",fg="#F2F2F2",cursor="hand2").grid(row=2,padx=30,pady=20)
    root1.geometry("+625+300")
    root1.configure(bg="#242424")
    root1.mainloop()


def f2():
    a1=random.randint(100,999)
    l1=list(str(a1))
    b=random.randint(97,122)
    l1.append(chr(b))
    print("Randomly generated sequence:",l1)
    x=0
    root2=Tk()
    L6=Label(root2,text="Enter a 3 number + 1 alphabet sequence as a guess",font="10",bg="#242424",fg="#F2F2F2").grid(row=0,padx=30,pady=20)
    e=Entry(root2,width=25,font="10",bg="#4D4D4D",borderwidth=5,fg="#F2F2F2")
    e.grid(row=1,padx=30,pady=10)
    root2.title("Level 2")

    def lvl2():
        win2=Tk()
        win2.title("Stats")
        nonlocal l1,x
        a2=e.get()
        l=list(a2)
        if len(l)!=0:
            while (len(l) and l[0]=="0"):
                l.pop(0)
        a2="".join(l)
        c=b=0
        l2=list(str(a2))
        l3=list(l1)
        l4=list(l2)#extra deep copy so that we can compare l1==l4 for winning condition
        x+=1
        if (len(a2)!=4 or not(a2[:3].isdigit()) or not(a2[3].isalpha())):
            L33=Label(win2,text="Invalid sequence entered, try again",bg="#242424",fg="#F2F2F2",font="10").grid(padx=10,pady=10)
            x-=1
        else:
            l2[3]=l2[3].lower()
            l4[3]=l4[3].lower()
            for i in range(len(l1)):
                if l1[i]==l2[i]:
                    c+=1
                    l3.pop(i)
                    l3.insert(i,"$")
                    l2.pop(i)
                    l2.insert(i,"!")
            for i in range(len(l1)):
                if l2[i] in l3:
                    b+=1
            d=abs(ord(l1[3])-ord(l4[3]))#to find distance between the alphabets
            if l1==l4:
                L18=Label(win2,text="You guessed the sequence!!!!!"+"\n"+"Number of guesses you took: "+str(x),bg="#242424",fg="#F2F2F2",font="10").grid(row=1,padx=20,pady=20)
            elif x==15:
                L19=Label(win2,text="You ran out of guesses",bg="#242424",fg="#F2F2F2",font="10").grid(row=1,padx=20,pady=20)
            else:
                if d==0:
                    L33=Label(win2,text="You guessed the alphabet!",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                elif d in range(1,7):
                    L10=Label(win2,text="Alphabet is close",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                elif d in range(7,16):
                    L11=Label(win2,text="Alphabet is far",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                elif d in range(16,26):
                    L12=Label(win2,text="Alphabet is very far",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                L13=Label(win2,text="Number of bulls: "+str(b),bg="#242424",fg="#F2F2F2",font="10").grid(row=1,pady=5,padx=10)
                L14=Label(win2,text="Number of cows: "+str(c),bg="#242424",fg="#F2F2F2",font="10").grid(row=2,pady=5,padx=10)
                L15=Label(win2,text="Number of guesses left: "+str(15-x),bg="#242424",fg="#F2F2F2",font="10").grid(row=3,pady=5,padx=20)
        def close():
            win2.destroy()
            if l1==l4:
                root2.destroy()
                if mb.askyesno("You guessed the sequence!!!!!","Do you want to proceed the the next level?"):
                    f3()
                    exit()
                else:
                    mb.showinfo("Exit","Bye")
                    exit()
            elif x==15:
                root2.destroy()
                if mb.askyesno("You ran out of guesses","play again?"):
                    f2()
                    exit()
                else:
                    mb.showinfo("Exit","Bye")
                    exit()
        b7=Button(win2,text="Okay",command=close,bg="#4D4D4D",fg="#F2F2F2",font="10",width=7,cursor="hand2").grid(row=4,pady=10,padx=20)
        win2.configure(bg="#242424")
        win2.geometry("+1070+295")
        win2.mainloop()

    b8=Button(root2,text="Submit",command=lvl2,font="10",bg="#4D4D4D",fg="#F2F2F2",cursor="hand2").grid(row=2,padx=30,pady=20)
    root2.geometry("+530+300")
    root2.configure(bg="#242424")
    root2.mainloop()


def f3():
    a1=random.randint(10,99)
    l1=list(str(a1))
    b=random.randint(97,122)
    c=random.randint(97,122)
    l1.append(chr(b))
    l1.append(chr(c))
    x=0
    root3=Tk()
    L20=Label(root3,text="Enter a two digit number and a 2 letter sequence:",font="10",bg="#242424",fg="#F2F2F2").grid(row=0,padx=30,pady=20)
    E=Entry(root3,width=25,font="10",bg="#4D4D4D",borderwidth=5,fg="#F2F2F2")
    E.grid(row=1,padx=30,pady=10)
    root3.title("Level 3")
    print("Randomly generated sequence:",l1)

    def lvl3():
        win3=Tk()
        win3.title("Stats")
        nonlocal l1,x
        a2=E.get()
        l=list(a2)
        if len(l)!=0:
            while (len(l) and l[0]=="0"):
                l.pop(0)
        a2="".join(l)
        x+=1
        c=b=0
        l2=list(str(a2))
        l3=list(l1)
        l4=list(l2)
        if (len(a2)!=4 or not(a2[:2].isdigit()) or not(a2[2:4].isalpha())):
            L34=Label(win3,text="Invalid sequence entered, try again",bg="#242424",fg="#F2F2F2",font="10").grid(padx=10,pady=10)
            x-=1
        else:
            l2[2]=l2[2].lower()
            l2[3]=l2[3].lower()
            l4[2]=l4[2].lower()
            l4[3]=l4[3].lower()
            d=abs(ord(l1[2])-ord(l4[2]))
            e=abs(ord(l1[3])-ord(l4[3]))
            for i in range(len(l1)):
                if l1[i]==l2[i]:
                    c+=1
                    l3.pop(i)
                    l3.insert(i,"$")
                    l2.pop(i)
                    l2.insert(i,"!")
            for i in range(len(l1)):
                if l2[i] in l3:
                    b+=1
            if l1==l4:
                L21=Label(win3,text="You guessed the sequence!!!!!"+"\n"+"Number of guesses you took: "+str(x),bg="#242424",fg="#F2F2F2",font="10").grid(row=1,padx=20,pady=20)
            elif x==15:
                L22=Label(win3,text="You ran out of guesses",bg="#242424",fg="#F2F2F2",font="10").grid(row=1,padx=20,pady=20)
            else:
                if d==0:
                    L34=Label(win3,text="You  guessed the first alphabet!!",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                elif d in range(1,7):
                    L23=Label(win3,text="First alphabet is close",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                elif d in range(7,16):
                    L24=Label(win3,text="First alphabet is far",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                elif d in range(16,26):
                    L25=Label(win3,text="First alphabet is very far",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,pady=10,padx=10)
                if e==0:
                    L35=Label(win3,text="You guessed the second alphabet!!",bg="#242424",fg="#F2F2F2",font="10").grid(row=1,pady=5,padx=10)
                elif e in range(1,7):
                    L26=Label(win3,text="Second alphabet is close",bg="#242424",fg="#F2F2F2",font="10").grid(row=1,pady=5,padx=10)
                elif e in range(7,16):
                    L27=Label(win3,text="Second alphabet is far",bg="#242424",fg="#F2F2F2",font="10").grid(row=1,pady=5,padx=10)
                elif e in range(16,26):
                    L28=Label(win3,text="Second alphabet is very far",bg="#242424",fg="#F2F2F2",font="10").grid(row=1,pady=5,padx=10)
                L29=Label(win3,text="Number of bulls: "+str(b),bg="#242424",fg="#F2F2F2",font="10").grid(row=2,pady=5,padx=10)
                L30=Label(win3,text="Number of cows: "+str(c),bg="#242424",fg="#F2F2F2",font="10").grid(row=3,pady=5,padx=10)
                L31=Label(win3,text="Number of guesses left: "+str(15-x),bg="#242424",fg="#F2F2F2",font="10").grid(row=4,pady=5,padx=20)
        def close():
            win3.destroy()
            if l1==l4:
                root3.destroy()
                end=Tk()
                end.geometry("+635+360")
                end.configure(bg="#242424")
                end.title("Game Over")
                L32=Label(end,text="You've completed the game!!!!!",bg="#242424",fg="#F2F2F2",font="10").grid(row=0,padx=20,pady=10)
                b=Button(end,text="Quit",command=lambda:exit(),font="10",bg="#4D4D4D",fg="#F2F2F2",width=7,cursor="hand2").grid(row=1,pady=5)
                end.mainloop()
            elif x==15:
                root3.destroy()
                if mb.askyesno("You ran out of guesses","play again?"):
                    f3()
                    exit()
                else:
                    mb.showinfo("Exit","Bye")
                    exit()
        b7=Button(win3,text="Okay",command=close,bg="#4D4D4D",fg="#F2F2F2",font="10",width=7,cursor="hand2").grid(row=5,pady=10,padx=20)
        win3.configure(bg="#242424")
        win3.geometry("+1070+295")
        win3.mainloop()

    b8=Button(root3,text="Submit",command=lvl3,font="10",bg="#4D4D4D",fg="#F2F2F2",cursor="hand2").grid(row=2,padx=30,pady=20)
    root3.geometry("+545+300")
    root3.configure(bg="#242424")
    root3.mainloop()


def levels():
    outer.destroy()
    global layout
    layout=Tk()
    layout.title("Menu")
    L=Label(layout,text="Choose a level",font="10",bg="#242424",fg="#F2F2F2").grid(row=0,pady=10)
    b3=Button(layout,text="Level 1",command=f1,font='10',fg="#F2F2F2",bg="#4D4D4D",cursor="hand2").grid(row=1,pady=10,padx=57)
    b4=Button(layout,text="Level 2",command=f2,font="font",fg="#F2F2F2",bg="#4D4D4D",cursor="hand2").grid(row=2,pady=10,padx=57)
    b5=Button(layout,text="Level 3",command=f3,font="10",fg="#F2F2F2",bg="#4D4D4D",cursor="hand2").grid(row=3,pady=10,padx=57)
    layout.geometry("190x250+700+290")
    layout.configure(bg="#242424")
    layout.mainloop()
    return layout


def ask():
    if mb.askyesno("Quit","Do you want to quit the game?"):
        exit()
    else:
        mb.showinfo("Play","Then play the game")


def rules():
    rules=Tk()
    L10=Label(rules,text="Rules",bg="#242424",fg="#F2F2F2",font=("Ariel",15)).grid(row=0,column=0,pady=10,padx=10,columnspan=2)
    L11=Label(rules,text="COWS:   Represents the number of digits/characters in your guess which are in the same position and "+"\n"+"have the same value as the digit/character in the randomly generated sequence"+"\n",bg="#242424",fg="#F2F2F2",font=("Ariel",13)).grid(row=3,column=0,pady=0,padx=10,sticky="W")
    L12=Label(rules,text="BULLS:   Represents the number of digits/characters in your guess which are present in the randomly generated"+"\n"+"sequence but their positions do not match with the randomly generated sequence"+"\n",bg="#242424",fg="#F2F2F2",font=("Ariel",13)).grid(row=6,column=0,pady=0,padx=10)
    L13=Label(rules,text="LEVEL1:   In level 1 you have to guess a 4 digit number"+"\n",bg="#242424",fg="#F2F2F2",font=("Ariel",13)).grid(row=9,column=0,pady=0,padx=10,sticky="W")
    L14=Label(rules,text="LEVEL2:   In level 2 you have to guess a sequence of 3 numbers and 1 alphabet(can be"+"\n"+"uppercase or lowercase) in the format 123a"+"\n",bg="#242424",fg="#F2F2F2",font=("Ariel",13)).grid(row=11,column=0,pady=0,padx=10,sticky="W")
    L15=Label(rules,text="LEVEL3:   In level 3 you have to guess a sequence of 2 numbers and 2 alphabets(can be"+"\n"+"uppercase or lowercase) in the format 12ab"+"\n",bg="#242424",fg="#F2F2F2",font=("Ariel",13)).grid(row=14,column=0,pady=0,padx=10,sticky="W")
    rules.geometry("+350+230")
    rules.configure(bg="#242424")
    rules.mainloop()


b1=Button(outer,text="Start",command=levels,bg="#4D4D4D",font="15",width=5,fg="#F2F2F2",cursor="hand2").grid(row=1,column=0,pady=30,padx=19)
b2=Button(outer,text="Quit",command=ask,bg="#4D4D4D",font="15",width=5,fg="#F2F2F2",cursor="hand2").grid(row=1,column=2,pady=30,padx=4)
b3=Button(outer,text="Rules",command=rules,cursor="hand2",bg="#4D4D4D",font="15",width=5,fg="#F2F2F2").grid(row=1,column=1,pady=30,padx=4)
outer.title("Cow-Bull Game")
outer.geometry("440x240+570+290")
outer.configure(bg="#242424")
outer.mainloop()

