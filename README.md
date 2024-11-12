# NLP-PROJECT
Real-Time Chat Application with NLP-Based Cuss Word Filtering and Abbreviation Expansion 

**Overview**
This is a real-time chat app using Flask and Socket.IO. It features:

**Profanity Filtering:** Masks offensive words using the better_profanity library.
**Abbreviation Expansion:** Expands common abbreviations using a custom dictionary.
**How to Run**
**1. Clone the Repository:**
bash

Copy code

git clone <repository-url>

cd <project-directory>

**2. Install Dependencies:**
Copy code

pip install flask flask-socketio better-profanity

**3.Start the Server:**
Copy code

python app.py

**4. Open in Browser:** Visit http://localhost:5000 to start chatting.

**How to Use**
1. Enter a message in the input field.
2. Press the Send button or hit Enter.
3. The message will be filtered for any offensive words and expanded if it contains abbreviations.
4. The processed message will appear in the chat window in real time.

**Project Structure**
- app.py: Main server file handling Flask and Socket.IO functionalities.
- static/: Contains JavaScript, CSS, and HTML files for the frontend.
- templates/: HTML template files for the chat interface.
- profanity_filter.py: Module for handling cuss word filtering.
- abbreviation_expansion.py: Module for handling abbreviation expansion.
