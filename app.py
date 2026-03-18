import streamlit as st
import anthropic

st.title("🌸 ギャル語変換機")
st.caption("普通の文章をギャル語に変換します！")

text = st.text_area("変換したい文章を入力してください", placeholder="例：今日は疲れました", height=150)

if st.button("ギャル語に変換する✌️"):
    if text:
        with st.spinner("変換中...💅"):
            client = anthropic.Anthropic()
            prompt = f"""
以下の文章をギャル語に変換してください。

ルール：
- 語尾を「〜じゃん」「〜だし」「〜くない？」「〜だよね」などギャルっぽくする
- 絵文字を適度に使う
- テンションを上げる
- 短縮語を使う（「マジ」「ヤバ」「ウケる」「草」など）
- 元の意味は変えない

文章：{text}

ギャル語に変換した文章だけを出力してください。
"""
            message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            st.write(message.content[0].text)
    else:
        st.warning("文章を入力してください")

st.divider()
st.caption("※このツールはエンタメ用です。変換結果を保証するものではありません。")