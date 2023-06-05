from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)


re = ""
nums=["","","",""]
def number1(event):
    calculadora("1")

def number2(event):
    return calculadora("2")

def number3(event):
    return calculadora("3")

def number4(event):
    return calculadora("4")

def number5(event):
    return calculadora("5")

def number6(event):
    return calculadora("6")

def number7(event):
    return calculadora("7")

def number8(event):
    return calculadora("8")

def number9(event):
    return calculadora("9")

def mas(event):
    if nums[1] =="":
        i = len(nums[0])+len(nums[1])+len(nums[2])
        pantalla.delete(0,i)
        nums[1] = "+"
        pantalla.insert(0,nums[0]+nums[1]+nums[2])

def menos(event):
    if nums[1] =="":
        i = len(nums[0])+len(nums[1])+len(nums[2])
        pantalla.delete(0,i)
        nums[1] = "-"
        pantalla.insert(0,nums[0]+nums[1]+nums[2])


def division(event):
    if nums[1] =="":
        i = len(nums[0])+len(nums[1])+len(nums[2])
        pantalla.delete(0,i)
        nums[1] = "/"
        pantalla.insert(0,nums[0]+nums[1]+nums[2])
    

def multi(event):
    if nums[1] =="":
        i = len(nums[0])+len(nums[1])+len(nums[2])
        pantalla.delete(0,i)
        nums[1] = "*"
        pantalla.insert(0,nums[0]+nums[1]+nums[2])
    

def igual(event):
    if nums[0]!="" and nums[1]!="" and nums[2]!="":
        if nums[1] == "+":
            n1 = float(nums[0])
            n2 = float(nums[2])
            nums[3] = n1+n2
        elif nums[1]=="-":
            n1 = float(nums[0])
            n2 = float(nums[2])
            nums[3] = n1-n2
        elif nums[1]=="*":
            n1 = float(nums[0])
            n2 = float(nums[2])
            nums[3] = n1*n2
        elif nums[1]=="/":
            n1 = float(nums[0])
            n2 = float(nums[2])
            nums[3] = n1/n2
        
        i = len(nums[0])+len(nums[1])+len(nums[2])
        pantalla.delete(0,i)
        pantalla.insert(0,str(nums[3]))


            

def punto(event):
    if nums[0] == ""  and nums[0].count(".") == 0:
        calculadora(".")
    elif nums[1] == "" and nums[0].count(".") == 0:
        calculadora(".")
    elif nums[2].count(".")==0 and nums[1]!="":
        calculadora(".")

def calculadora(numero):
    if nums[3]!="":
        pantalla.delete(0,len(str(nums[3])))
        nums[0]=""
        nums[1]=""
        nums[2]=""
        nums[3]=""
    i = len(nums[0])+len(nums[1])+len(nums[2])
    pantalla.delete(0,i)

    if nums[0] == "":
        nums[0] =nums[0]+ numero
    elif nums[1] == "":
        nums[0] =nums[0]+numero
    else:
        nums[2]=nums[2]+numero

    pantalla.insert(0,nums[0]+nums[1]+nums[2])
    return


        
        

# Configuración botones
boton_1 = Button(root,text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1  , pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)

boton_1.bind("<Button-1>",number1)
boton_2.bind("<Button-1>",number2)
boton_3.bind("<Button-1>",number3)
boton_4.bind("<Button-1>",number4)
boton_5.bind("<Button-1>",number5)
boton_6.bind("<Button-1>",number6)
boton_7.bind("<Button-1>",number7)
boton_8.bind("<Button-1>",number8)
boton_9.bind("<Button-1>",number9)
boton_igual.bind("<Button-1>",igual)
boton_punto.bind("<Button-1>",punto)
boton_mas.bind("<Button-1>",mas)
boton_menos.bind("<Button-1>",menos)
boton_multiplicacion.bind("<Button-1>",multi)
boton_division.bind("<Button-1>",division)

root.mainloop()