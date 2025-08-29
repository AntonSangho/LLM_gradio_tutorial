import os 
import gradio as gr
import random

# Ollama는 API키를 필요로하지 않으므로 더미 값 설정
os.environ["OPENAI_API_KEY"] = "not-needed"

def random_response(message, history):
    return random.choice(["Yes", "No"])

demo = gr.ChatInterface(
    fn=random_response,
    title = "예 아니오 응답 테스트",
    description= "무엇을 물어보든 예 아니오로 답한다."
).launch()

demo.launch()