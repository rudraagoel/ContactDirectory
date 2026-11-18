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
        choices = [
            Choice(title="Back to Main Menu", value="back"),
            Separator(),
            Choice(title="Search Contacts", value="search"),
            Choice(title="Sort Contacts", value="sort"),
            Separator()
        ]

        for i, contact in enumerate(self.contact_directory.Contacts):
            choices.append(Choice(title=contact.Name, value=i))

        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

        Browse = questionary.select(
            "Browse Contacts",
            choices=choices
        ).ask()

        if Browse == "back":
            pprint(CLI_UI.Start_Page(self))

        elif Browse == "search":
            query = questionary.text("Search:").ask()

            results = self.contact_directory.search_contacts(query)

            if results:
                selected = questionary.select(
                    "Search Results",
                    choices=[
                        Choice(title=c.Name, value=c.ID)
                        for c in results
                    ]
                ).ask()

                if selected is not None:
                    contact = next(
                        c for c in self.contact_directory.Contacts
                        if c.ID == selected
                    )
                    self.ShowContact(contact)
            else:
                print("No contacts found!")
                input("Press Enter to continue...")

            self.Browse_Page()

        elif Browse == "sort":
            sorting = questionary.select(
                "Sort Contacts",
                choices=[
                    Choice(title="Name (A-Z)", value="name_asc"),
                    Choice(title="Name (Z-A)", value="name_desc"),
                    Choice(title="Newest First", value="newest"),
                    Choice(title="Oldest First", value="oldest"),
                ]
            ).ask()

            if sorting is not None:
                self.contact_directory.sort_contacts(sorting)

            self.Browse_Page()

        elif isinstance(Browse, int):
            self.ShowContact(
                self.contact_directory.Contacts[Browse]
            )

    def ShowContact(self, contact):
        
        
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

        print("Name: " + contact.Name)
        print(f"Birthday: {contact.Birthday if contact.Birthday else 'Not specified'}")
        print("Phone Number: " + f"{contact.Phone_Number}")
        print("Email: " + contact.EMAIL)
        print("Address: " + contact.Address)
        print("Company Title: " + contact.Company_Title)
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
                
        
        
def run():
    CLI_UI().Start_Page()


if __name__ == "__main__":
    run()
    

