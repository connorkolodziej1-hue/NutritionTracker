from fileinput import filename

from doctr.io import DocumentFile
from doctr.models import kie_predictor

import img2pdf
import os

def extract_text(model, filepath):
    if not filepath.endswith('.pdf'):
        filepath = convert_to_pdf(filepath)

    doc = DocumentFile.from_pdf(filepath)
    result = model(doc)

    
    predictions = result.pages[0].predictions
    # for class_name in predictions.keys():
    #     list_predictions = predictions[class_name]
    #     for prediction in list_predictions:
    #         print(f"Prediction for {class_name}: {prediction}")
            
    predictions_to_textString(predictions, filepath)
    

def convert_to_pdf(filepath):
    try:
        pdf_bytes = img2pdf.convert(filepath)
        
        new_path = os.path.splitext(file_path)[0] + ".pdf"


        with open(new_path, "wb") as f:
            f.write(pdf_bytes)
        
        os.remove(filepath)
        return new_path
            
    except Exception as e:
        print(f" Error creating PDF: {e}")


def predictions_to_textString(predictions, filepath):
    text = ""
    for class_name in predictions.keys():
        list_predictions = predictions[class_name]
        for prediction in list_predictions:
            text += prediction.value + " "
    print(text)
    
    send_text_payload(text, filepath)

def send_text_payload(text, inputFileName):
    print("sending payload")
    output_path = os.path.splitext(file_path)[0].replace("input", "extractedText") + ".txt"

    with open(output_path, "w") as f:
        f.write(text)
    
    print("payload sent")

model = kie_predictor(det_arch="db_resnet50", reco_arch="crnn_vgg16_bn", pretrained=True)

directory = "./input/"
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path): # Check if it's a file
        print(f"Processing file: {file_path}")
        extract_text(model, file_path)
