#Fully working OCR model using EasyOCR, with text cleaning and format correction for license plates.
import easyocr
import re

reader = easyocr.Reader(['en'])

def clean_text(text):
    text = text.upper().replace(" ", "")

    # Common OCR fixes
    replacements = {
        '0': 'O',  
        'O': '0',  
        'I': '1',
        'L': '1',
        'B': '8'
    }

    return text


def correct_plate_format(text):
    text = text.upper()
    match = re.findall(r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}', text)
    if match:
        return match[0]

    text = text.replace('O', '0')  
    text = text.replace('I', '1')

    return text


def read_plate(image):
    results = reader.readtext(image)

    data = []
    for (bbox, text, conf) in results:
        x = sum([p[0] for p in bbox]) / 4
        y = sum([p[1] for p in bbox]) / 4
        data.append((text, x, y))

    data.sort(key=lambda x: x[2])

    lines = []
    current = []
    threshold = 30

    for item in data:
        if not current:
            current.append(item)
        elif abs(item[2] - current[0][2]) < threshold:
            current.append(item)
        else:
            lines.append(current)
            current = [item]

    if current:
        lines.append(current)

    final_text = ""
    for line in lines:
        line.sort(key=lambda x: x[1])
        final_text += "".join([w[0] for w in line])

    final_text = clean_text(final_text)
    final_text = correct_plate_format(final_text)

    return final_text

plate = read_plate("upscaled.png")
print("Final Plate:", plate)