import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="一維迴圈與陣列測驗", page_icon="🚨")
st.title("🚨 一維迴圈與陣列 程式識讀測驗")
st.write("本測驗共有 20 題程式識讀選擇題，請追蹤程式碼並選出正確的輸出結果。")

# 1. 定義 20 道題目資料 (題目、選項、正確答案)
questions = [
    {
        "code": "a = [1, 2, 3, 4, 5]\ns = 0\nfor x in a:\n    if x % 2 == 1:\n        s += x\nprint(s)",
        "options": ["(A) 6", "(B) 9", "(C) 15", "(D) 8"],
        "answer": "(B) 9"
    },
    {
        "code": "a = [5, 3, 8, 2]\nfor i in range(len(a)):\n    a[i] = a[i] * 2\nprint(a[1])",
        "options": ["(A) 10", "(B) 6", "(C) 16", "(D) 4"],
        "answer": "(B) 6"
    },
    {
        "code": "a = [10, 20, 30, 40, 50]\nprint(sum(a[1:4]))",
        "options": ["(A) 90", "(B) 60", "(C) 140", "(D) 100"],
        "answer": "(B) 60"
    },
    {
        "code": "a = [1, 3, 5, 7, 9]\ni = 0\nwhile i < len(a):\n    if a[i] == 5:\n        break\n    i += 1\nprint(i)",
        "options": ["(A) 1", "(B) 2", "(C) 3", "(D) 5"],
        "answer": "(B) 2"
    },
    {
        "code": "a = [3, 1, 4, 1, 5, 9]\nb = []\nfor x in a:\n    if x > 3:\n        b.append(x)\nprint(b)",
        "options": ["(A) [4, 5, 9]", "(B) [3, 4, 5, 9]", "(C) [4, 5]", "(D) [1, 1]"],
        "answer": "(A) [4, 5, 9]"
    },
    {
        "code": "a = [1, 2, 3]\nb = [4, 5, 6]\nc = []\nfor i in range(len(a)):\n    c.append(a[i] + b[i])\nprint(c[1])",
        "options": ["(A) 5", "(B) 7", "(C) 9", "(D) 8"],
        "answer": "(B) 7"
    },
    {
        "code": "a = [8, 4, 6, 2, 7]\nm = a[0]\nfor x in a:\n    if x < m:\n        m = x\nprint(m)",
        "options": ["(A) 8", "(B) 7", "(C) 2", "(D) 4"],
        "answer": "(C) 2"
    },
    {
        "code": "a = [1, 2, 3, 4]\nfor i in range(len(a)-1):\n    a[i], a[i+1] = a[i+1], a[i]\nprint(a)",
        "options": ["(A) [4, 3, 2, 1]", "(B) [2, 3, 4, 1]", "(C) [2, 1, 4, 3]", "(D) [1, 2, 3, 4]"],
        "answer": "(B) [2, 3, 4, 1]"
    },
    {
        "code": "a = [0] * 5\nfor i in range(5):\n    a[i] = i * i\nprint(a[3])",
        "options": ["(A) 4", "(B) 9", "(C) 16", "(D) 6"],
        "answer": "(B) 9"
    },
    {
        "code": "a = [2, 4, 6, 8, 10]\ns = 0\nfor i in range(0, len(a), 2):\n    s += a[i]\nprint(s)",
        "options": ["(A) 12", "(B) 18", "(C) 30", "(D) 20"],
        "answer": "(B) 18"
    },
    {
        "code": "a = [5, 2, 9, 1, 7]\ncount = 0\nfor x in a:\n    if x >= 5:\n        count += 1\nprint(count)",
        "options": ["(A) 2", "(B) 3", "(C) 4", "(D) 5"],
        "answer": "(B) 3"
    },
    {
        "code": "a = [1, 2, 3]\nfor i in range(2):\n    a.append(a[i] * 10)\nprint(len(a))",
        "options": ["(A) 3", "(B) 4", "(C) 5", "(D) 6"],
        "answer": "(C) 5"
    },
    {
        "code": "a = [12, 34, 56, 78]\ns = \"\"\nfor x in a:\n    s += str(x)[0]\nprint(s)",
        "options": ["(A) 12345678", "(B) 1357", "(C) 2468", "(D) 12"],
        "answer": "(B) 1357"
    },
    {
        "code": "a = [1, -2, 3, -4, 5]\nfor i in range(len(a)):\n    if a[i] < 0:\n        a[i] = 0\nprint(sum(a))",
        "options": ["(A) 3", "(B) 9", "(C) 15", "(D) 5"],
        "answer": "(B) 9"
    },
    {
        "code": "a = [1, 2, 3, 4, 5]\ni = 4\nwhile i >= 0:\n    if a[i] % 2 == 0:\n        print(a[i])\n        break\n    i -= 1",
        "options": ["(A) 2", "(B) 4", "(C) 5", "(D) 0"],
        "answer": "(B) 4"
    },
    {
        "code": "a = [3, 3, 4, 5, 3]\nc = 0\nfor x in a:\n    if x == 3:\n        c += 1\nprint(c)",
        "options": ["(A) 1", "(B) 2", "(C) 3", "(D) 4"],
        "answer": "(C) 3"
    },
    {
        "code": "a = [1, 2, 3, 4, 5]\nb = a[::-1]\nprint(b[1])",
        "options": ["(A) 1", "(B) 2", "(C) 4", "(D) 5"],
        "answer": "(C) 4"
    },
    {
        "code": "a = [1, 5, 2, 5, 3]\nm = max(a)\nidx = 0\nfor i in range(len(a)):\n    if a[i] == m:\n        idx = i\n        break\nprint(idx)",
        "options": ["(A) 1", "(B) 3", "(C) 5", "(D) 4"],
        "answer": "(A) 1"
    },
    {
        "code": "a = [1, 2, 3]\nfor x in a:\n    x = x + 10\nprint(a[0])",
        "options": ["(A) 11", "(B) 1", "(C) 10", "(D) 0"],
        "answer": "(B) 1"
    },
    {
        "code": "a = [10, 20, 30]\na.pop(1)\na.append(40)\nprint(a)",
        "options": ["(A) [10, 30, 40]", "(B) [10, 20, 40]", "(C) [20, 30, 40]", "(D) [10, 40]"],
        "answer": "(A) [10, 30, 40]"
    }
]

