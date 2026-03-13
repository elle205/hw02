import os
from openai import OpenAI

# 配置DeepSeek API Key（这里先留空，运行时用环境变量传入，避免泄露）
# 你也可以临时直接替换：api_key = "你的DeepSeek API Key"（测试用，提交前要删掉）
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("❌ 未找到DeepSeek API Key！请先设置环境变量 DEEPSEEK_API_KEY")

# 初始化DeepSeek客户端（OpenAI兼容接口）
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"  # DeepSeek官方接口地址
)

def chat_with_deepseek(user_input):
    """
    调用DeepSeek API生成回复
    :param user_input: 用户输入的问题
    :return: DeepSeek的回复内容
    """
    try:
        # 调用Chat Completions接口
        response = client.chat.completions.create(
            model="deepseek-chat",  # 指定DeepSeek对话模型
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7,  # 回复随机性（0-1，越小越固定）
        )
        # 提取回复内容
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 调用API失败：{str(e)}"

# 主交互逻辑
if __name__ == "__main__":
    print("🎉 DeepSeek Chatbot 已启动！输入 'quit' 退出对话")
    while True:
        # 获取用户输入
        user_input = input("\n你：")
        # 退出条件
        if user_input.lower() == "quit":
            print("👋 对话结束，再见！")
            break
        # 调用接口获取回复
        reply = chat_with_deepseek(user_input)
        # 打印回复
        print(f"\nDeepSeek：{reply}")