from tkinter import *



class Pizza:
    def __init__(self):
        window = Tk()
        window.title("Pizza Shop")
        
       
      


       

        frame1 = Frame(window)
        frame1.pack()
        

        


        Label(frame1, text = "Pizza Shop").grid(row = 1, column = 3, pady = 20)

        frame2 = Frame(window)
        frame2.pack()
        
        #create radio buttons for pizza size
        self.v1 = IntVar()
        self.v1.set(1)  # initializing the choice
        Label(frame2, text = "Choose Pizza Size:").grid(row = 1, column = 1, sticky = W)
        
        Radiobutton(frame2, text = "Small",variable = self.v1, value = 1).grid(row = 2, column = 2,sticky = W)
        
        
        Radiobutton(frame2, text = "Medium",variable = self.v1, value = 2).grid(row = 3, column = 2,sticky = W)

       
        Radiobutton(frame2, text = "Large",variable = self.v1, value = 3).grid(row = 4, column = 2,sticky = W)



        #create radio buttons for crust
        self.v2 = IntVar()
        self.v2.set(1)  # initializing the choice
        Label(frame2, text = "Choose Pizza Crust:").grid(row = 1, column = 4)
        
        Radiobutton(frame2, text = "Original",variable = self.v2, value = 1).grid(row = 2,padx = 6, column = 5, sticky = W)

        
        Radiobutton(frame2, text = "Pan",variable = self.v2, value = 2).grid(row = 3,padx = 6, column = 5, sticky = W)

       
        Radiobutton(frame2, text = "Thin",variable = self.v2, value = 3).grid(row = 4,padx = 6, column = 5, sticky = W)


        # create label for checkbutton
        Label(frame2, text = "Choose Toppings:").grid(row = 5,column = 1)




        # create variables and checkbuttons for toppings
        self.pep = IntVar()
        self.pep.set(0)
        Checkbutton(frame2, text = "Pepperoni", variable = self.pep).grid(row = 6, padx = 6,pady = 6,column = 2, sticky = W)
        
        self.sausage = IntVar()
        self.sausage.set(0)
        Checkbutton(frame2, text = "Sausage", variable = self.sausage).grid(row = 6,padx = 6,pady = 6, column = 3, sticky = W)
        
        self.ham = IntVar()
        self.ham.set(0)
        Checkbutton(frame2, text = "Ham", variable = self.ham).grid(row = 6, padx = 6,pady = 6,column = 4, sticky = W)
        
        self.bacon = IntVar()
        self.bacon.set(0)
        Checkbutton(frame2, text = "Bacon", variable = self.bacon).grid(row = 6,padx = 6,pady = 6, column = 5 , sticky = W)
        
        self.peppers = IntVar()
        self.peppers.set(0)
        Checkbutton(frame2, text = "Peppers", variable = self.peppers).grid(row = 7,padx = 6,pady = 6, column = 2, sticky = W)
        
        self.olives = IntVar()
        self.olives.set(0)
        Checkbutton(frame2, text = "Olives", variable = self.olives).grid(row = 7,padx = 6,pady = 6, column = 3, sticky = W)
        
        self.mush = IntVar()
        self.mush.set(0)
        Checkbutton(frame2, text = "Mushrooms", variable = self.mush).grid(row = 7,padx = 6,pady = 6, column = 4, sticky = W)
        
        self.onions = IntVar()
        self.onions.set(0)
        Checkbutton(frame2, text = "Onions", variable = self.onions).grid(row = 7,padx = 6,pady = 6, column =5 , sticky = W)


        # extra items checkboxes

       

        
        # creat label for extra items
        Label(frame2, text = "Extra Items:").grid(row = 9, column = 1,sticky =  W)

        # create checkbuttons for extra items
        self.bread = IntVar()
        self.bread.set(0)
        Checkbutton(frame2, text = "Cheese Bread", variable = self.bread).grid(row = 10, padx = 6,pady = 26,column = 2)
        self.wings = IntVar()
        self.wings.set(0)
        Checkbutton(frame2, text = "Wings", variable = self.wings).grid(row = 10,padx = 6,pady = 26, column = 3)
        self.rolls = IntVar()
        self.rolls.set(0)
        Checkbutton(frame2, text = "Cinnamon Rolls", variable = self.rolls).grid(row = 10,padx = 6,pady = 26, column = 4)



        #__________________________________________________________________________________________________________________

        # create name label
        Label(frame2, text = "Name:").grid(row = 11, column = 1,padx = 6,pady = 16, sticky = W)

        
         # create textbox
        self.name = StringVar()
        Entry(frame2, textvariable = self.name).grid(row = 11, column = 2)
        
        # create address label
        Label(frame2, text = "Address:").grid(row = 11, column = 3,padx = 6,pady = 16, sticky = W)

        
         # create address textbox
        self.address = StringVar()
        Entry(frame2, textvariable = self.address).grid(row = 11, column = 4)


        
         # create city label
        Label(frame2, text = "City:").grid(row = 12, column = 1,padx = 3,pady =16, sticky = W)

        
         # create textbox
        self.city = StringVar()
        Entry(frame2, textvariable = self.city).grid(row = 12, column = 2)


        # create state label
        Label(frame2, text = "State:").grid(row = 12, column =4,padx = 3,pady =5, sticky = W)

        
         # create textbox
        self.state = StringVar()
        Entry(frame2, textvariable = self.state, width = 4).grid(row = 12, column = 4, padx = 3,pady = 5,)


        # create zip label
        Label(frame2, text = "Zip:").grid(row = 13, column =1, padx = 3,pady =5 , sticky = W)

        
         # create textbox
        self.zip = StringVar()
        Entry(frame2, textvariable = self.zip, width = 9).grid(row = 13, column = 2, padx = 3,pady = 5,)

         # create phone label
        Label(frame2, text = "Phone Number:").grid(row = 13, column = 3,padx = 6,pady = 20, sticky = W)

        
         # create textbox
        self.phone = StringVar()
        Entry(frame2, textvariable = self.phone).grid(row = 13, column = 4)
        

        
        #_______________________________________________________________________________________________________________










        # create label variable and label
        self.total = StringVar()
        Label(frame2,textvariable = self.total).grid(row = 15,padx = 6,pady = 6, column = 2)



        
        
        
                
        # create calcualtion buttons

        Button(frame2, text = "Get Total", command = self.calcTotal).grid(row = 14,padx = 6,pady = 6, column = 1,sticky = W)

        Label(frame2, text = "Total").grid(row = 14,padx = 6,pady = 6, column = 2)



        # create discount button
        Button(frame2, text = "Discount", command = self.calcDiscount).grid(row = 14, pady = 6,padx = 6, column = 3, sticky = W)

 

        
       

        self.discount = StringVar()

      
        Label(frame2, text = "Discounted Total").grid(row = 14,padx = 6,pady = 6, column = 4)
        
        Label(frame2,textvariable = self.discount).grid(row = 15,padx = 6,pady = 6, column = 4)


        # creat confirm order button & label


        
        Button(frame2, text = "Confirm Order", command = self.receipt).grid(row = 18, padx = 6, pady = 6, column = 1,sticky = W)

        Label(frame2, textvariable = self.receipt).grid(row = 18, padx = 6, pady = 6, column = 2, sticky = W)
        

        

        text = Text(window)
        text.pack()

        text.insert(END,self.name.get())








        
        
        # create windows loop
        window.mainloop()

       

    def pizzaSize(self):
        SMALL = 7.99
        MEDIUM = 10.99
        LARGE = 14.99
        
        # get pizza size total
        if self.v1.get() == 1:
            size = SMALL
            
        elif self.v1.get() == 2:
            size = MEDIUM

        elif self.v1.get() == 3:
            size = LARGE
        return size
        
 

    
    def pizzaCrust(self):

        # pizza size plus type of crust
        if self.v2.get() == 1:
            crust = 1

        elif self.v2.get() == 2:
            crust = .50

        elif self.v2.get() == 3:
            crust = 0
        return crust


    def calcToppings(self):

        toppings = 0

        if self.pep.get():
            
            toppings = toppings + 1

        if self.sausage.get():
            toppings = toppings + 1

        if self.ham.get():
            toppings = toppings + 1

        if self.bacon.get():
            toppings = toppings + 1

        if self.peppers.get():
            toppings = toppings + 1

        if self.olives.get():
            toppings = toppings + 1

        if self.mush.get():
            toppings = toppings + 1

        if self.onions.get():
            toppings = toppings + 1

        return toppings


    def calcExtra(self):

        extra = 0

        if self.bread.get():
            extra = extra + 4.99

        if self.wings.get():
            extra = extra + 6.99

        if self.rolls.get():
            extra = extra + 5.99

        return extra
    
    
    

    def calcTotal(self):

        # calculation
        total = self.pizzaCrust() + self.pizzaSize() + self.calcToppings() + self.calcExtra()
        self.total.set(format(total))




        
              
    def calcDiscount(self):
        SENIOR = .10       

        discount = float(self.total.get()) - float(self.total.get()) * SENIOR
        discount = str(round(discount, 2))

        self.discount.set(format(discount))

           
    def receipt(self):
        Text.insert(END, self.name.get) 
        print(text.get(1.0, END)) # Print current contents
        
       





