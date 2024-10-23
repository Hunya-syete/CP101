class Record_Keeping_Add:
    
    def __init__(self):
        
        self.dataDict = {}
        
  #added data
    
    def addData(self):
        
        input_key = input("\nENTER A KEY [YOURNAME/LASTNAME]: ")
        input_value = input(f"\nENTER A VALUE OF [{input_key}] : ")
        
        self.dataDict[input_key] = input_value
        
        print("\nDATA ADDED!!")
        

        self.displayData()
        
    
  #delete data
    
    def deleteData(self):
        
        input_key = input("\nENTER A KEY TO DELETE: ")
        
        if input_key in self.dataDict:
            
            del self.dataDict[input_key]
            
            print("\nTHE KEY WILL BE REMOVED!")
            
        else:
            
            print(f"\nKEY {input_key} REMOVED.")
            
            self.displayData()
         
         
    #displaying data
    
    def displayData(self):
        
        if self.dataDict:
            
            print("\nCURRENT DATA: ", self.dataDict)
            
        else:
            
            print("\nNO DATA AVAILABALE :(")
            

    #run
  
    def run(self):
        
        while True:
            
             print("\nCHOOSE AN OPTION: ")
             
             print("A. ADD DATA")
             print("B. DELETE DATA")
             print("C. END")
             
             
             
             input_choice = input("\nENTER YOUR CHOICE [A/B/C]: ").upper()
             
             if input_choice == "A":
                 
                 self.addData()
                
             elif input_choice == "B":
                
                 self.deleteData()
                
             elif input_choice == "C":
                
                 print("THANK YOU!")
                 break
            
             else:
                
                 print("INVALID CHOICE! PLEASE TRY AGAIN! THANKS :)")
                

r = Record_Keeping_Add()
r.run()
