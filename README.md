
# hw02 作业说明

## 任务一：论文导读
- **论文来源**：《A survey on large language model based autonomous agents》（LLM自主智能体领域综述类论文）
- **导读生成方式**：使用 deepseek 大模型，按「引言 研究背景 → 核心方法 → 结果 → 小结」结构生成，后经人工润色调整
- **配图方式**：从论文原文中提取模型架构图、系统对比表、应用场景示意图，手动插入到导读对应章节并添加图注
- **文档**：`导读-A survey on large language model based autonomous agents.pdf`

## 任务二：Chatbot 示例代码
### 采用 API/平台
- 平台：DeepSeek 官方 OpenAI 兼容接口
- 接口地址：`https://api.deepseek.com`
- 模型：`deepseek-chat`

### 运行环境
- Python 3.8+
- 依赖：见 `requirements.txt`

### 依赖安装
```bash
pip install -r requirements.txt
set DEEPSEEK_API_KEY=DeepSeek API Key
python chatbot_deepseek.py
你：请介绍一下大语言模型自主智能体
DeepSeek：大语言模型自主智能体（LLM-based autonomous agents）是以大语言模型为核心，具备自主感知、规划、决策和行动能力的智能系统，能够独立完成复杂任务并适应动态环境...