import streamlit as st

#设置页面的配置项
st.set_page_config(
    page_title="streamlit的入门",
    page_icon="🧊",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.itcast.cn',
        'Report a bug': "https://www.itcast.cn",
        'About': "#这是一个streamlit的入门页面"
    }
)

#大标题
st.title("Steanmlit的入门演示：")
st.header("Streamlit的一级标题：")
st.subheader("Streamlit的二级标题")
#段落文字
st.write("暖暖，全名苏暖暖，是叠纸科技旗下暖暖系列游戏的女主角，也是《无限暖暖》中玩家将扮演的核心角色。")
st.write("她是一位19岁的粉发少女，身高160cm，生日是12月6日，性格善良、天真可爱又坚强乐观，天生具备出色的搭配天赋。")
st.write("在《无限暖暖》中，暖暖与她的好伙伴——一只圆嘟嘟又健谈的猫咪“大喵”一起，被传送到名为“奇迹大陆”的奇幻世界。在这里，服装蕴含名为“奇想力”的神奇力量，而暖暖作为被命运选中的搭配师，需要寻找传说中的“奇迹套装”，为这片大陆带去希望的曙光。")
st.write("她热爱换装与收集可爱物品，烦恼和许多女孩一样——衣橱里永远少一件最好看的衣服。在冒险途中，她可以使用不同能力的套装，如漂浮、净化、捕虫、钓鱼等，解决各种难题，体验温馨治愈的开放世界之旅。")

#引入图片
st.image("./resources/暖暖图片.jpg")
#引入音频
st.audio("./resources/暖暖自我介绍.mp3")
#引入视频
st.video("./resources/小红帽视频.mp4")
#引入logo
st.logo("./resources/暖暖logo.png")
#引入一个表格
import streamlit as st

# 以“暖暖”为主题的学生数据
student_data = {
    "角色名": ["暖暖", "妮妮", "大喵", "啵啵", "苏暖"],
    "编号": ["W2026001", "W2026002", "W2026003", "W2026004", "W2026005"],
    "搭配力": [98, 97, 92, 90, 89],
    "设计分": [100, 98, 32, 90, 96],
    "表现力": [100, 90, 98, 92, 82]
}

st.table(student_data)

#输入框
name=st.text_input("请输入搭配师的ID:")
st.write(f"搭配师的ID是：{name}")

password=st.text_input("请输入搭配师的密码:",type="password")
st.write(f"搭配师的密码是：{password}")

#单选按钮组件
gender=st.radio("请输入您的性别：",["男","女","未知"])
st.write(f"您的性别为：{gender}")