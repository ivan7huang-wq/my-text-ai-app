import streamlit as st
import google.generativeai as genai

# 設定網頁標題
st.title("我的 AI 助理 🤖")

# 1. 取得 API Key (從 Streamlit 的秘密金庫拿)
# 這裡要注意，我們不直接把密碼寫在程式裡，是為了安全
api_key = st.secrets["GOOGLE_API_KEY"]

# 2. 設定 Google Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro') # 你也可以改成 gemini-1.5-flash

# 3. 初始化聊天紀錄 (如果還沒開始聊，就建立一個空的清單)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. 顯示過去的對話紀錄
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. 接收使用者的輸入
if prompt := st.chat_input("請輸入你的問題..."):
    # 顯示使用者的話
    with st.chat_message("user"):
        st.markdown(prompt)
    # 存入紀錄
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 6. 呼叫 AI 回答
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
    # 存入紀錄
    st.session_state.messages.append({"role": "assistant", "content": response.text})
