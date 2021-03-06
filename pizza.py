from tkinter import *



class Pizza:
    def __init__(self):
        window = Tk()
        window.title("Pizza Shop")
        
       
      


       

        frame1 = Frame(window)
        frame1.pack()
        

        


        pizzaImage = PhotoImage(file ="image/pizza2.gif")
       


        

        Label(frame1, image = pizzaImage).grid(row = 1, column = 3, pady = 20)

        frame2 = Frame(window)
        frame2.pack()
        
        #create radio buttons for pizza size
        self.v1 = IntVar()
        self.v1.set(1)  # initializing the choice
        Label(frame2, text = "Choose Pizza Size:").grid(row = 1, column = 1, sticky = W)
        
        Radiobutton(frame2, text = "Small  $7.99",variable = self.v1, value = 1).grid(row = 2, column = 2,sticky = W)

        
        Radiobutton(frame2, text = "Medium  $10.99",variable = self.v1, value = 2).grid(row = 3, column = 2,sticky = W)

       
        Radiobutton(frame2, text = "Large  $14.99",variable = self.v1, value = 3).grid(row = 4, column = 2,sticky = W)



        #create radio buttons for crust
        self.v2 = IntVar()
        self.v2.set(1)  # initializing the choice
        Label(frame2, text = "Choose Pizza Crust:").grid(row = 1, column = 4)
        
        Radiobutton(frame2, text = "Original  $1.00",variable = self.v2, value = 1).grid(row = 2,padx = 6, column = 5, sticky = W)

        
        Radiobutton(frame2, text = "Pan  $.50",variable = self.v2, value = 2).grid(row = 3,padx = 6, column = 5, sticky = W)

       
        Radiobutton(frame2, text = "Thin  No Charge",variable = self.v2, value = 3).grid(row = 4,padx = 6, column = 5, sticky = W)


        # create label for checkbutton
        Label(frame2, text = "Choose Toppings").grid(row = 5,column = 1)




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
        Checkbutton(frame2, text = "Cheese Bread  $4.99", variable = self.bread).grid(row = 10, padx = 6,pady = 26,column = 2)
        self.wings = IntVar()
        self.wings.set(0)
        Checkbutton(frame2, text = "Wings  $6.99", variable = self.wings).grid(row = 10,padx = 6,pady = 26, column = 3)
        self.rolls = IntVar()
        self.rolls.set(0)
        Checkbutton(frame2, text = "Cinnamon Rolls  $5.99", variable = self.rolls).grid(row = 10,padx = 6,pady = 26, column = 4)



        #__________________________________________________________________________________________________________________

        # create name label
        Label(frame2, text = "Name:").grid(row = 11, column = 1,padx = 2,pady = 1, sticky = W)

        
         # create textbox
        self.name = StringVar()
        Entry(frame2, textvariable = self.name).grid(row = 11, column = 2)
        
         # label for summary
        Label(frame2, text = "Summary").grid(row = 11,column = 4, sticky = E)

        

        #______________________________________________________________________________________________
        
         # create name label
        Label(frame2, text = "Address:").grid(row = 12, column = 1,padx = 1,pady = 1, sticky = W)

        
         # create textbox
        self.address = StringVar()
        Entry(frame2, textvariable = self.address).grid(row = 12, column = 2)

       

         # label and variable for total in summary area
        self.total = StringVar()
        Label(frame2, text = "Subtotal").grid(row = 12, column = 4, sticky = W)
        Label(frame2, textvariable = self.total).grid(row = 12, column = 5,sticky = W)

        #__________________________________________________________________________________________

         # create name label
        Label(frame2, text = "Phone:").grid(row = 13, column = 1,padx = 1,pady = 1, sticky = W)


        


         # label for discount in summary
        self.difference = StringVar()

        Label(frame2, text = " -").grid(row = 13, column = 4, sticky = E)
        Label(frame2, textvariable = self.difference).grid(row = 13, column = 5, sticky = W)



        
        
         # create textbox
        self.phone = StringVar()
        Entry(frame2, textvariable = self.phone).grid(row = 13, column = 2)
        
        


         # label for total in summary 
        Label(frame2, text = "Total").grid(row = 14, column = 4, sticky = W)

        # label for new total after discount
        self.discount = StringVar()
        Label(frame2, textvariable = self.discount).grid(row = 14, column = 5, sticky = W)
        
        #_______________________________________________________________________________________________________________










      



        
        
        
              
        # create calcualtion buttons

        Button(frame2,text = "Checkout" , command = self.calcTotal).grid(row = 14,padx = 6,pady = 6, column = 1,sticky = W)

       


       

      
       

        # create discount button
        Button(frame2, text = "Discount", command = self.calcDiscount).grid(row = 15, pady = 6,padx = 6, column = 1, sticky = W)

        

        
       
    
        


              
         #create new frame
        frame3 = Frame(window)
        frame3.pack() 

        

      
        
       

       

       

        
        

       

       

       

        
        







        
        
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

        # calculate discount for senoirs
        discount = float(self.total.get()) - float(self.total.get()) * SENIOR
        discount = float(round(discount, 2))

        
        self.discount.set(format(discount))

        # calculates the differnce so it can display in the label
        difference = float(self.total.get()) * SENIOR

        difference = float(round(difference,2))
        
        self.difference.set(format(difference))

           
    
    
        
Pizza()
