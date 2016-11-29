'''
Created on Jun 14, 2016

@author: thanh.viet.le
'''

class Email(object):
    
    def __init__(self, email_from = "", email_to = "", title = "", content = ""):
        self.email_from = email_from
        self.email_to = email_to
        self.title = title
        self.content = content
        