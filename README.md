ChiPlus
A research project that proposes the development of an integrated platform designed to enhance research management and collaboration efficiency.
by Cypee

Goal: Develop a user-friendly interface for seamless report submission and collation.

For the Frontend I chose to use basic HTML and JavaScript without any additional frameworks while the backend was set up with python (Flask). One of its features is to accept variability in data formats such as JSON, XML and CSV.

Below is a simple web application that collates information from different sources and displays it in a single interface. This project will use Python (Flask) for the backend, and JavaScript for the frontend. The sources in this case is mock APIs for simplicity.

Backend (Python - Flask)
First, set up a simple Flask server that will fetch data from different sources:
1. Install Flask
2. Create app.py

Frontend (HTML + JavaScript)
Create a simple HTML page that will fetch and display the collated data:
1. Create index.html

C Component (Optional)
Alternative need to integrate a C component for some specific processing, by creating a simple shared library and calling it from Python. Simple C function compiled into a shared library:
1. Create collate.c
2. Compile collate.c into a shared library
3. Modify app.py to use the C library

Running the Application:
1. Start the Flask server
2. Open index.html in a web browser

This is a creates an application that collates information from different sources using Python for the backend, and JavaScript for the frontend, with an optional C component for additional processing.
