# Flask Interactive File and Image App

This is a simple web application built with Flask that provides a clean, modern user interface for two main functions:
1.  Displaying an image of a selected animal (Cat, Dog, or Elephant).
2.  Uploading a file and displaying its metadata (name, type, and size).

The project is designed to be lightweight and uses modern frontend techniques to communicate with the Flask backend asynchronously, meaning the page doesn't need to reload to show results.

---

## Features

* **Interactive UI**: A responsive and user-friendly interface with two distinct functional boxes.
* **Dynamic Image Display**: Select an animal via radio buttons to instantly fetch and display its image from the server.
* **File Metadata Analysis**: Upload any file to get immediate feedback on its name, MIME type, and size in a human-readable format.
* **Asynchronous Communication**: Uses the `fetch` API in JavaScript to interact with the backend without page reloads, providing a smooth user experience.
* **Modern Tech Stack**: Built with Python, Flask, and vanilla HTML/CSS/JavaScript.
* **Fast Dependency Management**: Uses `uv` for incredibly fast package installation and management.

---

## Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

* **Python 3.8+**: Make sure you have a modern version of Python installed.
* **uv**: This project uses `uv` for package management. If you don't have it, install it with:
    ```bash
    pip install uv
    ```

### Step-by-Step Guide

1.  **Clone the Repository**
    Clone or download this project to your local machine.

2.  **Navigate to the Project Directory**
    Open your terminal and change into the project's root folder.
    ```bash
    cd path/to/your-project-folder
    ```

3.  **Create and Activate a Virtual Environment**
    This project is set up to use a `.venv` folder. Use `uv` to create it.
    ```bash
    uv venv
    ```
    Activate the environment:
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    * **On Windows (PowerShell/CMD):**
        ```bash
        .venv\Scripts\activate
        ```

4.  **Install Dependencies**
    Use `uv` to install the required packages from `pyproject.toml`. It's blazing fast!
    ```bash
    uv pip install -e .
    ```
    *(The `-e .` installs the project in "editable" mode, which is good practice for development).*

5.  **Add Animal Images**
    Make sure you have placed `cat.jpg`, `dog.jpg`, and `elephant.jpg` inside the `static/images/` directory.

---

## How to Run the Application

With your virtual environment activated and dependencies installed, run the main Python script:

```bash
python main.py