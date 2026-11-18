from functions import ContactDirectory
from contact import Contact, SocialHandle
import uuid as uid
import numpy as np
import qrcode
import os
import subprocess
from pprint import pprint

import questionary
from questionary import Choice
from questionary import Separator
from questionary import prompt

class CLI_UI:
   
    Contact_Directory = ContactDirectory()
    current_path = "/"  
    def __init__(self):
        self.contact_directory = ContactDirectory()
        
        
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
                
                Choice(title="Close App", value="close"),
                ]
            ).ask()
        
        
        match Start:
            case "add":
                self.contact_directory.create_contact()
                CLI_UI.current_path = "/"
                pprint(CLI_UI.Start_Page(self))
                
            case "browse":
                CLI_UI.current_path = "/browse"
                pprint(CLI_UI.Browse_Page(self))
            case "close":
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

                exit()
            
    def Browse_Page(self):
        ContactIndex = {}
        choices = [Choice(title="Back to Main Menu", value=-1)]
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
        if(Browse != -1):
                    
                    CLI_UI.current_path = "/"
                    CLI_UI.ShowContact(self, contact=self.contact_directory.Contacts[Browse-1])
        else:
            
                    CLI_UI.current_path = "/"
                    pprint(CLI_UI.Start_Page(self))
    def ShowContact(self, contact):
        
        
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

        print("Name: " + contact.Name)
        
        print("Phone Number: " + f"{contact.Phone_Number}")
        print("Email: " + contact.EMAIL)
        print("Address: " + contact.Address)
        print("Notes: " + str(contact.Notes))
        print("Social Media Handles: ")
        
       
        
        for i in range(len(contact.SocialMediaHandles)):
            print(contact.SocialMediaHandles[i].PlatformName + ": " + contact.SocialMediaHandles[i].Handle)
        qr = qrcode.QRCode(border=1)
        qr.add_data(f"tel:{contact.Phone_Number}")
        qr.make(fit=True)
        qr.print_ascii(invert=True)
                
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

# better ui 
# write readme