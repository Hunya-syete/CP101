class RecordKeepingAdd:
    
    def __init__(self):
        
        self.data_dict = {}

#adddata

    def dataAdd(self):
        
        shiela_key = input("\nEnter a Key (lastname/firstname): ")
        
        shiela_value = input(f"\nEnter a Value [{shiela_key}]: ")
        
        self.data_dict[shiela_key] = shiela_value
        print("\nData Will Be Added!!")
        
        self.displayData()
        

#deletedata

    def dataDelete(self):
        
        shiela_key = input("\nEnter a Key to Delete: ")
        
        if shiela_key in self.data_dict:
            
            del self.data_dict[shiela_key]
            
            print("\nTHE KEY HAS BEEN REMOVED!")
            
        else:
            
            print(f"\nKEY [{shiela_key}] NOT FOUND.")
            
        self.displayData()
        
#displaydata

    def displayData(self):
        
        if self.data_dict:
            
            print("\nCurrent Data:", self.data_dict)
            
        else:
            
            print("\nNO DATA AVAILABLE!")
            
    #rundata

    def rundata(self):
        
        while True:
            
            choice = input("\nChoose an option [a/b/c]: ").lower()
            
            if choice == "a":
                
                self.dataAdd()
                
            elif choice == "b":
                
                self.dataDelete()
                
            elif choice == "c":
                
                print("THANK YOU!")
                break
            
            else:
                
                print("INVALID CHOICE! PLEASE TRY AGAIN! THANKS ")


r = RecordKeepingAdd()
r.rundata()
