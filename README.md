# ai-math-scribe
This project is a Python-based solution for digitizing handwritten mathematical notes. It leverages the power of the Google Gemini API to accurately read and convert messy, scribbled equations and text from image or PDF files into a clean, digital format.



![Project Header Image](https://via.placeholder.com/800x200?text=Handwritten+Math+OCR)

A Python-based solution for digitizing handwritten mathematical notes using the Google Gemini API. This project converts messy, handwritten equations and text from image or PDF files into a clean, digital format.

---

##Features

- **Multimodal OCR:** Leverages a state-of-the-art AI model to understand both handwritten text and image content.
- **Math Recognition:** Accurately recognizes and converts mathematical expressions into a readable, organized format.
- **Secure API Integration:** Follows best practices by handling API keys securely via environment variables.
- **Flexible Input:** Supports both single image files (`.png`, `.jpg`) and multi-page PDF documents.
- **User-Friendly Output:** Generates a single text file (`extracted_answers.txt`) with the digitized content.

##Getting Started

Follow these steps to set up and run the project on your local machine.

#Prerequisites

- Python 3.8+
- A Google Gemini API Key. You can get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/handwritten-math-ocr.git](https://github.com/your-username/handwritten-math-ocr.git)
    cd handwritten-math-ocr
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # For Windows: venv\Scripts\activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install google-generativeai Pillow PyMuPDF
    ```

## Usage

1.  **Set your API Key:**
    Set your Google Gemini API key as an environment variable in your terminal.
    ```bash
    export GEMINI_API_KEY='YOUR_API_KEY'
    ```

2.  **Place your file:**
    Place your handwritten math file (e.g., `my_notes.png` or `answers.pdf`) in the project directory.

3.  **Update the file name:**
    Open `ocr_project.py` and change the `file_path` variable on line 87 to the name of your file.
    ```python
    file_path = "my_notes.png"
    ```

4.  **Run the script:**
    Execute the Python script from your terminal.
    ```bash
    python ocr_project.py
    ```

The digitized content will be saved to a new file named `extracted_answers.txt`.


#Contributions

Contributions are welcome! If you have suggestions or improvements, please feel free to open an issue or submit a pull request.

