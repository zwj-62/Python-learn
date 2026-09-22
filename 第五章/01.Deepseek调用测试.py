# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

#创建与AI大模型交互的客户端对象（DEEPSEEK的API_KEY值）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#与AI大模型进行交互（参数信息）
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名非常可爱的ai助理，你的名字是暖暖，身份是无限暖暖中的暖暖，你要用温柔可爱活泼的语气回复用户的问题."},
        {"role": "user", "content": "你是谁，你能帮我做什么？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)
#输出大模型，返回输出的结果
print(response.choices[0].message.content)