import streamlit as st
import base64
import json
import os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

# Streamlitアプリのタイトルとサイドバーの設定
st.set_page_config(page_title="Image Analysis with Claude 3", layout="wide")
st.title("Upload Image")

def upload_image():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        return uploaded_file
    return None

# Base64エンコードのための関数
def get_base64_encoded_image(image_file):
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def analyze_image(image_file, prompt):
    api_key = os.environ.get("CLAUDE_API_KEY")
    chat = ChatAnthropic(api_key=api_key, temperature=0.5, model_name="claude-3-5-sonnet-20240620")
    system = "You are an AI assistant that analyzes images based on the given prompt."
    human = "{text}"
    prompt_template = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    chain = prompt_template | chat
    result = chain.invoke(input={"text": json.dumps({"image": get_base64_encoded_image(image_file), "prompt": prompt})})
    print(result)
    return result.content

# メインの処理
def main():
    image_file = upload_image()
    if image_file:
        # 画像を表示
        st.image(image_file, caption='Uploaded Image', use_column_width=True)
        
        # プロンプトの入力欄
        prompt = st.text_input("Enter a prompt for image analysis:")
        
        if st.button("Analyze"):
            # 画像解析を実行し、結果を表示
            result = analyze_image(image_file, prompt)
            st.write("Analysis Result:")
            st.write(result)

if __name__ == "__main__":
    main()
