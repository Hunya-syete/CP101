import re

print ("\033[36m=\033[0m" * 33 + "\n\t\033[35mRECORD KEEPING APP\033[0m\n" + "\033[36m=\033[0m" * 33)

def record_keeper():
    data_record_dict = {}

    def valid_id_num():
        while True:
            id_num = input("\033[34mEnter ID#\033[0m: ")
            if id_num.isdigit():
                return id_num
            else:
                print ("\033[31mInvalid\033[0m ID #, in digits only. Please try again.")

    while True:
        print ("\n\033[32mPLEASE CHOOSE AN ACTION\033[0m")
        print ("\n\033[33ma\033[0m. Add data \t\033[33mb\033[0m. Delete data")
        print ("\033[33mc\033[0m. End   \t\033[33md\033[0m. View data")

        choice = input("\n\033[32mENTER YOUR CHOICE\033[0m: ").lower()

        if choice == "a":
            name = input("\n\033[34mStudent Name\033[0m: ").upper()
            course = input("\033[34mStudent Course\033[0m: ").upper()
            id_num = valid_id_num()

            data_record_dict[id_num] = {"Name": name, "Course": course}
            print (f"\n\033[35mDATA FOR ID # {id_num} ADDED TO FILE\033[0m.")

        elif choice == "b":
            id_num = valid_id_num()
            if id_num in data_record_dict:
                del data_record_dict[id_num]
                print (f"Record for ID# {id_num} has been deleted!")
            else:
                print (f"NO record found with ID# {id_num}.")

        elif choice == "c":
            print ("\n\033[35mTHANK YOU FOR YOUR TIME!\033[0m")
            break
        
        elif choice == "d":
            if data_record_dict:
                print ("\033[36m=\033[0m" * 44 + "\n\t\033[35mCURRENT RECORDS ON FILE\033[0m\n" + "\033[36m=\033[0m" * 44)
                for id_num, details in data_record_dict.items():
                    print (f"\033[34mID#\033[0m: {id_num} \t\033[34mName\033[0m: {details["Name"]} \t\033[34mCourse\033[0m: {details["Course"]}")
            else:
                print ("\n\033[34mNO RECORDS FOUND!\033[0m")

        else:
            print ("\033[31mINVALID!\033[0m Please try again.")

record_keeper()
