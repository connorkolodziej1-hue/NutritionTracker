from ollama import chat
import shutil
import os
import json
import time

def extractFacts(filepath):

    with open(filepath, "r") as f:
        content = f.read()

    print("Starting Ollama...")

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": (
                        "Extract the nutrition facts in the following format"
                        "{"
                        "   calories: {put listed calories here}"
                        "   servings: {put number of servings per container. assume 1 if none is listed}"
                        "   total_fat: {put listed daily value percentage for total fat here}"
                        "   saturated_fat: {put listed daily value percentage for saturated fat here}"
                        "   trans_fat: {put listed daily value percentage for total fat here. assume 0 if none is listed}"
                        "   cholesterol: {put listed daily value percentage for cholesterol here}"
                        "   sodium: {put listed daily value percentage for sodium here}"
                        "   total_carbohydrate: {put listed daily value percentage for total carbohydrate here}"
                        "   dietary_fiber: {put listed daily value percentage for dietary fiber here}"
                        "   total_sugars: {put listed daily value percentage for total sugars here}"
                        "   protein: {put listed daily value percentage for protein here}"
                        "   vitamin_d: {put listed daily value percentage for vitamin D here}"
                        "   iron: {put listed daily value percentage for iron here}"
                        "   calcium: {put listed daily value percentage for calcium here}"
                        "   potassium: {put listed daily value percentage for total fat here}"
                        "}"
                        " from the following text. "
                        "Return ONLY valid JSON.\n\n"
                        + content
                )
            }
        ],
        stream=True
    )

    print("Ollama is responding:")

    full_response = ""

    for chunk in response:
        text = chunk["message"]["content"]
        print(text, end="", flush=True)
        full_response += text

    print("\n\nOllama finished.")

    send_json_payload(full_response)

    shutil.move(filepath, "./readText/")
    
def send_json_payload(payloadString):
    print("sending payload")
    payload = json.loads(payloadString)

    with open("./readFacts/facts.json", "w") as f:
        json.dump(payload, f, indent=4)
    
    print("payload sent")


while True:
    files = os.listdir("./extractedText/")
    
    if files:
        print("reading file")
        extractFacts("./extractedText/" + files[0])
        print("file read")
        

    time.sleep(1)
    
    

