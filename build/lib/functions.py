
import json
import os
import uuid as uid
import datetime
from contact import Contact, SocialHandle


class ContactDirectory:
    def __init__(self):
        self.Contacts = []
        self.FILE_PATH = os.path.join(os.path.dirname(__file__), "contacts.json")
        self.load_contacts()

    def save_contacts(self):
        data = []

        for contact in self.Contacts:
            data.append({
                "Name": contact.Name,
                "Birthday": contact.Birthday.isoformat() if contact.Birthday else None,  
                "ID": str(contact.ID),
                "Phone_Number": contact.Phone_Number,
                "EMAIL": contact.EMAIL,
                "Address": contact.Address,
                "Company_Title": contact.Company_Title,
                "Notes": contact.Notes,
                "SocialMediaHandles": [
                    {
                        "PlatformName": handle.PlatformName,
                        "Handle": handle.Handle
                    }
                    for handle in contact.SocialMediaHandles
                ]
            })

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_contacts(self):
        if not os.path.exists(self.FILE_PATH):
            self.save_contacts()
            return

        with open(self.FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.Contacts = []

        for item in data:
            handles = [
                SocialHandle(handle["PlatformName"], handle["Handle"])
                for handle in item["SocialMediaHandles"]
            ]

            contact = Contact(
                item["Name"],
                datetime.datetime.strptime(item["Birthday"], "%Y-%m-%d").date() if item.get("Birthday") else None,
                uid.UUID(item["ID"]),
                item["Phone_Number"],
                item["EMAIL"],
                item["Address"],
                item.get("Company_Title", ""),
                item["Notes"],
                handles
            )

            self.Contacts.append(contact)

    def add_contact(self, NAME,Birthday, ID, PHONE_NUMBER, EMAIL, ADDRESS, COMPANY_TITLE, NOTES, SOCIAL_MEDIA_HANDLES):
        contact = Contact(NAME, Birthday, ID, PHONE_NUMBER, EMAIL, ADDRESS, COMPANY_TITLE, NOTES, SOCIAL_MEDIA_HANDLES)

        self.Contacts.append(contact)
        self.save_contacts()

    def create_contact(self):
        Name = input("Enter Name: ")
        Birthday = input("Enter Birthday (YYYY-MM-DD): ")
        Birthday = datetime.datetime.strptime(Birthday, "%Y-%m-%d").date() if Birthday else None
        Phone_Number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        Address = input("Enter Address: ")
        Company_Title = input("Enter Company Title: ")

        Notes = input("Enter Notes (Seperated by ;): ")
        notes_array = Notes.split(";")

        SocialMediaHandles = input("Enter Social Media Handles (Example: 'TWITTER elonmusk', seperated by comma): ")
        social_media_array = SocialMediaHandles.split(",")

        social_media_handles_array = []

        for i in range(len(social_media_array)):
            Split_String = social_media_array[i].strip().split(" ")

            if len(Split_String) >= 2:
                PLF_Name = Split_String[0]
                Handle = Split_String[1]

                social_media_handles_array.append(SocialHandle(PLF_Name, Handle))

        self.add_contact(Name, Birthday, uid.uuid4(), Phone_Number, email, Address, Company_Title, notes_array, social_media_handles_array)

    def remove_contact(self, ID):
        for i in range(len(self.Contacts)):
            if self.Contacts[i].ID == ID:
                self.Contacts.pop(i)
                self.save_contacts()
                print("Contact Removed Successfully!")
                return

        print("Contact Not Found!")

    def update_contact(self, ID):
        for i in range(len(self.Contacts)):
            if self.Contacts[i].ID == ID:
                Name = input("Enter Name (empty for no change): ")

                if Name != "":
                    self.Contacts[i].Name = Name
                Birthday = input("Enter Birthday (YYYY-MM-DD) (empty for no change): ")
                if Birthday != "":
                    self.Contacts[i].Birthday = datetime.datetime.strptime(Birthday, "%Y-%m-%d").date()

                Phone_Number = input("Enter Phone Number (empty for no change): ")

                if Phone_Number != "":
                    self.Contacts[i].Phone_Number = Phone_Number

                email = input("Enter Email (empty for no change): ")

                if email != "":
                    self.Contacts[i].EMAIL = email

                Address = input("Enter Address (empty for no change): ")

                if Address != "":
                    self.Contacts[i].Address = Address
                
                Company_Title = input("Enter Company Title (empty for no change): ")
                if Company_Title != "":
                    self.Contacts[i].Company_Title = Company_Title

                Notes = input("Enter Notes (Separated by ;) (empty for no change), end with '--' to remove previous notes: ")

                if Notes != "":
                    if Notes.strip() == "--":
                        self.Contacts[i].Notes = []
                    else:
                        self.Contacts[i].Notes = Notes.split(";")

                SocialMediaHandles = input("Enter Social Media Handles (Example: 'TWITTER RUDRAGOELGGG', separated by comma) (empty for no change), enter '--' to remove previous handles: ")

                if SocialMediaHandles != "":
                    if SocialMediaHandles.strip() == "--":
                        self.Contacts[i].SocialMediaHandles = []
                    else:
                        social_media_array = SocialMediaHandles.split(",")
                        social_media_handles_array = []

                        for j in range(len(social_media_array)):
                            Split_String = social_media_array[j].strip().split(" ")

                            if len(Split_String) >= 2:
                                PLF_Name = Split_String[0]
                                Handle = Split_String[1]

                                social_media_handles_array.append(SocialHandle(PLF_Name, Handle))

                        self.Contacts[i].SocialMediaHandles = social_media_handles_array

                self.save_contacts()
                return
    
    def search_contacts(self, query):
        query = query.lower().strip()

        return [
            contact for contact in self.Contacts
            if query in contact.Name.lower()
            or query in contact.Phone_Number.lower()
            or query in contact.EMAIL.lower()
        ]


    def sort_contacts(self, sort_by):
        if sort_by == "name_asc":
            self.Contacts.sort(key=lambda contact: contact.Name.lower())

        elif sort_by == "name_desc":
            self.Contacts.sort(key=lambda contact: contact.Name.lower(), reverse=True)

        elif sort_by == "newest":
            self.Contacts.reverse()

        elif sort_by == "oldest":
            pass

        self.save_contacts()

