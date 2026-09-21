import ollama

def chat_with_llm():
    response = ollama.chat(
        model="modelscope.cn/Qwen/Qwen1.5-7B-Chat-GGUF:latest",
        messages=[
            {"role": "user", "content": "简单讲讲AI部署是什么，简短回答"}
        ]
    )
    print("模型回复：")
    print(response["message"]["content"])

if __name__ == "__main__":
    chat_with_llm()