Pizza()

        Radiobutton(frame2, text = "Pan",variable = self.v2, value = 2).grid(row = 3, column = 5)

       
        Radiobutton(frame2, text = "Thin",variable = self.v2, value = 3).grid(row = 4, column = 5)


        # create label for checkbutton

        Label(frame2, text = "Choose Toppings:").grid(row = 5,column = 1)




        # create variables and checkbuttons for toppings
        self.pep = IntVar()
        self.pep.set(0)
        Checkbutton(frame2, text = "Pepperoni", variable = self.pep).grid(row = 6, column = 2)
        
        self.sausage = IntVar()
        self.sausage.set(0)
        Checkbutton(frame2, text = "Sausage", variable = self.sausage).grid(row = 6, column = 3)
        
        self.ham = IntVar()
        self.ham.set(0)
        Checkbutton(frame2, text = "Ham", variable = self.ham).grid(row = 6, column = 4)
        
        self.bacon = IntVar()
        self.bacon.set(0)
        Checkbutton(frame2, text = "Bacon", variable = self.bacon).grid(row = 6, column = 5)
        
        self.peppers = IntVar()
        self.peppers.set(0)
        Checkbutton(frame2, text = "Peppers", variable = self.peppers).grid(row = 7, column = 2)
        
        self.olives = IntVar()
        self.olives.set(0)
        Checkbutton(frame2, text = "Olives", variable = self.olives).grid(row = 7, column = 3)
        
        self.mush = IntVar()
        self.mush.set(0)
        Checkbutton(frame2, text = "Mushrooms", variable = self.mush).grid(row = 7, column = 4)
        
        self.onions = IntVar()
        self.onions.set(0)
        Checkbutton(frame2, text = "Onions", variable = self.onions).grid(row = 7, column = 5)


        # extra items checkboxes

       

        
        # creat label for extra items
        Label(frame2, text = "Extra Items:").grid(row = 9, column = 1)

        # create checkbuttons for extrA items
        self.bread = IntVar()
        self.bread.set(0)
        Checkbutton(frame2, text = "Cheese Bread", variable = self.bread).grid(row = 10, column = 2)
        self.wings = IntVar()
        self.wings.set(0)
        Checkbutton(frame2, text = "Wings", variable = self.wings).grid(row = 10, column = 3)
        self.rolls = IntVar()
        self.rolls.set(0)
        Checkbutton(frame2, text = "Cinnamon Rolls", variable = self.rolls).grid(row = 10, column = 4)

        # create calcualtion buttons

        Button(frame2, text = "Get Total", command = self.calcTotal).grid(row = 12, column = 1, sticky = W)
        
        # create label variable and label
        self.total = StringVar()
        Label(frame2,textvariable = self.total).grid(row = 12, padx = 6, pady = 6,column = 2)

        # create discount button
        Button(frame2, text = "Senior Discount", command = self.calcDiscount).grid(row = 13, pady = 6, column = 1, sticky = W)
        
        
        
         # create windows loop
        window.mainloop()


        def calcTotal(self):

            # get pizza size total
            if self.v1.get() == 1:
                total += 7.99
            elif self.v1.get() == 2:
                total += 10.99
            elif self.v1.get() == 3:
                total += 14.99


            
            
       
       

        











Pizza()























