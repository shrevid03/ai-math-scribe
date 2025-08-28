import os
import io
import fitz 
from PIL import Image 
import google.generativeai as genai

# have connfigure the Gemini API Key 
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

#  Functions- File and Image Processing

def convert_pdf_to_images(pdf_path: str) -> list[Image.Image]:
    """
    Converts a PDF file into a list of Pillow Image objects, one for each page.
    This is necessary because the Gemini API processes images, not PDFs.

    Args:
        pdf_path: The path to the input PDF file.

    Returns:
        A list of Pillow Image objects.
    """
    print(f"Converting PDF at '{pdf_path}' to images...")
    try:
        pdf_document = fitz.open(pdf_path)
        images = []
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            # Creates image from the page
            pix = page.get_pixmap(dpi=300) 
            img_bytes = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_bytes))
            images.append(image)
        print(f"converted {len(images)} page(s) to images.")
        return images
    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred during PDF conversion: {e}")
        return []

def load_image(image_path: str) -> Image.Image:
    """
    Loads a single image file into a Pillow Image object.

    Args:
        image_path: The path to the image file.

    Returns:
        A Pillow Image object, or None if the file is not found.
    """
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print(f"Error: The image file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the image: {e}")
        return None

# Function for the API Call

def get_handwritten_math_text(image: Image.Image) -> str:
    """
    Sends an image with handwritten math to the Gemini API for recognition.
    The prompt specifically asks for mathematical expressions to be
    converted into a readable format.

    Args:
        image: A Pillow Image object to be processed.

    Returns:
        A string containing the extracted, formatted text.
    """
    
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    
    prompt_text = (
        "You are an expert handwritten text recognition assistant. "
        "Your task is to convert the handwritten content from the image into editable text. "
        "The content contains mathematical solutions. "
        "Do not use LaTeX or any other formatting. "
        "Return the full text with all content clearly transcribed and organized."
    )

    try:
        response = model.generate_content([prompt_text, image])
        # Check if a valid text response was received.
        if response.text:
            return response.text
        else:
            return "Could not get a valid text response from the model. Check for safety blocks or model issues."
    except genai.types.BlockedPromptException as e:
        return f"The prompt was blocked by the safety filter. Details: {e}"
    except Exception as e:
        return f"An error occurred during the API call: {e}"

# Main Execution Block

if __name__ == "__main__":
    file_path = "IMG_3457.JPG"

    extracted_content = ""

    if file_path.lower().endswith(".pdf"):
        # Process a multi-page PDF
        images_to_process = convert_pdf_to_images(file_path)
        if images_to_process:
            for i, page_image in enumerate(images_to_process):
                print(f"\nProcessing page {i + 1} of the PDF ")
                text_output = get_handwritten_math_text(page_image)
                print(text_output)
                extracted_content += f"\n\n--- Page {i + 1} ---\n{text_output}"
        else:
            print("No images to process. Please check your PDF file.")
            
    else:
        # Process a single image file
        image_to_process = load_image(file_path)
        if image_to_process:
            print(f"\n Processing a single image file ")
            text_output = get_handwritten_math_text(image_to_process)
            print(text_output)
            extracted_content = text_output
        else:
            print("No image to process. Please check your image file.")
            
   
    if extracted_content:
        with open("extracted_answers.txt", "w", encoding="utf-8") as f:
            f.write(extracted_content)
        print("\nAll extracted content has been saved to 'extracted_answers.txt'.")
