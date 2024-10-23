class RecordKeepAdd:
    def __init__(self):
        self.dataDict = {}

    def addData(self):
        key = input("\nENTER A KEY [YOURNAME/LASTNAME]: ")
        value = input(f"\nENTER A VALUE OF [{key}]: ")
        self.dataDict[key] = value
        print("\nDATA ADDED!!")
        self.displayData()

    def deleteData(self):
        key = input("\nENTER A KEY TO DELETE: ")
        if key in self.dataDict:
            del self.dataDict[key]
            print("\nTHE KEY HAS BEEN REMOVED!")
        else:
            print(f"\nKEY {key} NOT FOUND.")
        self.displayData()

    def displayData(self):
        if self.dataDict:
            print("\nCURRENT DATA:", self.dataDict)
        else:
            print("\nNO DATA AVAILABLE 🙁")

    def run(self):
        while True:
            choice = input("\nCHOOSE AN OPTION:\nA. ADD DATA\nB. DELETE DATA\nC. END\nENTER YOUR CHOICE [A/B/C]: ").lower()
            if choice == "a":
                self.addData()
            elif choice == "b":
                self.deleteData()
            elif choice == "c":
                print("THANK YOU!")
                break
            else:
                print("INVALID CHOICE! PLEASE TRY AGAIN! THANKS 🙂")

if __name__ == "__main__":  # Corrected the if statement
    r = RecordKeepAdd()
    r.run()
