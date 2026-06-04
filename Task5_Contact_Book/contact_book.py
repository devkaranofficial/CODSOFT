contacts = []


def display():
    if total_contacts != 0:
        print("Contact Book:")
        for i in range(total_contacts):
            print(f"\n==============Contact{i+1}==============")
            print(f"Name           : {contacts[i]['Name']}\n")
            print(f"Contact_Number : {contacts[i]['Phone_Number']}\n")
            print(f"Email          : {contacts[i]['Email']}\n")
            print(f"Address        : {contacts[i]['Address']}\n")
    else:
        print("The Contact Book is Empty!\n")

def add_contact(name , phone_no , email , address):
    contact_data = {}
    contact_data["Name"] = name
    contact_data["Phone_Number"] = phone_no
    contact_data["Email"] = email
    contact_data["Address"] = address
    contacts.append(contact_data)
    print("Contact Added SuccessFully!\n")

def search(contact_name):
    y = 0
    all_contacts = len(contacts)
    for i in range(all_contacts):
        if contact_name in contacts[i]["Name"].lower():
            y = 1
            index = i
            break
    if y == 1:
        print(f"Contact is Present in Contact Book! at Index{index + 1}\n")
        print(f"==============Contact{index+1}==============")
        print(f"Name           : {contacts[index]['Name']}\n")
        print(f"Contact_Number : {contacts[index]['Phone_Number']}\n")
        print(f"Email          : {contacts[index]['Email']}\n")
        print(f"Address        : {contacts[index]['Address']}\n")
    else:
        print("Contact Not Found!\n")
    
        
def update_contact(contact_sno):
    if contact_sno >= 0 and contact_sno < total_contacts:
        new_name = input("Enter New name:")
        new_number = input("Enter New Number:")
        if not(new_number.isdigit()) or len(new_number) != 10:
            print("Enter Valid Digits (Lenght-10digits!\n)")
            return 
        new_email = input("Enter New Email:")
        new_address = input("Enter New Address:")
        contacts[contact_sno]["Name"] = new_name
        contacts[contact_sno]["Phone_Number"] = new_number
        contacts[contact_sno]["Email"] = new_email
        contacts[contact_sno]["Address"] = new_address
        print("Contact Updated Successfully!\n")
    else:
        print(f"Enter Valid S.no.(1-{total_contacts})")

def delete_contact(contact_sno):
    if contact_sno >= 0 and contact_sno < total_contacts:
        del contacts[contact_sno]
        print("Contact Deleted Successfully!\n")
    else:
        print(f"Enter Valid S.no.(1-{total_contacts})")


def menu():
    print("==================Contact_Book===================")
    print("1)Display Contacts")
    print("2)Add Contact")
    print("3)Update Contact")
    print("4)Search_contact")
    print("5)Delete_Contact")
    print("6)Exit")


while True:
    total_contacts = len(contacts)
    menu()
    try:
        choice = int(input("Enter Your Choice:"))
    except ValueError:
        print("Enter Valid Input(1-6)")
        continue

    #Exit
    if choice == 6:
        print("Program Exited Succesfully!\n")
        break

    #DIsplaying
    elif choice == 1:
        display()

    #Addition
    elif choice == 2:
        name = input("Enter Contact Name:")
        
        phone_number = input("Enter Phone Number:")
        if not(phone_number.isdigit()) or len(phone_number) != 10:
            print("Enter Valid Digits (Lenght-10digits!\n)")
            continue 
        email = input("Enter Email:")
        address = input("Enter Address:")
        add_contact(name,phone_number,email,address)

    #Updating
    elif choice == 3:
        if total_contacts != 0:
            try:
                sno = int(input("Enter S.no. of Contact:"))
            except ValueError:
                print("Enter Valid Input!")
                continue
            update_contact(sno - 1)
        else:
            print("The Contact Book Is Empty!\n")

    #Searching
    elif choice == 4:
        if total_contacts != 0:
            name = input("Enter Contact Name:")
            search(name.lower())
        else:
            print("The Contact Book Is Empty!\n")

    #Deletion
    elif choice == 5:
        if total_contacts != 0:
            try:
                sno = int(input("Enter S.no. of Contact:"))
            except ValueError:
                print("Enter Valid Input!")
                continue
            delete_contact(sno - 1)
        else:
            print("The Contact Book Is Empty!\n")

    else:
        print("Enter Valid Input(1-6)!\n")