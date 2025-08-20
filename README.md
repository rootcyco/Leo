# LEO - Logical Enforcement Oracle

LEO is a cyber virtual assistant designed to assist users with various cyber-related tasks, including network scanning, system information retrieval, and web searching. This Python-based assistant supports both voice and text input and features basic network security functionalities.

## Features
- **Voice Recognition & Text Input**: Interact with LEO using voice commands or by typing queries.
- **Text-to-Speech (TTS)**: LEO responds with a male voice.
- **Time & Date Functions**: Retrieves and announces the current time and date.
- **Web Search**: Opens Google search results for a given query.
- **IP Information Retrieval**: Displays the local IP address.
- **Port Scanning**: Scans a target IP for open ports.
- **Vulnerability Scan**: Runs an Nmap vulnerability scan.
- **System Information Retrieval**: Displays system details.
- **Intrusion Detection System (NIDS)**: Detects common network attacks (SYN flood, port scanning, etc.).
- **ASCII Art & Greetings**: Welcomes the user with ASCII art and a personalized greeting.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  ```sh
  pip install speechrecognition pyttsx3 pyaudio
  ```
- **For network functionalities:** Install Nmap and Scapy:
  ```sh
  sudo apt install nmap
  pip install scapy
  ```

## Usage
1. **Run the script**:
   ```sh
   python leo.py
   ```
2. LEO will start with a greeting and listen for voice commands.
3. If voice input is unclear, you can type your queries manually.
4. Example commands:
   - "What is the time?"
   - "Search for cybersecurity news"
   - "Check IP"
   - "Scan ports" (requires user to input an IP address)
   - "Check vulnerabilities"
   - "System info"
   - "Start NIDS"
   
## Customization
- To modify the assistant's voice, adjust the `tts_engine.setProperty('voice', voice.id)` settings in the script.
- The ASCII art in the `asciiart()` function can be replaced with custom designs.

## Security Notice
- Running the intrusion detection system (IDS) may require administrative privileges.
- Port scanning and vulnerability scanning should only be performed on systems you own or have permission to scan.

## License
This project is developed by O G Studio and is intended for ethical use. Unauthorized or malicious usage is strictly prohibited.

## Acknowledgments
Inspired by cyber security tools and AI-based voice assistants.

---
Feel free to contribute and enhance LEO with additional features!

