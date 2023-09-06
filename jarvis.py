# Prerequisites:
# To build a virtual assistant like JARVIS, 
# you'll need to import several Python libraries and modules. 
# These libraries enable various functionalities of JARVIS. 
# Here's an overview of each library and module used in the provided code snippet:

# Now, let's detail the purpose of each library/module:
import speech_recognition as sr # speech_recognition (sr): Used for speech recognition,
#allowing JARVIS to understand voice commands.
import pyttsx3 # pyttsx3: Enables text-to-speech functionality, 
#allowing JARVIS to respond audibly.
import pywhatkit #pywhatkit: Provides various functionalities, 
# including playing music on YouTube, performing web searches, and more.
import datetime pywhatkit: #Provides various functionalities, 
# including playing music on YouTube, performing web searches, and more.
import wikipedia # datetime: Used for working with date and time, 
# enabling JARVIS to provide time-related information or schedule tasks.
import smtplib # smtplib: Used for sending emails through the Simple Mail Transfer Protocol (SMTP). 
# JARVIS can send emails on behalf of the user.
import webbrowser # webbrowser: Provides functionality to open web pages in a default web browser, 
# useful for web-related tasks.
import pyaudio #pyaudio: Necessary for audio input and output operations, 
# crucial for speech recognition and text-to-speech functionalities.
from email.message import EmailMessage # EmailMessage: A class from the email.message 
# module for creating and formatting email messages.
import subprocess as sp # subprocess (sp): Used to create and manage additional processes, 
# which can be helpful for various system-related tasks.
import os # os: The os module provides a way to interact with the operating system, 
# enabling JARVIS to perform file and system operations.

# These libraries and modules serve as the foundation for building a basic virtual assistant like JARVIS in Python. 
# Depending on the specific functionalities you want to implement, 
# you may also need additional libraries and modules to extend its capabilities.
  
# Initialize speech recognition and text-to-speech engine:
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice property for the text-to-speech engine:
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Define the "talk" function to speak out text:
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Define the "take_command" function to take voice commands:
# Open a microphone as the audio source.
# Adjust for ambient noise.
# Listen for voice input.
# Recognize and process the voice input.
# Check if "jarvis" is mentioned in the command.
# Return the processed command.

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

# Define the "greet" function to greet the user based on the time of day:
# Get the current hour.
# Check the time of day (morning, afternoon, evening).
# Greet the user accordingly.
# Introduce as "Jarvis."
# Start the main script execution.
# Call the "greet" function to welcome the user. 
# Enter an infinite loop to continuously listen for user commands.
def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning!")
    elif 12 <= hour < 18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
    talk("I am Jarvis. Please tell me how can I help you.")

if __name__ == "__main__":
    greet()
    while True:
        # Take a voice command using the "take_command" function
        command = take_command()
        print(command)

# Take a voice command using the "take_command" function:

# Handle user's commands:
def run_jarvis():
    command = take_command()
    print(command)

    # Check the user's command
    if 'tell me about yourself' in command:
        print('''  
        Greetings, I'm JARVIS, your virtual artificial intelligence assistant.
        I'm at your service around the clock, ready to assist you with a wide range of tasks every day, all week long.
        ''')
        talk('''  
        Greetings, I'm JARVIS, your virtual artificial intelligence assistant.
        I'm at your service around the clock, ready to assist you with a wide range of tasks every day, all week long.
        ''')