# 2. 渲染測驗題目（使用 st.radio 收集答案，不包裝在任何自訂 def 中）
user_answers = []

for idx, q in enumerate(questions):
    st.markdown(f"### **第 {idx + 1} 題**")
    st.code(q["code"], language="python")
    # 利用 radio 的 key 屬性確保狀態獨立
    ans = st.radio(
        "請選擇正確的輸出結果：", 
        q["options"], 
        key=f"q_{idx}",
        index=None,
        placeholder="尚未選擇"
    )
    user_answers.append(ans)
    st.write("---")

# 3. 計算得分與顯示答案面板
if st.button("🚨 送出解答", type="primary"):
    score = 0
    unanswered = False
    
    # 計算分數
    for idx, q in enumerate(questions):
        if user_answers[idx] == q["answer"]:
            score += 5
        if user_answers[idx] is None:
            unanswered = True
            
    if unanswered:
        st.warning("⚠️ 您還有題目尚未作答，分數已就現有作答結算。")
        
    # 呈現最終得分
    st.success(f"## 🎯 您的最終得分：{score} / 100 分")
    
    # 一次呈現 20 題的答案（不用詳解）
    st.markdown("### 📌 本測驗全體正確答案總覽")
    
    # 運用 4 個欄位並排呈現，畫面更乾淨
    col1, col2, col3, col4 = st.columns(4)
    for idx, q in enumerate(questions):
        target_col = [col1, col2, col3, col4][idx % 4]
        target_col.markdown(f"**第 {idx+1} 題：** `{q['answer']}`")
