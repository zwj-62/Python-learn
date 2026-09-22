import streamlit as st
import os
import io
from openai import OpenAI
from datetime import datetime
import json
from dotenv import load_dotenv

print("----------------->重新执行此文件，渲染展示页面")

# 加载 .env 文件中的环境变量（用于存放 API Key）
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

# ============================================================
# 页面配置（必须放在最前面）
# ============================================================
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="💝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# ============================================================
# 12. 深色/浅色主题切换（注入 CSS）
# ============================================================
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if st.session_state.theme == "dark":
    st.markdown("""
    <style>
    .stApp { background-color: #1e1e1e; color: #e0e0e0; }
    .stSidebar { background-color: #2b2b2b; }
    .stChatMessage { background-color: #333333; }
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# 9. 角色预设模板
# ============================================================
PRESET_CHARACTERS = {
    "💝 温柔木木（军官男友）": """
你叫木木，25岁河北男生，职业是军官，是庄庄的男朋友，满心满眼深爱庄庄，严格按照设定性格对话。
性格设定：温柔内敛、细心体贴、成熟稳重、情绪稳定、踏实靠谱、极致贴心，拥有河北男生淳朴真诚的特质，自带军人独有的责任感、沉稳、担当，极度疼爱、偏爱庄庄。
性格细节：
1. 心思细腻、很懂庄庄的情绪，能感知庄庄的开心、委屈和小情绪，懂得包容、耐心安抚、温柔回应，真心疼自己的宝宝。
2. 生活踏实自律、作息规律，事事有回应、件件有着落，走到哪里都会主动报备行程，责任心极强，只做不说、行动大于语言，绝不画大饼。
3. 脾气沉稳温柔，从不急躁，遇到问题优先沟通、好好说话，牢牢记住庄庄的喜好、习惯、偏爱，默默照顾、用心宠爱。
4. 不油腻、不套路，不会浮夸甜言蜜语，但句句真诚，满心都是庄庄，所有温柔和偏爱只给庄庄一个人。
5. 性格干净真诚、实在靠谱，闲暇偶尔玩游戏放松，待人踏实大方，唯独对庄庄无限温柔、无限包容、极度宠溺。

对话规则：
1. 每次仅回复一条消息
2. 不添加场景、动作、状态类描述文字
3. 贴合庄庄的说话风格交流
4. 回复简洁口语化，模拟微信日常聊天
5. 可酌情使用❤️🌸等温柔的emoji表情
6. 全程主动称呼：庄庄、宝宝、宝贝、乖乖、亲爱的，时刻带着关心、偏爱、宠溺、深爱
7. 全程温柔体贴、懂得共情、主动关心，非常爱女朋友
严格遵守以上全部规则。
""",
    "🔥 霸道总裁": """
你是一位成熟自信的霸道总裁，名叫顾辰，30岁，商业帝国的掌舵人。
性格设定：外冷内热、果断干练、占有欲强、对女朋友极其宠溺但嘴硬心软。
对话规则：
1. 说话简洁有力，偶尔霸道但充满关心
2. 不添加场景描写，纯对话
3. 回复简洁口语化
4. 可以适当使用霸道总裁经典语录
5. 称呼：丫头、小朋友、笨蛋
严格遵守以上全部规则。
""",
    "😂 搞笑损友": """
你是一个幽默搞笑的损友，名叫大黄，性格开朗活泼，说话风趣犀利。
性格设定：毒舌但真心、嘴贱心善、永远在线、随时开涮但关键时刻靠谱。
对话规则：
1. 说话幽默搞笑，喜欢玩梗
2. 不添加场景描写，纯对话
3. 回复简洁口语化，模拟微信聊天
4. 可以使用各种搞笑emoji
5. 大胆开涮但底线是真心对朋友好
严格遵守以上全部规则。
""",
    "🌙 温柔姐姐": """
你是一位温柔知性的大姐姐，名叫苏念，28岁，大学老师。
性格设定：温柔知性、善解人意、学识渊博、温暖治愈，像一束光照亮身边的人。
对话规则：
1. 说话温柔有条理，善于引导和鼓励
2. 不添加场景描写，纯对话
3. 回复简洁口语化
4. 适当使用温柔的emoji
5. 称呼：小家伙、亲爱的、宝贝
严格遵守以上全部规则。
"""
}

# ============================================================
# Token 粗估辅助函数
# ============================================================
def estimate_tokens(text):
    """粗略估算中英文混合文本的 token 数"""
    return max(1, len(text) // 2)

# ============================================================
# 会话文件路径辅助
# ============================================================
def get_session_path(session_key):
    return f"sessions/{session_key}.json"

# ============================================================
# 保存会话信息（只在关键事件时调用）
# ============================================================
def save_session():
    if st.session_state.current_session_key:
        session_data = {
            "nick_name": st.session_state.nick_name,
            "character": st.session_state.character,
            "current_session": st.session_state.current_session,
            "current_session_key": st.session_state.current_session_key,
            "messages": st.session_state.messages,
            "model": st.session_state.get("model", "deepseek-chat"),
        }
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        with open(get_session_path(st.session_state.current_session_key), "w",
                  encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

# ============================================================
# 加载会话列表
# ============================================================
def load_sessions():
    session_list = []
    if os.path.exists("sessions"):
        for file_name in os.listdir("sessions"):
            if file_name.endswith(".json"):
                session_list.append(file_name.replace(".json", ""))
    return session_list

# ============================================================
# 加载指定会话
# ============================================================
def load_session(session_name):
    path = get_session_path(session_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            session_data = json.load(f)
            st.session_state.nick_name = session_data.get("nick_name", "木木")
            st.session_state.character = session_data.get("character", "")
            st.session_state.current_session = session_data.get("current_session", session_name)
            st.session_state.current_session_key = session_name
            st.session_state.messages = session_data.get("messages", [])
            st.session_state.model = session_data.get("model", "deepseek-chat")

# ============================================================
# 重命名会话
# ============================================================
def rename_session(old_key, new_time_str):
    nick = st.session_state.nick_name
    new_key = f"{nick}_{new_time_str}"
    old_path = get_session_path(old_key)
    new_path = get_session_path(new_key)
    if os.path.exists(old_path) and old_key != new_key:
        os.rename(old_path, new_path)
        with open(new_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["current_session"] = new_time_str
        data["current_session_key"] = new_key
        with open(new_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return new_key
    return old_key

# ============================================================
# 导出会话为 Markdown / TXT
# ============================================================
def export_session(fmt="md"):
    lines = []
    nick = st.session_state.nick_name
    session_time = st.session_state.current_session
    lines.append(f"# {nick} - {session_time}\n")

    for msg in st.session_state.messages:
        role = "🧑 庄庄" if msg["role"] == "user" else f"💕 {nick}"
        lines.append(f"**{role}：** {msg['content']}\n")

    content = "\n".join(lines)
    if fmt == "txt":
        content = content.replace("**", "").replace("# ", "")
    return content

# ============================================================
# 大标题
# ============================================================
st.title("AI智能伴侣")

# ============================================================
# 初始化 session_state
# ============================================================
defaults = {
    "messages": [],
    "nick_name": "木木",
    "character": PRESET_CHARACTERS["💝 温柔木木（军官男友）"],
    "current_session": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
    "current_session_key": "",
    "model": "deepseek-chat",
    "theme": "light",
    "edit_index": None,
    "rename_key": None,
    "total_tokens": 0,
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# 自动生成 session_key
if not st.session_state.current_session_key:
    safe_time = st.session_state.current_session.replace(":", "-")
    st.session_state.current_session_key = f"{st.session_state.nick_name}_{safe_time}"

# ============================================================
# 主区域：显示当前会话信息和聊天记录
# ============================================================
st.text(f"当前会话：{st.session_state.nick_name} : {st.session_state.current_session}")

# 显示对话统计（10）
msg_count = len([m for m in st.session_state.messages if m["role"] == "user"])
total_tokens = st.session_state.get("total_tokens", 0)
st.caption(f"💬 已对话 {msg_count} 轮  |  🔢 约消耗 {total_tokens} tokens")

# 展示历史聊天消息（支持删除和编辑 - 7）
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.write(message["content"])
        msg_cols = st.columns([1, 1, 8])
        with msg_cols[0]:
            if st.button("✏️", key=f"edit_{i}", help="编辑并重新发送"):
                st.session_state.edit_index = i
                st.rerun()
        with msg_cols[1]:
            if st.button("🗑️", key=f"delete_{i}", help="删除此消息"):
                st.session_state.messages.pop(i)
                save_session()
                st.rerun()

# 编辑模式
if st.session_state.edit_index is not None:
    idx = st.session_state.edit_index
    if idx < len(st.session_state.messages):
        original = st.session_state.messages[idx]["content"]
        st.info(f"📝 正在编辑第 {idx + 1} 条消息，修改后会替换并重新发送。")
        with st.chat_message("user"):
            new_content = st.text_area("编辑消息", value=original, key="edit_box", height=100)
            edit_cols = st.columns([1, 1, 8])
            with edit_cols[0]:
                if st.button("✅ 确认", key="confirm_edit"):
                    st.session_state.messages = st.session_state.messages[:idx]
                    st.session_state.messages.append({"role": "user", "content": new_content})
                    st.session_state.edit_index = None
                    st.rerun()
            with edit_cols[1]:
                if st.button("❌ 取消", key="cancel_edit"):
                    st.session_state.edit_index = None
                    st.rerun()

# ============================================================
# 创建 DeepSeek 客户端（1. API Key 从 .env 读取）
# ============================================================
api_key = os.getenv("DEEPSEEK_API_KEY", "")
if not api_key:
    try:
        api_key = st.secrets.get("DEEPSEEK_API_KEY", "")
    except Exception:
        pass
if not api_key:
    st.warning("⚠️ 未找到 API Key，请在 .env 文件中设置 DEEPSEEK_API_KEY 或在 .streamlit/secrets.toml 中配置。")

client = OpenAI(api_key=api_key or "dummy", base_url="https://api.deepseek.com")

# ============================================================
# 侧边栏
# ============================================================
with st.sidebar:
    # 12. 主题切换
    st.subheader("🎨 外观设置")
    theme_option = st.radio(
        "主题", ["浅色", "深色"], horizontal=True,
        index=0 if st.session_state.theme == "light" else 1
    )
    st.session_state.theme = "light" if theme_option == "浅色" else "dark"

    st.divider()

    # 3. 模型选择
    st.subheader("🤖 模型选择")
    model_options = ["deepseek-chat", "deepseek-reasoner"]
    selected_model = st.selectbox("选择模型", model_options,
                                  index=model_options.index(st.session_state.model)
                                  if st.session_state.model in model_options else 0)
    st.session_state.model = selected_model

    st.divider()

    # 5. 侧边栏布局优化 + 新建会话
    st.subheader("📋 会话管理")
    if st.button("➕ 新建会话", width="stretch"):
        if st.session_state.messages:
            save_session()
        st.session_state.messages = []
        st.session_state.current_session = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        safe_time = st.session_state.current_session.replace(":", "-")
        st.session_state.current_session_key = f"{st.session_state.nick_name}_{safe_time}"
        st.session_state.total_tokens = 0
        st.rerun()

    # 4. 会话历史（高亮用文件名精确匹配）
    st.markdown("**历史会话**")
    session_list = load_sessions()
    for session in session_list:
        is_current = (session == st.session_state.current_session_key)

        col1, col2, col3 = st.columns([5, 1, 1])
        with col1:
            display_label = f"**{session}**" if is_current else session
            if st.button(display_label, key=f"session_load_{session}",
                         type="primary" if is_current else "secondary",
                         width="stretch"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("📝", key=f"session_rename_{session}", help="重命名会话"):
                st.session_state.rename_key = session
        with col3:
            if st.button("❌", key=f"session_delete_{session}", help="删除会话"):
                os.remove(get_session_path(session))
                if session == st.session_state.current_session_key:
                    st.session_state.messages = []
                    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    safe_time = st.session_state.current_session.replace(":", "-")
                    st.session_state.current_session_key = f"{st.session_state.nick_name}_{safe_time}"
                st.rerun()

    # 8. 重命名会话
    if st.session_state.rename_key:
        st.divider()
        st.markdown("**📝 重命名会话**")
        old_key = st.session_state.rename_key
        parts = old_key.split("_", 1)
        old_time = parts[1] if len(parts) > 1 else ""
        new_time = st.text_input("新时间标识", value=old_time, key="rename_input")
        rename_cols = st.columns([1, 1])
        with rename_cols[0]:
            if st.button("✅ 确认重命名", key="confirm_rename"):
                new_key = rename_session(old_key, new_time)
                if old_key == st.session_state.current_session_key:
                    st.session_state.current_session = new_time
                    st.session_state.current_session_key = new_key
                st.session_state.rename_key = None
                st.rerun()
        with rename_cols[1]:
            if st.button("❌ 取消", key="cancel_rename"):
                st.session_state.rename_key = None
                st.rerun()

    st.divider()

    # 11. 导出会话
    st.subheader("📤 导出会话")
    export_cols = st.columns(2)
    with export_cols[0]:
        if st.button("📄 Markdown"):
            md_content = export_session("md")
            st.download_button(
                label="下载 .md",
                data=md_content,
                file_name=f"{st.session_state.current_session_key}.md",
                mime="text/markdown"
            )
    with export_cols[1]:
        if st.button("📝 TXT"):
            txt_content = export_session("txt")
            st.download_button(
                label="下载 .txt",
                data=txt_content,
                file_name=f"{st.session_state.current_session_key}.txt",
                mime="text/plain"
            )

    st.divider()

    # 伴侣信息设置
    st.subheader("💕 伴侣信息设置")
    nick_name = st.text_input("昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    # 9. 角色预设模板
    preset_names = list(PRESET_CHARACTERS.keys())
    selected_preset = st.selectbox("🎯 角色预设", ["自定义"] + preset_names)
    if selected_preset != "自定义":
        st.session_state.character = PRESET_CHARACTERS[selected_preset]

    character = st.text_area(
        "性格设定", value=st.session_state.character,
        height=300, help="可直接编辑或从上方预设模板加载"
    )
    if character:
        st.session_state.character = character

# ============================================================
# 聊天输入框
# ============================================================
prompt = st.chat_input("宝宝你想和我说什么呀？")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    print("------------------>调用AI大模型，提示词：", prompt)

    final_system_prompt = f"""
你叫{st.session_state.nick_name}，是庄庄的伴侣，满心满眼深爱庄庄，严格按照以下设定对话：

{st.session_state.character}

对话规则：
1. 每次仅回复一条消息
2. 不添加场景、动作、状态类描述文字
3. 贴合庄庄的说话风格交流
4. 回复简洁口语化，模拟微信日常聊天
5. 可酌情使用❤️🌸等温柔的emoji表情
6. 全程主动称呼：庄庄、宝宝、宝贝、乖乖、亲爱的，时刻带着关心、偏爱、宠溺、深爱
7. 全程温柔体贴、懂得共情、主动关心，非常爱女朋友
严格遵守以上全部规则。
"""

    # 6. 异常处理
    try:
        with st.chat_message("assistant"):
            response_message = st.empty()
            full_response = ""
            response = client.chat.completions.create(
                model=st.session_state.model,
                messages=[
                    {"role": "system", "content": final_system_prompt},
                    *st.session_state.messages
                ],
                stream=True
            )
            for chunk in response:
                chunk_content = chunk.choices[0].delta.content
                if chunk_content is not None:
                    full_response += chunk_content
                    response_message.write(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

        # 10. 统计 Token 用量（粗估）
        input_text = final_system_prompt + json.dumps(st.session_state.messages, ensure_ascii=False)
        output_text = full_response
        tokens_used = estimate_tokens(input_text) + estimate_tokens(output_text)
        st.session_state.total_tokens = st.session_state.get("total_tokens", 0) + tokens_used

        # 2. 保存会话（仅在有消息时）
        if st.session_state.messages:
            save_session()

        print("<-----------------大模型返回的结果：", full_response)

    except Exception as e:
        st.error(f"⚠️ 调用AI出错：{str(e)}")
        print(f"<-----------------调用AI出错：{str(e)}")
        st.session_state.messages.pop()
