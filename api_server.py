from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
import uuid

# 实例化FastAPI应用
app = FastAPI(title="Qwen1.5-7B 大模型部署服务", version="1.0")

# 内存存储会话：key=session_id，value=对话历史messages
# ⚠️ 重启服务后所有会话会清空；生产环境换成Redis
session_store = {}


# 请求体结构
class ChatRequest(BaseModel):
    prompt: str
    session_id: str | None = None  # 会话ID，第一次请求不传会自动生成


# 对话接口
@app.post("/chat")
async def chat(req: ChatRequest):
    model_name = "modelscope.cn/Qwen/Qwen1.5-7B-Chat-GGUF:latest"

    # 第一次对话，没有session_id → 创建新会话
    if not req.session_id:
        new_session_id = str(uuid.uuid4())
        session_store[new_session_id] = []
        req.session_id = new_session_id

    # 检查会话是否存在
    if req.session_id not in session_store:
        raise HTTPException(status_code=404, detail="会话不存在，请重新发起对话")

    # 取出当前会话历史
    messages = session_store[req.session_id]
    # 添加用户最新提问
    messages.append({"role": "user", "content": req.prompt})

    # 调用ollama推理
    response = ollama.chat(
        model=model_name,
        messages=messages
    )
    reply = response["message"]["content"]

    # 把模型回答存入会话历史，用于下一轮上下文
    messages.append({"role": "assistant", "content": reply})
    session_store[req.session_id] = messages

    return {
        "session_id": req.session_id,
        "reply": reply
    }


# 清空指定会话
@app.delete("/chat/{session_id}")
async def clear_chat(session_id: str):
    if session_id in session_store:
        del session_store[session_id]
        return {"msg": "会话已清空"}
    raise HTTPException(status_code=404, detail="会话不存在")


if __name__ == "__main__":
    import uvicorn

    # 启动服务，reload=True：代码修改自动重启（开发用，上线关掉）
    uvicorn.run("api_server:app", host="127.0.0.1", port=8000, reload=True)