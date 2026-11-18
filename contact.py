import datetime

import numpy as np
import uuid as uid

class Contact:
    Name = ""
    Birthday: datetime.datetime = None
    ID: uid = uid.uuid4()
    Phone_Number = +1-123-456-7890
    EMAIL = ""
    Address = ""
    Company_Title = "Software Engineer @ Hack Club"
    Notes =  np.array([], dtype=str)
    SocialMediaHandles = np.array([], dtype=object)
    
    def __init__(self, Name, Birthday, ID, Phone_Number, EMAIL, Address, Company_Title, Notes, SocialMediaHandles):
        self.Name = Name
        self.Birthday = Birthday
        self.ID = ID
        self.Phone_Number = Phone_Number
        self.EMAIL = EMAIL
        self.Address = Address
        self.Company_Title = Company_Title
        self.Notes = Notes
        self.SocialMediaHandles = SocialMediaHandles
        
        
    
    
class SocialHandle:
    PlatformName = ""
    Handle = ""
    def __init__(self, PlatformName, Handle):
        self.PlatformName = PlatformName
        self.Handle = Handle
        
        
'''
    TEMPLATE CONTACT OBJECT
        Contact1 = Contact(
            "John Smith",
            uid.uuid4(),
            +1-233-255-454,
            "johnsmith@smiths.com",
            "Smith St. - House 225",
            np.append(Contact.Notes, "string"),
            np.append(Contact.SocialMediaHandles, SocialHandle("Facebook", "Boomer_JohnSmith"))
        )+
'''