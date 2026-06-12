Cocktail Recommendation System:

 Description:
This is a client-server desktop application built in Python that recommends cocktails based on user preferences. The system uses socket programming for communication between client and server, SQLite for database storage, and Tkinter for the graphical user interface.

 Features:
Client-server communication using TCP sockets
Cocktail filtering based on ingredients, strength, and taste
SQLite database for storing cocktail data
Multithreading for handling server operations and live updates
JSON format for structured data exchange
Tkinter GUI for user interaction
Logging requests into a file

 Technologies Used:
Python
Tkinter
SQLite3
Socket Programming (TCP/IP)
JSON
Threading
File handling

 How to Run:
1. Start the server
python server.py
2. Start the client
python client.py

 Project Structure:
project/
│
├── server.py
├── client.py
├── bazakoktela.db
├── ispis.txt
└── README.md

 Notes
Server must be running before starting the client
Communication is done via localhost (socket connection)
Results are returned in JSON format
