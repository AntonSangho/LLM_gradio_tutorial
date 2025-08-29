import os 
import gradio as gr
import random

# Ollama는 API키를 필요로하지 않으므로 더미 값 설정
os.environ["OPENAI_API_KEY"] = "not-needed"

demo = gr.load_chat(
    "http://localhost:11434/v1", 
    model="llama3:8b"
)

demo.launch()