import os
from flask import Flask, request, jsonify, render_template, url_for

# Initialize the Flask application
app = Flask(__name__)

# Configuration
# It's good practice to have an upload folder, though we won't be saving files in this example.
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_request():
    """
    Handles both animal selection and file uploads from the frontend.
    """
    # --- Animal Selection Logic ---
    if 'animal' in request.form:
        animal = request.form['animal']
        image_url = ''
        if animal in ['cat', 'dog', 'elephant']:
            # Generate the URL for the static image file
            image_url = url_for('static', filename=f'images/{animal}.jpg')
        return jsonify({'imageUrl': image_url})

    # --- File Upload Logic ---
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # We read the file to get its size, but we don't save it to the server.
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0) # Reset pointer

        # Prepare file details for the response
        file_details = {
            'name': file.filename,
            'type': file.mimetype,
            'size_bytes': file_size,
            'size_human': f"{file_size / 1024:.2f} KB"
        }
        return jsonify({'fileDetails': file_details})

    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    # Runs the app in debug mode, which is helpful for development.
    app.run(debug=True)