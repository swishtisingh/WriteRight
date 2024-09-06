<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README.md</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        code {
            background: #f4f4f4;
            border: 1px solid #ddd;
            padding: 5px;
        }
        pre {
            background: #f4f4f4;
            border: 1px solid #ddd;
            padding: 10px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Chrome Extension for Grammar Improvement Using Hugging Face API</h1>

    <p>This repository contains the files for a Google Chrome extension that uses the Hugging Face API to provide grammatically improved versions of input text. The backend is powered by a Flask server.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#file-structure">File Structure</a></li>
        <li><a href="#technologies-used">Technologies Used</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
    </ul>

    <h2 id="overview">Overview</h2>
    <p>This Chrome extension allows users to input text and receive a grammatically improved version using the Hugging Face API. The extension communicates with a Flask server that processes the input and returns the corrected text.</p>

    <h2 id="features">Features</h2>
    <ul>
        <li>Input text through the Chrome extension.</li>
        <li>Receive grammatically corrected text using the Hugging Face API.</li>
        <li>User-friendly interface with a simple form and result display.</li>
        <li>Flask server backend to handle API requests.</li>
    </ul>

    <h2 id="installation">Installation</h2>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>pip (Python package installer)</li>
        <li>Node.js and npm (for Chrome extension development)</li>
    </ul>

    <h3>Setup</h3>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name</code></pre>
        </li>
        <li><strong>Set up the Flask server:</strong>
            <ul>
                <li>Create a virtual environment:
                    <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
                </li>
                <li>Install dependencies:
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
                <li>Create a <code>requirements.txt</code> file with the following content if it doesn't exist:
                    <pre><code>Flask==2.0.3
requests==2.27.1
Flask-CORS==3.0.10</code></pre>
                </li>
                <li>Run the Flask server:
                    <pre><code>python app.py</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Set up the Chrome extension:</strong>
            <ul>
                <li>Open Chrome and go to <code>chrome://extensions/</code>.</li>
                <li>Enable "Developer mode" in the top right corner.</li>
                <li>Click on "Load unpacked" and select the directory containing your extension files (the cloned repository).</li>
            </ul>
        </li>
    </ol>

    <h2 id="usage">Usage</h2>
    <ol>
        <li><strong>Start the Flask server:</strong>
            <pre><code>python app.py</code></pre>
        </li>
        <li><strong>Use the Chrome extension:</strong>
            <ul>
                <li>Click on the extension icon in the Chrome toolbar.</li>
                <li>Enter the text you want to improve.</li>
                <li>Click "Submit Text" to send the request.</li>
                <li>The improved version of the text will be displayed in the result area.</li>
            </ul>
        </li>
    </ol>

    <h2 id="file-structure">File Structure</h2>
    <pre><code>.
├── app.py                # Flask server application
├── popup.html            # Chrome extension popup HTML file
├── popup.css             # Chrome extension CSS file
├── popup.js              # Chrome extension JavaScript file
├── requirements.txt      # Python dependencies
└── README.md             # This README file</code></pre>

    <h2 id="technologies-used">Technologies Used</h2>
    <ul>
        <li><strong>Flask</strong>: Python web framework for the server.</li>
        <li><strong>Requests</strong>: Python library for making HTTP requests.</li>
        <li><strong>Flask-CORS</strong>: Extension for handling Cross-Origin Resource Sharing (CORS).</li>
        <li><strong>Hugging Face API</strong>: API for grammar correction.</li>
        <li><strong>HTML, CSS, JavaScript</strong>: Frontend technologies for the Chrome extension.</li>
    </ul>

    <h2 id="contributing">Contributing</h2>
    <p>Contributions are welcome! Please follow these steps to contribute:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
        <li>Make your changes and commit them (<code>git commit -m 'Add new feature'</code>).</li>
        <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
        <li>Open a Pull Request.</li>
    </ol>

    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
