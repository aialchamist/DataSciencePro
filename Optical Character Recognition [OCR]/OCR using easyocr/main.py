import easyocr

def extract_text(image_path):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image_path)
  
    detected_text = " ".join([result[1] for result in results])
    return detected_text

if __name__ == "__main__":
    image_path = 'your_image_path.jpg'

    extracted_text = extract_text(image_path)

    print("Extracted Text:")
    print(extracted_text)
