# Python AI Demo
## 项目简介
基于 FastAPI + Ollama 实现Qwen1.5‑7B大模型会话Web服务。
实现多会话上下文记忆，支持创建会话、对话聊天、清空会话，提供HTTP接口，可通过API调用本地大模型推理。

## 技术栈
- Python 3.11.9
- FastAPI：Web接口框架
- Uvicorn：ASGI服务运行器
- Pydantic：请求参数校验
- Ollama：本地大模型推理
- Git + GitHub：版本管理与代码托管

## 项目结构
```
ai_deploy_demo/
├── main.py          # ollama 简单调用测试脚本
├── api_server.py    # FastAPI 会话 Web 服务主程序
├── .gitignore       # Git 忽略文件配置
├── requirements.txt # 项目依赖清单
└── README.md        # 项目文档
```

## 前置准备
本地Ollama环境需要提前拉取Qwen1.5‑7B模型：
```bash
ollama pull modelscope.cn/Qwen/Qwen1.5-7B-Chat-GGUF:latest
```
1. 安装全部依赖
```bash
pip install -r requirements.txt
```
2. 方式1：运行简单测试脚步
```bash
python main.py
```
3. 方式2：启动FastAPI对话服务
```bash
python api_server.py
```
服务器启动后访问接口文档页面：
http://127.0.0.1:8000/docs

## 接口说明

1. `POST /chat` 发起对话，支持自动生成 session_id，保存上下文会话
2. `DELETE /chat/{session_id}` 删除指定会话

## 项目亮点

1. 封装本地大模型为 HTTP 接口，外部可调用 AI 推理能力
2. 实现多用户会话上下文记忆，内存存储对话历史
3. 使用 Pydantic 完成请求参数校验，接口规范
4. 开发环境支持热重载，便于调试开发

## 待优化点

1. 当前会话存储在内存，服务重启会话丢失，生产环境可替换 Redis 持久化会话
2. 关闭 uvicorn reload 参数用于线上部署
