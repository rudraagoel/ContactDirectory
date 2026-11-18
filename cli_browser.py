from functions import ContactDirectory
from contact import Contact, SocialHandle
import uuid as uid
import numpy as np
import os
import subprocess
from pprint import pprint

import questionary
from questionary import Choice
from questionary import Separator
from questionary import prompt

class CLI_UI:
    contact = Contact(
                    "John Smith",
                    uid.uuid4(),
                    +1-233-255-454,
                    "johnsmith@smiths.com",
                    "Smith St. - House 225",
                np.append(Contact.Notes, "string"),
                np.append(Contact.SocialMediaHandles, SocialHandle("Facebook", "Boomer_JohnSmith"))
            )
    Contact_Directory = None
    current_path = "/"
    def __init__(self):
        self.contact_directory = ContactDirectory()
        self.contact_directory.Contacts = np.append( self.contact_directory.Contacts, self.contact)
        
        
        self.current_path = "/"
    
    def Start_Page(self):
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        
        Start = questionary.select(
            "Welcome to your Contacts App! *Runs in your terminal*",
            choices=
            [
                Choice(title="Browse Contacts", value="browse"),
                Separator(),
                Choice(title="Add Contact", value="add"),
                Separator(),
                Choice(title="Search Contacts", value="search"),
                Separator(),
                Choice(title="Close App", value="close"),
                ]
            ).ask()
        
        
        match Start:
            case "browse":
                CLI_UI.current_path = "/browse"
                pprint(CLI_UI.Browse_Page(self))
            
    def Browse_Page(self):
        ContactIndex = {}
        choices = []
        for(i, contact) in enumerate(self.contact_directory.Contacts):
            ContactIndex[i] = contact
            choices.append(Choice(title=f"{contact.Name}", value=i+1))
        if len(choices) == 0:
            choices.append(Choice(title="No Contacts Found, Press enter to return to Main Menu", value=-1))
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

        Browse = questionary.select(
                "Browse Contacts",
                choices=choices
                ).ask()
        match Browse:
                case 1:
                    CLI_UI.current_path = "/"
                    CLI_UI.ShowContact(self, contact=self.contact_directory.Contacts[0])
                case -1:
                    CLI_UI.current_path = "/"
                    pprint(CLI_UI.Start_Page(self))
    def ShowContact(self, contact):
        
        
        print("Name: " + contact.Name)
        print("Phone Number: " + f"{contact.Phone_Number}")
        print("Email: " + contact.EMAIL)
        print("Address: " + contact.Address)
        print("Notes: " + str(contact.Notes))
        print("Social Media Handles: ")
        
        
        for i in range(len(contact.SocialMediaHandles)):
            print(contact.SocialMediaHandles[i].PlatformName + ": " + contact.SocialMediaHandles[i].Handle)
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

        Q = questionary.select(
            "",
            choices=
            [
                Choice(title="Back to Browse Menu", value="back"),
                Choice(title="Update Contact", value="update"),
                Choice(title="Delete Contact", value="delete"),
                
                ]
            ).ask()
        match Q:
           case "update":
                self.contact_directory.update_contact(contact.ID)
                CLI_UI.current_path = "/browse"
                pprint(CLI_UI.Browse_Page(self))
           case "back":
                CLI_UI.current_path = "/browse"
                pprint(CLI_UI.Browse_Page(self))

                
           case "delete":
                self.contact_directory.remove_contact(contact.ID)
                CLI_UI.current_path = "/browse"
                pprint(CLI_UI.Browse_Page(self))
                
        
        
pprint(CLI_UI.Start_Page(self=CLI_UI()))

# rendering browsing contacts : done
# removal of contacts: done
# add and update contacts
# match cases for close app, search contact and  add cotnact
# actively maintaining path and contact list 
# saving the contacts to a file