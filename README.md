# formi-chatbot-assignment

Barbeque Nation Chatbot Assignment
Description
This project is a conversational AI chatbot for Barbeque Nation. It handles restaurant reservations, answers menu and outlet queries, and provides information about special closures and facilities. The backend is built with Python Flask and serves knowledge base information via an API.

Features
Restaurant Reservations: Handles booking flow (city, outlet, date, meal, pax, confirmation, booking complete).

Menu Queries: Answers questions about veg, non-veg, Jain food, drinks, and desserts.

Outlet Information: Provides address, timings, contact details, and info on special closures.

API Endpoints: Serves knowledge base data for chatbot integration.

Documentation: Includes setup instructions and example API usage.

Project Structure
text
formi-chatbot-assignment/
├── api/                # Flask backend and API code
│   └── app.py
├── knowledge_base/     # JSON files with menu/outlet data
│   └── outlets.json
├── docs/               # Documentation and screenshots
├── src/                # (Optional) Chatbot scripts or other code
└── README.md
Installation
Clone the repository:

text
git clone https://github.com/AAnand11111/formi-chatbot-assignment.git
cd formi-chatbot-assignment
Install dependencies:

text
pip install flask
Run the Flask API:

text
cd api
python app.py
Usage
API Endpoint Example:
To get outlet info, use a POST request:

text
curl -X POST http://127.0.0.1:5000/knowledge -H "Content-Type: application/json" -d "{\"query\": \"unity mall janakpuri\"}"
Example response:

json
{
  "outlet": "Unity Mall Janakpuri",
  "contact": "7827935431",
  "timings": {
    "lunch": "12:00 pm – 5:00 pm",
    "dinner": "6:00 pm – 12:00 am"
  },
  "closures": ["2025-03-14 (Holi lunch closed)"]
}
Chatbot Demo:
[Add your Retell AI agent phone number or web link here, if available]

API Endpoints
POST /knowledge – Query outlet or menu information
Body: { "query": "your question here" }

(Optional) POST /log – Log conversation data

Screenshots
(Add screenshots of your chatbot flow, API responses, or UI here if required. Place image files in the docs/ folder and reference them like this:)

![Chatbot Flow Example](docs/chatbot_flow

Name: Your Name

Email: your.email@example.com

License
This project is for educational purposes only.

How to use this template:

Copy and paste the above into your README.md.

Fill in any missing details (your name, screenshots, agent link, etc.).

Save and push the changes to GitHub.

If you want, paste your current README here and I’ll help you improve it further!

Related
How can I ensure my README file includes all important descriptions
What are the best practices for writing a comprehensive README file
How can I structure my README file for clarity and readability
What sections should be included in a well-written README file
How can I review my README file to ensure it covers all necessary information
