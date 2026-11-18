
import json
import os
import uuid as uid

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
                "ID": str(contact.ID),
                "Phone_Number": contact.Phone_Number,
                "EMAIL": contact.EMAIL,
                "Address": contact.Address,
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
                uid.UUID(item["ID"]),
                item["Phone_Number"],
                item["EMAIL"],
                item["Address"],
                item["Notes"],
                handles
            )

            self.Contacts.append(contact)

    def add_contact(self, NAME, ID, PHONE_NUMBER, EMAIL, ADDRESS, NOTES, SOCIAL_MEDIA_HANDLES):
        contact = Contact(NAME, ID, PHONE_NUMBER, EMAIL, ADDRESS, NOTES, SOCIAL_MEDIA_HANDLES)

        self.Contacts.append(contact)
        self.save_contacts()

    def create_contact(self):
        Name = input("Enter Name: ")
        Phone_Number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        Address = input("Enter Address: ")

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

        self.add_contact(Name, uid.uuid4(), Phone_Number, email, Address, notes_array, social_media_handles_array)

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

                Phone_Number = input("Enter Phone Number (empty for no change): ")

                if Phone_Number != "":
                    self.Contacts[i].Phone_Number = Phone_Number

                email = input("Enter Email (empty for no change): ")

                if email != "":
                    self.Contacts[i].EMAIL = email

                Address = input("Enter Address (empty for no change): ")

                if Address != "":
                    self.Contacts[i].Address = Address

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
