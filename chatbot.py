import requests

API_KEY = "0000000000"
API_URL = "https://api.openai.com/v1/engines/davinci-codex/completions"

def chatgpt_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "prompt": prompt,
        "max_tokens": 50,
        "temperature": 0.7,
        "n": 1,
        "stop": ["\n"]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()
    response_text = response_json['choices'][0]['text'].strip()

    return response_text

def chatbot():
    print("간단한 ChatGPT 챗봇입니다. 대화를 시작해주세요. 종료하려면 'quit'을 입력하세요.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        
        prompt = f"사용자: {user_input}\n챗봇: "
        chatgpt_output = chatgpt_response(prompt)
        print(f"챗봇: {chatgpt_output}")

if __name__ == "__main__":
    chatbot()
  
