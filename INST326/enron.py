"""Use regular expressions to parse emails in a txt file.
"""
import re
from argparse import ArgumentParser
import sys

class Server: 
    """Stores the data for all emails found in the dataset
    
    Attributes: 
        emails: a list of email objects
    """
    
    def __init__(self, path):
        """Stores the data for all emails found in the dataset
        
        Args: 
            path: path to the file
        """
        self.path = path
        self.emails = []
        
        with open(path, 'r') as f:
            file = f.read()
            
            #seperate file into single emails
            emailList = file.split("End Email")
        
        for email in emailList:
            message_id = re.search(r"Message-ID: <(.+)>", email)
            
            #NoneType is found before being used
            if message_id == None:
                message_id = ' '
            else:    
                message_id = message_id.group(1)
                
            date = re.search(r"Date: (.+)", email)
            if date == None:
                date = ' '
            else:    
                date = date.group(1)
                
            subject = re.search(r"Subject: (.+)", email)
            if subject == None:
                subject = ' '
            else:    
                subject = subject.group(1)
                
            sender = re.search(r"From: (\w*.\w*.\w*.com)", email)
            if sender == None:
                sender = ' '
            else:    
                sender = sender.group(1)
                
            receiver = re.search(r"To: (\w*.\w*.\w*.com)", email)
            if receiver == None:
                receiver = ' '
            else:    
                receiver = receiver.group(1)
                
            #everything bt filename and end email
            body = re.search(r"FileName: .+((.*\n?)+\n)", email)
            if body == None:
                body = ' '
            else:    
                body = body.group(1)
        
            self.emails.append(Email(message_id, date, subject, sender, receiver, body))
        
class Email: 
    """Stores the data related to individual email messages
    
    Attributes: 
        message_id(str): message id of each email 
        date(str): date associated with each email
        subject(str): subject of each email
        sender(str): sender of each email 
        receiver(str): reciever of each email
        body(str): body of each email
    """
    
    def __init__(self, message_id, date, subject, sender, receiver, body):
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body

 
def main(path):
    """ Creates an instance of Server class using path
    
    Args: 
        path(str): path to the file
    
    Returns: 
        An integer, length of the emails attribute
    """
    serverObj = Server(path)
    return len(serverObj.emails[1:])
    
def parse_args(args_list):
    """ Creates an instance of ArguemntParser class and 
    uses add_argument() method to add arguments
    
    Args: 
        args_list(str): list of stringss containing command line args
    
    Returns: 
        An instance of ArguemntParser() with args_list passed in 
    """
    parser = ArgumentParser()
    
    parser.add_argument('path', type = str, help="Path of the File")
    args = parser.parse_args(args_list)
    
    return args

    
if __name__ == "__main__":
  args = parse_args(sys.argv[1:])
  main(args.path)