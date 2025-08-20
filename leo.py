import os
import socket
import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
from scapy.all import sniff
import threading

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set male voice
voices = tts_engine.getProperty('voices')
for voice in voices:
    if 'male' in voice.name.lower():
        tts_engine.setProperty('voice', voice.id)
        break

# Function to speak
def speak(text):
    print(text)
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio, language='en-In')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

# Function for keyboard input
def get_input():
    return input("Type your query: ").lower()

# Function to display ASCII Art
def asciiart():
    print("""
 ⠀        ⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀  
⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀   
⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       ###          ##########   ##########
⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       ###          ##########   ##########
⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       ###          ###          ###    ###
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀       ###          #######      ###    ###
⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀       ###          #######      ###    ###
⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀       ###          ###          ###    ###
⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀       ##########   ##########   ##########
⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ##########   ##########   ##########
    """)

# Function to greet based on time
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, Comrade!")
    elif 12 <= hour < 18:
        speak("Good afternoon, Comrade!")
    else:
        speak("Good evening, Comrade!")
    speak("I am LEO, your cyber virtual assistant. How can I help you today?")

# Function to tell time
def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    speak(f"The current time is {time_str}")

# Function to tell date
def tell_date():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    speak(f"Today's date is {date_str}")

# Function to search the web
def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Here are the search results for {query}")

# Function to check IP information
def check_ip_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    speak(f"Your local IP address is {ip_address}")

# Function to scan ports
def scan_ports(ip_address):
    open_ports = []
    threads = []
    for port in range(1, 1025):
        thread = threading.Thread(target=scan_ports, args=(ip_address, port, open_ports))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    if open_ports:
        ports = ', '.join(map(str, open_ports))
        speak(f"Open ports on {ip_address}: {ports}")
    else:
        speak(f"No open ports found on {ip_address}")

# Function to check vulnerabilities (placeholder)
def check_vulnerabilities():
    os.system("sudo nmap -sV --script vuln localhost")
    speak("Vulnerability scan completed. Check the console output for details.")

# Function to display system information
def display_system_info():
    os.system("systeminfo")
    speak("System information displayed. Check the console output for details.")

# Function to tell about LEO
def tell_about_self():
    speak("""Naan da Leo, Logical Enforcement Oracle.
          A cyber virtual assistant created by O G Studio. 
          My purpose is to assist you with various tasks. 
          How can I assist you today? """)

# Intrusion Detection Function
def detect_intrusions(packet):
    print("Packet Captured:", packet.summary())
   

# Function to start NIDS
def start_nids():
    speak("Network Intrusion Detection System started. Monitoring network traffic...")

     # Find your correct network interface (use netsh command)
    interface = "Wi-Fi"  # Change based on your system

    # Start sniffing packets
    sniff(prn=detect_intrusions, store=False, iface=interface, filter="ip")

# Main function
def main():
    asciiart()
    greet()
    while True:
        query = listen()
        if query is None:
            print("No valid voice input detected. Please type your query.")
            query = get_input()

        if query:
            if "time" in query:
                tell_time()
            elif "date" in query:
                tell_date()
            elif "search for" in query:
                search_term = query.replace("search for", "").strip()
                search_web(search_term)
            elif "check ip" in query:
                check_ip_info()
            elif "scan ports" in query:
                ip_address = input("Enter IP address to scan: ")
                scan_ports(ip_address)
            elif "check vulnerabilities" in query:
                check_vulnerabilities()
            elif "system info" in query:
                display_system_info()
            elif "tell me something about yourself" in query or "who are you" in query:
                tell_about_self()
            elif "start nids" in query:
                start_nids()
            elif "stop" in query or "exit" in query or "end" in query:
                speak("Red Salute!")
                break
            else:
                speak("I did not understand your request. Please try again.")

if __name__ == "__main__":
    main()
