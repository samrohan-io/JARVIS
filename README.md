# Building JARVIS using Python.
![jarvisai](https://github.com/samrohan-io/JARVIS/assets/139897809/dbdaacd6-0733-49c7-94a4-ed0f410a1d5b)

## Introduction:
Hello everyone! I'm excited to share this moment with all of you. Many of us have dreamt of having our own personal A.I. assistant, and now that dream is becoming a reality. I've been working on developing JARVIS using Python since 2020, and although the project was put on hold for a while, I am determined to complete it in 2023 and make it an open-source endeavor for fellow A.I. enthusiasts who are eagerly waiting to create their own A.I. assistants. Before we dive deep into the project, let's take a brief look at JARVIS.

![3553059](https://github.com/samrohan-io/JARVIS/assets/139897809/514eb893-ed49-4d1d-8c06-3fb36940838c)


## J.A.R.V.I.S:
Tony Stark's personal A.I., JARVIS (Just A Rather Very Intelligent System), is a fictional but iconic artificial intelligence system featured in the Marvel Cinematic Universe (MCU). Created by Stark himself, JARVIS serves as Tony Stark's highly advanced and sophisticated digital assistant and interface for his high-tech suits and the entire Stark Industries infrastructure. Here are some key points about JARVIS:

### Origins and Development:
JARVIS was initially developed by Tony Stark's father, Howard Stark, as a rudimentary computer program. However, Tony significantly upgraded and refined the system over the years, turning it into a highly intelligent and responsive A.I.

### Capabilities:
JARVIS possesses a wide range of capabilities, including speech recognition, natural language processing, problem-solving, and the ability to control and interface with Stark's suits and various devices. It can also manage Stark's home and lab, providing security and automation.


### Integration with Iron Man Suits:
JARVIS plays a critical role in Tony Stark's superhero persona as Iron Man. It assists him in controlling and managing his suits, providing real-time data analysis, weapon systems management, and even helping him suit up and down.

### Strategic Advisor:
Beyond its technical abilities, JARVIS serves as a strategic advisor to Tony Stark, helping him make decisions and providing information on a wide range of topics. It can access vast databases, including the internet, to retrieve information.

### Influence on Real-World Technology:
The concept of JARVIS has inspired real-world advancements in artificial intelligence and voice-controlled assistants. It showcases the potential of A.I. systems to assist with complex tasks and make human-machine interaction more intuitive.

Tony Stark's JARVIS is a beloved character in the MCU, symbolizing the fusion of cutting-edge technology and human creativity. It highlights the idea that advanced A.I. systems, when used responsibly, can enhance human capabilities and improve various aspects of our lives.

![wp11132158-iron-man-lab-wallpapers](https://github.com/samrohan-io/JARVIS/assets/139897809/e02e481a-3cd3-49b2-aea8-9265b5bbfe6a)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Prerequisites:
- To build a virtual assistant like JARVIS, you'll need to import several Python libraries and modules. These libraries enable various functionalities of JARVIS. Here's an overview of each library and module used in 
 the provided code snippet:

##### Now, let's detail the purpose of each library/module:

* speech_recognition (sr):
Used for speech recognition, allowing JARVIS to understand voice commands.

* pyttsx3:
Enables text-to-speech functionality, allowing JARVIS to respond audibly.

* pywhatkit:
Provides various functionalities, including playing music on YouTube, performing web searches, and more.

* datetime:
Used for working with date and time, enabling JARVIS to provide time-related information or schedule tasks.

* wikipedia:
Allows JARVIS to fetch information from Wikipedia, enabling it to answer questions or provide information on various topics.

* smtplib:
Used for sending emails through the Simple Mail Transfer Protocol (SMTP). JARVIS can send emails on behalf of the user.

* webbrowser:
Provides functionality to open web pages in a default web browser, useful for web-related tasks.

* EmailMessage:
A class from the email.message module for creating and formatting email messages.

* subprocess (sp):
Used to create and manage additional processes, which can be helpful for various system-related tasks.

* pyaudio:
Necessary for audio input and output operations, crucial for speech recognition and text-to-speech functionalities.

* os:
The os module provides a way to interact with the operating system, enabling JARVIS to perform file and system operations.

* These libraries and modules serve as the foundation for building a basic virtual assistant like JARVIS in Python. Depending on the specific functionalities you want to implement, you may also need additional libraries and modules to extend its capabilities.
  
  
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Process flow:

#### Start: The program starts.
#### Initialize: Initialize speech recognition, text-to-speech engine, and other required components.
#### Greet User: The program greets the user based on the time of day (morning, afternoon, evening) and introduces itself as "Jarvis."

![STEP -](https://github.com/samrohan-io/JARVIS/assets/139897809/5935b816-9981-4934-a0c4-6ec2b658b9d5)


#### Listen for Commands: Enter a loop to continuously listen for voice commands.

![2](https://github.com/samrohan-io/JARVIS/assets/139897809/1c883f9b-e9af-478b-a667-cbeb81d15c5e)

#### Take Voice Command: Use the microphone to capture voice input from the user.

![3](https://github.com/samrohan-io/JARVIS/assets/139897809/a36e5eed-fc4b-4bee-8776-070070fa74a0)

#### Process Voice Command: Recognize and process the voice command. Remove the phrase "jarvis" if present.

![4](https://github.com/samrohan-io/JARVIS/assets/139897809/3c4081c7-61cc-4fa4-972f-2c3f370ee28e)

#### Execute Actions:

* Depending on the recognized command, execute specific actions (represented by empty conditions in your code). Each action should perform a specific task, such as retrieving * information, opening applications, or performing other functions.
* Speak Response: Use the text-to-speech engine to respond to the user with speech.
 
![5](https://github.com/samrohan-io/JARVIS/assets/139897809/87bffb44-a90e-4ef1-b534-f183dfa5ed1b)

#### Speak Response: Use the text-to-speech engine to respond to the user with speech.


![6](https://github.com/samrohan-io/JARVIS/assets/139897809/eaf4ce73-6c26-4942-ba0e-cab856b34718)

#### Repeat: Return to the listening state to continuously accept new commands.

![7](https://github.com/samrohan-io/JARVIS/assets/139897809/11f462af-1378-4303-b3e1-0eecda3db836)

#### End: The program ends when terminated by the user.

![8](https://github.com/samrohan-io/JARVIS/assets/139897809/c7d9f36c-2438-4dce-9097-209e71951063)




-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Instructions:

* Start

* Initialize speech recognition and text-to-speech engine.

* Set the voice property for the text-to-speech engine.

* Define the "talk" function to speak out text.

* Define the "take_command" function to take voice commands.
  * Open a microphone as the audio source.
  * Adjust for ambient noise.
  * Listen for voice input.
  * Recognize and process the voice input.
  * Check if "jarvis" is mentioned in the command.
  * Return the processed command.

* Define the "greet" function to greet the user based on the time of day:
  * Get the current hour.
  * Check the time of day (morning, afternoon, evening).
  * Greet the user accordingly.
  * Introduce as "Jarvis."
  * Start the main script execution.
  * Call the "greet" function to welcome the user.

* Enter an infinite loop to continuously listen for user commands.

* Take a voice command using the "take_command" function.
  * Check the user's command:
  * If the command starts with "what is," "how to," "when did," "why did," or "how could," then:
  * Extract the query from the command.
  * Search Wikipedia for information related to the query.
  * Print the information and speak it using the "talk" function.
 

* If the command contains the word "time," then:
  * Get the current time.
  * Speak the current time using the "talk" function.

* If the command involves sending an email, then: 
  * Define a "send_email" function to send emails.
  * Ask the user for the recipient's name.
  * Look up the recipient's email address from a predefined email list.
  * Ask for the email subject and message content.
  * Send the email and confirm its sending.
  * Ask if the user wants to send more emails.


* If the command involves opening software applications, then:
  * Determine the software to open based on the command.
  * Construct the path to the software executable.
  * Use the "os.startfile" function to open the software.


* If the command does not match any recognized patterns, then:
  * Print an error message.
  * Talk an error message.
  * End of the loop.

* Repeat the loop for continuous user interaction.
* End
  * This process flow outlines the main functionalities and decision points of the Python script, helping to illustrate how the program processes voice commands and performs various actions based on those commands.


* If you find the provided instructions unclear, please refer to the 'jarvis.py' file in the repository for the complete source code and instructions placed at the appropriate locations. You can effectively compare the instructions with the source code by viewing them side by side on your screen. I hope this helps.

### Note: 
Always remember that you must use the wake-up word 'JARVIS' before issuing any commands to the program. Failure to do so will result in the program not executing its operations correctly and may lead to errors. You have the flexibility to rename the AI assistant according to your preferences and enhance its features as needed.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Features:

![j](https://github.com/samrohan-io/JARVIS/assets/139897809/e18df54d-e831-44bd-96f2-4ff0b48fdf2c)


## Answering Questions:

Our developed JARVIS personal AI assistant excels at providing answers to various open-ended questions. You have the freedom to expand this feature by adding more questions and pre-written answers, allowing for endless possibilities limited only by your creativity. To grasp the functionality, please review the commands provided below.


  * Command 'hat is'
  * Command 'How to'
  * Command 'When did'
  * Command 'Why did'
  * Command 'How could'
  * Command 'Whom did'
  * Command 'What could'
  * Command 'Where was'
  * Command 'Who is'
  * Command 'Why do'
  * Command 'How can'
  * Command 'When will'
  * Command 'Where should'
  * Command 'What would'
  * Command 'Which one'
  * Command 'Who should'
  * Command 'How might'
  * Command 'When can'
  * Command 'Why would'
  * Command 'Where might'
  * Command 'Which way'
  * Command 'Who could'
  * Command 'How did'
  * Command 'What should'
  * Command 'Command Where can'
  * Command 'Why should'
  * Command 'Which type'
  * Command 'Who might'
  * Command 'How was'
  * Command 'When has'
  

## Navigating to Requested Websites:
Our JARVIS personal AI assistant, thoughtfully designed, smoothly opens the most valuable websites tailored to the user's needs. This feature offers flexibility as you can effortlessly incorporate numerous websites, enhancing the overall appeal and utility of your project. Your choice of websites can make your project stand out, and the possibilities are boundless. To understand how this feature works, kindly refer to the provided commands. Moreover, this feature can be customized to align precisely with your specific preferences.

 
*Command: 'open youtube'
  * Response: Opening YouTube

* Command: 'open google'
  * Response: Opening Google

* Command: 'open stackoverflow'
  * Response: Opening Stack Overflow

* Command: 'open archive.is'
  *Response:
   Opening Archive.is - 
   Archive.is helps you take a permanent snapshot of a web page that will   exist forever even if the original page is gone

* Command: 'open fast.com'
  *Response:
   Opening Fast.com - 
   Fast.com helps you check the current speed of your Internet connection

* Command: 'open slides.com'
  * Response:
   Opening Slides.com - 
   Slides.com helps you create pixel-perfect slide decks and broadcast your presentations to an audience of any size from anywhere

* Command: 'open screenshot.guru'
  * Response:
   Opening Screenshot.guru - 
   Screenshot.guru helps you take high-resolution screenshots of web pages on mobile and desktops

* Command: 'open dictation.io'
  * Response:
   Opening Dictation.io - 
   Dictation.io helps in accurate and quick voice recognition in your browser using Google Speech API

* Command: 'open reverse.photos'
  * Response:
   Opening Reverse.photos - 
   Reverse.photos helps you upload an image and find similar pictures on the web

* Command: 'open copychar.cc'
  * Response:
   Opening Copychar.cc - 
   Copychar.cc helps you copy special characters and emojis that aren’t on your keyboard

* Command: 'open iconfinder.com'
  * Response:
   Opening Iconfinder.com - 
   Iconfinder.com helps you find millions of icons for all kinds of projects. Also try icons8.com and flaticon.com

* Command: 'open jotti.org' 
  * Response:
   Opening Jotti.org - 
   Jotti.org helps you scan any suspicious file or email attachment for viruses

* Command: 'open wolframalpha.com'
  * Response:
    Opening Wolfram Alpha - 
    WolframAlpha.com helps you get answers directly without searching

* Command: 'open earth.google.com'
  * Response: Opening Earth.google.com

* Command: 'open onlineocr.net'
  * Response:
    Opening Onlineocr.net - 
    Onlineocr.net helps you recognize text from scanned PDFs – see other OCR tools

* Command: 'open wetransfer.com'
  * Response:
    Opening Wetransfer.com - 
    Wetransfer.com helps you in sharing really big files online

* Command: 'open file.pizza'
  * Response:
    Opening File.pizza - 
    File.pizza helps you in peer-to-peer file transfer over WebRTC without any middleman

* Command: 'open hundredzeros.com'
  * Response:
    Opening Hundredzeros.com - 
    Hundredzeros.com helps you download free Kindle books

* Command: 'open app.grammarly.com'
  * Response:
    Opening App.grammarly.com - 
    App.grammarly.com helps you check your writing for spelling, style, and grammatical errors

* Command: 'open similarsites.com'
  * Response:
    Opening Similarsites.com - 
    Similarsites.com helps you discover new sites that are similar to what you like already

* Command: 'open bubbl.us'
  * Response:
    Opening Bubbl.us - 
    Bubbl.us helps you create mind-maps and brainstorm ideas in the browser

* Command: 'open flightstats.com'
  * Response:
    Opening Flightstats.com - 
    Flightstats.com helps you track flight status at airports worldwide

* Command: 'open instructables.com'
  * Response:
    Opening Instructables.com - 
    Instructables.com gives you step-by-step guides on how to build anything and everything

* Command: 'open wirecutter.com'
  * Response:
    Opening Wirecutter.com - 
    Wirecutter.com is the best product recommendation website on the Internet

* Command: 'open gohighbrow.com'
  * Response:
    Opening Gohighbrow.com - 
    Gohighbrow.com helps you take bite-sized courses on a variety of topics, with chapters delivered by email every morning

## Opening Installed Softwares in the Computer:
Our JARVIS personal AI assistant has the capability to launch installed software on your computer. However, it requires manual specification of the exact file paths, which should be pasted into the code. It's important to note that the file paths provided in the code serve as placeholders with random extension names. You are responsible for configuring this feature by replacing these placeholders with the actual file paths of the software you intend to open. To comprehend the process, please review the commands provided below. You can expand this feature by installing numerous free and open-source software applications and integrating them with JARVIS. This way, you can proudly showcase a cutting-edge computer setup to your friends, leaving everyone amazed. The more innovative your approach, the more advanced your setup becomes.

* Command: 'open clock'
  * Response: Opening Clock

* Command: 'open calculator'
  * Response: Opening Calculator

* Command: 'open camera'
  * Response: Opening Camera

* Command: 'open notepad'
  * Response: Opening Notepad

* Command: 'open ms office'
  * Response: Opening Microsoft Office

* Command: 'open skype'
  * Response: Opening Skype

* Command: 'open teams'
  * Response: Opening Microsoft Teams

* Command: 'open zoom'
  * Response: Opening Zoom

* Command: 'open chime'
  * Response: Opening Chime

* Command: 'open anydesk'
  * Response: Opening AnyDesk

* Command: 'open maps'
  * Response: Opening Maps

* Command: 'open mail'
  * Response: Opening Mail

* Command: 'open edge'
  * Response: Opening Microsoft Edge

* Command: 'open chrome'
  * Response: Opening Google Chrome

* Command: 'open firefox'
  * Response: Opening Mozilla Firefox

* Command: 'open gallery'
  * Response: Opening Image Viewer

* Command: 'open videos'
  * Response: Opening Video Player

* Command: 'open songs'
  * Response: Opening My Music

* Command: 'open recorder'
  * Response: Opening Voice Recorder

* Command: 'open store'
  * Response: Opening Microsoft Store

* Command: 'open xbox'
  * Response: Opening Xbox

* Command: 'open weather'
  * Response: Opening Weather  

* Command: 'open mcafee'
  * Response: Opening McAfee  

* Command: 'open spotify'
  * Response: Opening Spotify

* Command: 'open steam'
  * Response: Opening Steam  

* Command: 'open dropbox'
  * Response: Opening Dropbox  

* Command: 'open pdf reader'
  * Response: Opening Adobe Acrobat

* Command: 'open word'
  * Response: Opening Microsoft Word

* Command: 'open powerpoint'
  * Response: Opening Microsoft PowerPoint

* Command: 'open excel'
  * Response: Opening Microsoft Excel

* Command: 'open clipchamp'
  * Response: Opening Clipchamp  

* Command: 'open audacity'
  * Response: Opening Audacity  

* Command: 'open bleachbit'
  * Response: Opening BleachBit  

* Command: 'open blender'
  * Response: Opening Blender  

* Command: 'open cpuz'
  * Response: Opening CPU-Z   

* Command: 'open gimp'
  * Response: Opening GIMP Editor

* Command: 'open davinciresolve'
  * Response: Opening DaVinci Resolve  

* Command: 'open vs code'
  * Response: Opening Microsoft Visual Studio Code

* Command: 'open everything'
  * Response: Opening Everything  

* Command: 'open glary'
  * Response: Opening Glary  

* Command: 'open google earth'
  * Response: Opening Google Earth Pro

* Command: 'open greenshot'
  * Response: Opening Greenshot  

* Command: 'open handbrake'
  * Response: Opening HandBrake  

* Command: 'open hw info'
  * Response: Opening HWiNFO  

* Command: 'open seven zip'
  * Response: Opening 7-Zip  

* Command: 'open obs studio'
  * Response: Opening OBS Studio  

* Command: 'open rufus'
  * Response: Opening Rufus  

* Command: 'open virtual box'
  * Response: Opening Oracle VM VirtualBox  

* Command: 'open vmware'
  * Response: Opening VMware  

* Command: 'open cmd'
  * Response: Opening Microsoft Command Prompt

* Command: 'open blue stacks'
  * Response: Opening BlueStacks  

* Command: 'open tor'
  * Response: Opening tor

* Command: 'open veracrypt'
  * Response:  opening veracrypt

* Command: 'open screen copy'
  * Response: Opening screen copy

* Command: 'open vnc'
  * Response: Opening  vnc
 
## Conclusion:

I have exerted my utmost effort to provide a comprehensive output in this project. The primary aim is to empower you with the correct knowledge about the critical logical functions and operations that underlie the development of an AI assistant in the backend. Given that this program spans 500+ lines of code, the possibility of errors emerging is not negligible. Therefore, it's essential to bear in mind that full customization and optimization of the code are essential for successfully deploying and running the program. I wish you the best of luck on your journey into the realm of artificial intelligence!
