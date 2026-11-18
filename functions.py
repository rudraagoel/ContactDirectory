import numpy as np

from contact import Contact
from contact import SocialHandle
class ContactDirectory:
    Contacts = np.array([], dtype=object)
    def __init__(self):
        self.Contacts = np.array([], dtype=object)
    
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
            
            Split_String = social_media_array[i].split(" ")
            
            
            PLF_Name = Split_String[0] 
            Handle = Split_String[1]
            social_media_handles_array = np.append(social_media_handles_array, SocialHandle(PLF_Name, Handle))
        
            
            
        
    
    # def add_contact(self, contact):
    
ContactDirectory().create_contact()
        