# if the command involves asking questions, then:
# Check the user's command:
# If the command starts with "what is," "how to," "when did," "why did," or "how could," then:
# Extract the query from the command.
# Search Wikipedia for information related to the query.
# Print the information and speak it using the "talk" function.

    
    elif 'what is' in command:
    	result = command.replace('what is', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'how to' in command:
	    result = command.replace('how to', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'when did' in command:
	    result = command.replace('when did', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'why did' in command:
	    result = command.replace('why did', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'how could' in command:
	    result = command.replace('how could', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'whom did' in command:
	    result = command.replace('whom did', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'what could' in command:
	    result = command.replace('what could', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'where was' in command:
	    result = command.replace('where was', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'who is' in command:
	    result = command.replace('who is', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'why do' in command:
	    result = command.replace('why do', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'how can' in command:
	    result = command.replace('how can', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'when will' in command:
	    result = command.replace('when will', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'where should' in command:
	    result = command.replace('where should', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'what would' in command:
	    result = command.replace('what would', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'which one' in command:
	    result = command.replace('which one', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'who should' in command:
	    result = command.replace('who should', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'how might' in command:
	    result = command.replace('how might', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'when can' in command:
	    result = command.replace('when can', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'why would' in command:
	    result = command.replace('why would', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'where might' in command:
	    result = command.replace('where might', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'which way' in command:
	    result = command.replace('which way', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'who could' in command:
	    result = command.replace('who could', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'how did' in command:
	    result = command.replace('how did', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'what should' in command:
	    result = command.replace('what should', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'where can' in command:
	    result = command.replace('where can', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'why should' in command:
	    result = command.replace('why should', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'which type' in command:
	    result = command.replace('which type', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'who might' in command:
	    result = command.replace('who might', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'how was' in command:
	    result = command.replace('how was', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)
	elif 'when has' in command:
	    result = command.replace('when has', '')
	    info = wikipedia.summary(result, 1)
	    print(info)
	    talk(info)

# If the command involves opening websites, then:
# determine the website to open based on the command
# integrate the url of the website
# use webbrowser.open to navigate to the website

    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        talk('Opening YouTube')

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        talk('Opening Google')

    elif 'open stackoverflow' in command:
        webbrowser.open("https://stackoverflow.com")
        talk('Opening Stack Overflow')

    elif 'open archive.is' in command:
        webbrowser.open("https://archive.is/")
        talk('Opening Archive.is')
        talk('Archive.is helps you take a permanent snapshot of a web page that will exist forever even if the original page is gone')

    elif 'open fast.com' in command:
        webbrowser.open("https://fast.com/")
        talk('Opening Fast.com')
        talk('Fast.com helps you check the current speed of your Internet connection')

    elif 'open slides.com' in command:
        webbrowser.open("https://slides.com/")
        talk('Opening Slides.com')
        talk('Slides.com helps you create pixel-perfect slide decks and broadcast your presentations to an audience of any size from anywhere')

    elif 'open screenshot.guru' in command:
        webbrowser.open("https://screenshot.guru/")
        talk('Opening Screenshot.guru')
        talk('Screenshot.guru helps you take high-resolution screenshots of web pages on mobile and desktops')

    elif 'open dictation.io' in command:
        webbrowser.open("https://dictation.io/")
        talk('Opening Dictation.io')
        talk('Dictation.io helps in accurate and quick voice recognition in your browser using Google Speech API')

    elif 'open reverse.photos' in command:
        webbrowser.open("https://reverse.photos/")
        talk('Opening Reverse.photos')
        talk('Reverse.photos helps you upload an image and find similar pictures on the web')

    elif 'open copychar.cc' in command:
        webbrowser.open("https://copychar.cc/")
        talk('Opening Copychar.cc')
        talk('Copychar.cc helps you copy special characters and emojis that aren’t on your keyboard')

    elif 'open iconfinder.com' in command:
        webbrowser.open("https://www.iconfinder.com/")
        talk('Opening Iconfinder.com')
        talk('Iconfinder.com helps you find millions of icons for all kinds of projects. Also try icons8.com and flaticon.com')

    elif 'open jotti.org' in command:
        webbrowser.open("https://virusscan.jotti.org/en")
        talk('Opening Jotti.org')
        talk('Jotti.org helps you scan any suspicious file or email attachment for viruses')

    elif 'open wolframalpha.com' in command:
        webbrowser.open("https://www.wolframalpha.com/")
        talk('Opening Wolfram Alpha')
        talk('WolframAlpha.com helps you get answers directly without searching')

    elif 'open earth.google.com' in command:
        webbrowser.open("https://earth.google.com/web/")
        talk('Opening Earth.google.com')

    elif 'open onlineocr.net' in command:
        webbrowser.open("https://www.onlineocr.net/")
        talk('Opening Onlineocr.net')
        talk('Onlineocr.net helps you recognize text from scanned PDFs – see other OCR tools')

    elif 'open wetransfer.com' in command:
        webbrowser.open("https://wetransfer.com/")
        talk('Opening Wetransfer.com')
        talk('Wetransfer.com helps you in sharing really big files online')

    elif 'open file.pizza' in command:
        webbrowser.open("https://file.pizza/")
        talk('Opening File.pizza')
        talk('File.pizza helps you in peer-to-peer file transfer over WebRTC without any middleman')

    elif 'open hundredzeros.com' in command:
        webbrowser.open("https://hundredzeros.com/")
        talk('Opening Hundredzeros.com')
        talk('Hundredzeros.com helps you download free Kindle books')

    elif 'open app.grammarly.com' in command:
        webbrowser.open("https://www.grammarly.com/")
        talk('Opening App.grammarly.com')
        talk('App.grammarly.com helps you check your writing for spelling, style, and grammatical errors')

    elif 'open similarsites.com' in command:
        webbrowser.open("https://www.similarsites.com/")
        talk('Opening Similarsites.com')
        talk('Similarsites.com helps you discover new sites that are similar to what you like already')

    elif 'open bubbl.us' in command:
        webbrowser.open("https://bubbl.us/")
        talk('Opening Bubbl.us')
        talk('Bubbl.us helps you create mind-maps and brainstorm ideas in the browser')

    elif 'open flightstats.com' in command:
        webbrowser.open("https://www.flightstats.com/v2")
        talk('Opening Flightstats.com')
        talk('Flightstats.com helps you track flight status at airports worldwide')

    elif 'open instructables.com' in command:
        webbrowser.open("https://www.instructables.com/")
        talk('Opening Instructables.com')
        talk('Instructables.com gives you step-by-step guides on how to build anything and everything')

    elif 'open wirecutter.com' in command:
        webbrowser.open("https://www.nytimes.com/wirecutter/")
        talk('Opening Wirecutter.com')
        talk('Wirecutter.com is the best product recommendation website on the Internet')

    elif 'open gohighbrow.com' in command:
        webbrowser.open("https://gohighbrow.com/")
        talk('Opening Gohighbrow.com')
        talk('Gohighbrow.com helps you take bite-sized courses on a variety of topics, with chapters delivered by email every morning')

# If the command involves opening software applications, then:
# Determine the software to open based on the command.
# Construct the path to the software executable.
# Use the "os.startfile" function to open the software.
    
    elif 'open clock' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\clock.exe"
            os.startfile(path)
            print('opening clock')
            talk('opening clock')
            
    elif 'open calculator' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\calculator.exe"
            os.startfile(path)
            print('opening calculator')
            talk('opening calculator')

    elif 'open camera' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\camera.exe"
            os.startfile(path)
            print('opening camera')
            talk('opening camera')

    elif 'open notepad' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\notepad.exe"
            os.startfile(path)
            print('opening notepad')
            talk('opening notepad')

    elif 'open ms office' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftoffice.exe"
            os.startfile(path)
            print('opening ms office')
            talk('opening ms office')

    elif 'open skype' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\skype.exe"
            os.startfile(path)
            print('opening skype')
            talk('opening skype')

    elif 'open teams' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftteams.exe"
            os.startfile(path)
            print('opening teams')
            talk('opening teams')

    elif 'open zoom' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\zoomclient.exe"
            os.startfile(path)
            print('opening zoom')
            talk('opening zoom')

    elif 'open chime' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\chimeapp.exe"
            os.startfile(path)
            print('opening chime')
            talk('opening chime')

    elif 'open anydesk' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\anydeskclient.exe"
            os.startfile(path)
            print('opening anydesk')
            talk('opening anydesk')

    elif 'open maps' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\mapsviewer.exe"
            os.startfile(path)
            print('opening maps')
            talk('opening maps')

    elif 'open mail' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\mailclient.exe"
            os.startfile(path)
            print('opening mail')
            talk('opening mail')

    elif 'open edge' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftedge.exe"
            os.startfile(path)
            print('opening edge')
            talk('opening edge')

    elif 'open chrome' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\googlechrome.exe"
            os.startfile(path)
            print('opening chrome')
            talk('opening chrome')

    elif 'open firefox' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\mozillafirefox.exe"
            os.startfile(path)
            print('opening firefox')
            talk('opening firefox')

    elif 'open gallery' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\imageviewer.exe"
            os.startfile(path)
            print('opening image viewer')
            talk('opening image viewer')

    elif 'open videos' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\videoplayer.exe"
            os.startfile(path)
            print('opening video player')
            talk('opening video player')

    elif 'open songs' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\mymusics"
            os.startfile(path)
            print('opening my musics')
            talk('opening my musics')

    elif 'open recorder' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\voicerecorder.exe"
            os.startfile(path)
            print('opening voice recorder')
            talk('opening voice recorder')

    elif 'open store' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftstore.exe"
            os.startfile(path)
            print('opening microsoft store')
            talk('opening microsoft store')

    elif 'open xbox' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\xboxclient.exe"
            os.startfile(path)
            print('opening xbox')
            talk('opening xbox')

    elif 'open weather' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\weatherclient.exe"
            os.startfile(path)
            print('opening weather')
            talk('opening weather')

    elif 'open mcafee' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\mcafeeantivirus.exe"
            os.startfile(path)
            print('opening mcafee')
            talk('opening mcafee')

    elif 'open spotify' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\spotify.exe"
            os.startfile(path)
            print('opening spotify')
            talk('opening spotify')

    elif 'open steam' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\steamgaming.exe"
            os.startfile(path)
            print('opening steam')
            talk('opening steam')

    elif 'open dropbox' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\dropboxclient.exe"
            os.startfile(path)
            print('opening dropbox')
            talk('opening dropbox')

    elif 'open pdf reader' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\adobeacrobat.exe"
            os.startfile(path)
            print('opening pdf reader')
            talk('opening pdf reader')

    elif 'open word' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftword.exe"
            os.startfile(path)
            print('opening word')
            talk('opening word')

    elif 'open powerpoint' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftpowerpoint.exe"
            os.startfile(path)
            print('opening powerpoint')
            talk('opening powerpoint')

    elif 'open excel' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftexcel.exe"
            os.startfile(path)
            print('opening excel')
            talk('opening excel')

    elif 'open clipchamp' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\clipchampeditor.exe"
            os.startfile(path)
            print('opening clip champ')
            talk('opening clip champ')

    elif 'open audacity' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\audacityutils.exe"
            os.startfile(path)
            print('opening audacity')
            talk('opening audacity')

    elif 'open bleachbit' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\bleachbitcleaner.exe"
            os.startfile(path)
            print('opening bleachbit')
            talk('opening bleachbit')

    elif 'open blender' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\blendergraphics.exe"
            os.startfile(path)
            print('opening blender')
            talk('opening blender')
            
    elif 'open cpu z' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\cpuzscans.exe"
            os.startfile(path)
            print('opening cpu z')
            talk('opening cpu z')

    elif 'open gimp' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\gimpeditor.exe"
            os.startfile(path)
            print('opening gimp')
            talk('opening gimp')

    elif 'open davinci resolve' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\davinciresolvecommunity.exe"
            os.startfile(path)
            print('opening davinci resolve')
            talk('opening davinci resolve')

    elif 'open vs code' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftvscode.exe"
            os.startfile(path)
            print('opening vs code')
            talk('opening vs code')

    elif 'open everything tool' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\everything_voidtools.exe"
            os.startfile(path)
            print('opening everything tool')
            talk('opening everything tool')

    elif 'open glary' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\glaryutilities.exe"
            os.startfile(path)
            print('opening glary')
            talk('opening glary')

    elif 'open google earth' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\googleearthpro.exe"
            os.startfile(path)
            print('opening google earth')
            talk('opening google earth')

    elif 'open greenshot' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\greenshotutils.exe"
            os.startfile(path)
            print('opening greenshot')
            talk('opening greenshot')

    elif 'open handbrake' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\handbraketranscode.exe"
            os.startfile(path)
            print('opening handbrake')
            talk('opening handbrake')

    elif 'open hardware info' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\hwinfodiognostics.exe"
            os.startfile(path)
            print('opening hardware info')
            talk('opening hardware info')

    elif 'open seven zip' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\7ziputilities.exe"
            os.startfile(path)
            print('opening seven zip')
            talk('opening seven zip')

    elif 'open obs studio' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\obsstudiosetup.exe"
            os.startfile(path)
            print('opening obs studio')
            talk('opening obs studio')

    elif 'open rufus' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\rufustoolkit.exe"
            os.startfile(path)
            print('opening rufus')
            talk('opening rufus')

    elif 'open virtual box' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\oraclevmsetup.exe"
            os.startfile(path)
            print('opening virtual box')
            talk('opening virtual box')

    elif 'open vmware' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\vmwareenvsetup.exe"
            os.startfile(path)
            print('opening vmware')
            talk('opening vmware')

    elif 'open cmd' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\microsoftcmdprompt.exe"
            os.startfile(path)
            print('opening command prompt')
            talk('opening command prompt')

    elif 'open blue stacks' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\bluestackssetuptools.exe"
            os.startfile(path)
            print('opening blue stacks')
            talk('opening blue stacks')

    elif 'open tor' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\torbrowser.exe"
            os.startfile(path)
            print('opening tor browser')
            talk('opening tor browser')

    elif 'open veracrypt' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\veracryptsec.exe"
            os.startfile(path)
            print('opening veracrypt')
            talk('opening veracrypt')

    elif 'open screen copy' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\scrcpysetup.exe"
            os.startfile(path)
            print('opening screen copy')
            talk('opening screen copy')

    elif 'open vnc' in command:
            path = "C:\\Users\\Windows\\AppData\\Local\\Programs\\vncclientexe"
            os.startfile(path)
            print('opening vnc')
            talk('opening vnc')
    else:
        talk('Please repeat the command.')


# If the command contains the word "time," then:
# Get the current time.
# speak the current time using the "talk" function.

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

# If the command involves sending an email:
# Define a "send_email" function to send emails.
# Ask the user for the recipient's name.
# Look up the recipient's email address from a predefined email list.
# Ask for the email subject and message content.
# Send the email and confirm its sending.
# Ask if the user wants to send more emails.

    def send_email(receiver, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Make sure to enable "Allow less secure apps" in your Google account settings
        server.login('Sender_Email', 'Sender_Email_password')
        email = EmailMessage()
        email['From'] = 'Sender_Email'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
        server.quit()
    except Exception as e:
        print(e)

# Define a dictionary for storing email addresses
email_list = {
     'Robert' : 'tony@starindustries.com',
     'Steve'  : 'cpt.rogers@shieldsecurity.com',
     'Bruce' : 'hulkmode@greensquad.com',
     'Scott'  : 'lang.s@quantumtech.com'
}

# Define a function to obtain user input (e.g., via voice or text input)
def get_info():
    pass

# Function to get email-related information from the user
def get_email_info():
    talk('To whom do you want to send an email?')
    name = get_info()
    receiver = email_list.get(name)
    
    if receiver:
        talk(f'Sending email to {name}.')
        talk('What is the subject of your email?')
        subject = get_info()
        talk('Tell me the text in your email.')
        message = get_info()
        send_email(receiver, subject, message)
        talk('Hey, your email has been sent!')
        talk('Do you want to send more email?')
        send_more = get_info()
        if 'yes' in send_more.lower():
            get_email_info()
        else:
            talk('Okay, no more emails to send.')
    
# If the command does not match any recognized patterns, then:
# Print an error message.
# Talk an error message.
# End of the loop.

    else:
        talk(f"Sorry, I couldn't find an email address for {name}. Please check the name and try again.")


# Repeat the loop for continuous user interaction:
while True:
    run_jarvis()


# End of the script
