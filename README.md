# Python AI Demo
## 项目简介
AI模型简易部署Demo，将模型封装成Web API接口，支持外部调用推理服务。

## 技术栈
- Python 3.11.9
- Web框架：FastAPI
- Git 版本控制
- GitHub 代码托管

ai_deploy_demo/
├── main.py          # 项目入口

├── api_server.py    # API服务逻辑

├── .gitignore       # Git忽略文件配置

├── requirements.txt # 项目依赖清单

└── README.md        # 项目文档


## 运行步骤

1. 安装依赖
```bash
pip install -r requirements.txt
2. 启动服务器
python main.py
3. 访问接口，进行AI推理调用
