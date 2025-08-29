# **Flask Interactive File and Image App**

This is a simple web application built with Flask that provides a clean, modern user interface for two main functions:

1. Displaying an image of a selected animal (Cat, Dog, or Elephant).  
2. Uploading a file and displaying its metadata (name, type, and size).

The project is designed to be lightweight and uses modern frontend techniques to communicate with the Flask backend asynchronously, providing a smooth user experience. It is managed entirely with uv for a fast and efficient development workflow.

## **Features**

* **Interactive UI**: A responsive and user-friendly interface with two distinct functional boxes.  
* **Dynamic Image Display**: Select an animal via radio buttons to instantly fetch and display its image from the server.  
* **File Metadata Analysis**: Upload any file to get immediate feedback on its name, MIME type, and size.  
* **Asynchronous Communication**: Uses the fetch API in JavaScript to interact with the backend without page reloads.  
* **Modern Tech Stack**: Built with Python, Flask, and vanilla HTML/CSS/JavaScript.  
* **Blazing Fast Workflow**: Uses uv for environment creation, dependency management, and running scripts.

## **Project Structure**

The project follows a standard Flask application structure to keep code organized and maintainable.

flask\_file\_app/  
├── .venv/                   \# Virtual environment directory  
├── static/                  \# Contains static assets  
│   ├── images/              \# Stores animal images  
│   │   ├── cat.jpg  
│   │   ├── dog.jpg  
│   │   └── elephant.jpg  
│   └── styles.css           \# CSS for styling the frontend  
├── templates/               \# Contains HTML templates  
│   └── index.html           \# The main page of the application  
├── main.py                  \# The core Flask application logic  
├── pyproject.toml           \# Project configuration and dependencies  
└── README.md                \# You are here\!

## **Setup and Installation**

This guide walks through setting up the project from scratch using Python 3.10 and uv.

### **Prerequisites**

* **Python 3.10**: You must have Python 3.10 installed on your system to create the virtual environment.

### **Step-by-Step Guide**

1. Create the Virtual Environment  
   First, create a virtual environment specifically with Python 3.10.  
   `py -3.10 -m venv .venv`

2. Activate the Environment  
   Activate the newly created environment.  
   * **On macOS/Linux:**  
     `source .venv/bin/activate`

   * **On Windows (PowerShell/CMD):**  
     `.venv\\Scripts\\activate`

3. Install uv  
   Inside the active environment, install uv using pip.  
   `pip install uv`

4. Initialize the Project with uv  
   Run uv init to create a pyproject.toml file for your project.  
  ` uv init`

5. Add Dependencies to pyproject.toml  
   Open the newly created pyproject.toml file and add flask to the \[project.dependencies\] array. It should look like this:  
     ``` 
   \[project\]  
   name \= "flask\_file\_app"  
   version \= "0.1.0"  
   description \= "Add your description here."  
   dependencies \= \[  
       "flask",  
   \]  
   \# ... rest of the file
   ```
6. Install Dependencies with uv sync  
   Now, tell uv to install the dependencies listed in your pyproject.toml file. The sync command is extremely fast.  
   `uv sync`

7. Add Animal Images  
   Ensure you have placed cat.jpg, dog.jpg, and elephant.jpg inside the static/images/ directory.

## **How to Run the Application**

With your environment set up and dependencies synced, use uv run to execute the Flask application script.

`uv run python main.py`

The terminal will show output indicating that the server is running, usually on http://122.161.54.45:5000.


## **How to Use the App**

* **To see an animal**: Simply click on the radio button corresponding to "Cat", "Dog", or "Elephant". The image will appear in the result box below.  
* **To get file details**: Click the "Choose File" button, select any file from your computer, and then click "Get Details". The file's metadata will be displayed in the result box.

## **Technologies Used**

* **Backend**: Python, Flask  
* **Frontend**: HTML, CSS, JavaScript (vanilla)  
* **Package Management**: uv

## AWS Integration 
 - To Be Done
