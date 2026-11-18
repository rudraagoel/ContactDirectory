import numpy as np

from contact import Contact
from contact import SocialHandle
import contact
import contact
import uuid as uid
class ContactDirectory:
    Contacts = np.array([], dtype=object)
    def __init__(self):
        self.Contacts = np.array([], dtype=object)
    def add_contact(self, NAME, ID, PHONE_NUMBER, EMAIL, ADDRESS, NOTES, SOCIAL_MEDIA_HANDLES):
            contact = Contact(NAME,ID, PHONE_NUMBER, EMAIL, ADDRESS, NOTES, SOCIAL_MEDIA_HANDLES)
            
            self.Contacts = np.append(self.Contacts, contact)
            print("Contact Added Successfully!")
            print("Name: " + contact.Name)
            print(contact.ID)
    def create_contact(self):
        Name = input("Enter Name: ")
        Phone_Number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        Address = input("Enter Address: ")
        Notes = input("Enter Notes ( Seperated by ;): ")
        notes_array = np.array(Notes.split(";"), dtype=str)
        
        SocialMediaHandles = input("Enter Social Media Handles (Example: 'TWITTER RUDRAGOELGGG', seperated by comma): ")
        social_media_array = np.array(SocialMediaHandles.split(","), dtype=str)
        social_media_handles_array = np.array([], dtype=object)
        for i in range(len(social_media_array)):
            
                social_media_array[i].strip()
                Split_String = social_media_array[i].split(" ")
                
                
                if len(Split_String) >= 2:
                    PLF_Name = Split_String[0]
                    Handle = Split_String[1]
                    social_media_handles_array = np.append(social_media_handles_array, SocialHandle(PLF_Name, Handle))

        self.add_contact(Name, uid.uuid4(), Phone_Number, email, Address, notes_array, social_media_handles_array)
            
        
    
ContactDirectory().create_contact()


        