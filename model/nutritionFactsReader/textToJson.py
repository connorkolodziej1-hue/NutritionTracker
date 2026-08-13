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
                        "Extract the nutrition facts from the following text. "
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
    
    

