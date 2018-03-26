#coding: utf-8

"""@package docstring 
"""
from Tkinter import *
import webbrowser
import speech_recognition as sr                               

"""Create an instance of window"""
window = Tk()                                                 

window.iconbitmap(r'C:/MyVoiceek/favicon.ico')
"""set the created window's title"""
window.title('Voiceek - Google Inc.')                         

"""define an input and its size"""
entry_text = Entry(window, width=50)
"""the layout manager"""
entry_text.pack(pady=40)                                             
"""let the input-text on focus"""
entry_text.focus_set()                                        
window.geometry('470x180+200+200')

"""recognition module's instance."""
rec = sr.Recognizer()                                         

""" @brief Function to click button
    This function allows to click the button
    and verify if the it is a sum, multiply or text query.
"""
def click_button(): 
    """ Condition verifies if there is some text in the entry_text field"""
    if(entry_text.get() != ""):
        s = entry_text.get()
        for _ in s:                                           
            """for sum queries"""
            if ("+" in s):                                    
                s = s.replace('+','%2B')
                webbrowser.open('https://www.google.com/search?q='+ s, new=0)
                break    
            """for multiply queries"""
            elif ("*" in s):                                   
                s = s.replace('+','%F5')
                webbrowser.open('https://www.google.com/search?q='+ s, new=0)
                break    
            else:
            """for other queries"""  
                s = s.replace(' ','+')                        
                webbrowser.open('https://www.google.com/search?q='+ s, new=0)
                break
    """ Otherwise, the function will listen the microphone """
    else:
        entry_text.delete(0,END)
        with sr.Microphone() as speech:  
            """the listen method captures the voice sound and assigns it to variable."""
            phrase = rec.listen(speech)                  
            """translate the speech to text and print it in the entry_text field"""            
            trans = (rec.recognize_google(phrase, language="pt"))     
            s = entry_text.insert(0,trans)
            """treats the translation query and then search it at Google"""
            google_search = trans.replace(' ','+')
            webbrowser.open('https://www.google.com/search?q='+ google_search, new=0)

btn = Button(window, text='Search', width=20, command=click_button)
btn.pack()

"""draw the window and initialize the application"""
window.mainloop()                                            
