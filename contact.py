import numpy as np

class Contact:
    Name = ""
   
    Phone_Number = +1-123-456-7890
    EMAIL = ""
    Address = ""
    Notes =  np.array([], dtype=str)
    SocialMediaHandles = np.array([], dtype=object)
    
    def __init__(self, Name, Phone_Number, EMAIL, Address, Notes, SocialMediaHandles):
        self.Name = Name
        self.Phone_Number = Phone_Number
        self.EMAIL = EMAIL
        self.Address = Address
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
            +1-233-255-454,
            "johnsmith@smiths.com",
            "Smith St. - House 225",
            np.append(Contact.Notes, "string"),
            np.append(Contact.SocialMediaHandles, SocialHandle("Facebook", "Boomer_JohnSmith"))
        )+
'''