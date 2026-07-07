import streamlit as st

# 設定網頁標題
st.title("🚨一維迴圈與陣列 程式識讀測驗")
st.write("本測驗共有 20 題程式識讀選擇題，請追蹤程式碼並選出正確的輸出結果。全卷完成後點擊最下方按鈕送出。")
st.write("---")

# ----------------------------------------------------
st.markdown("### 1. 第 1 題")
st.code("""a = [1, 2, 3, 4, 5]
s = 0
for x in a:
    if x % 2 == 1:
        s += x
print(s)""", language='python')
ans_1 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 6", "(B) 9", "(C) 15", "(D) 8"], key="q1")
st.write("---")

st.markdown("### 2. 第 2 題")
st.code("""a = [5, 3, 8, 2]
for i in range(len(a)):
    a[i] = a[i] * 2
print(a[1])""", language='python')
ans_2 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 10", "(B) 6", "(C) 16", "(D) 4"], key="q2")
st.write("---")

st.markdown("### 3. 第 3 題")
st.code("""a = [10, 20, 30, 40, 50]
print(sum(a[1:4]))""", language='python')
ans_3 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 90", "(B) 60", "(C) 140", "(D) 100"], key="q3")
st.write("---")

st.markdown("### 4. 第 4 題")
st.code("""a = [1, 3, 5, 7, 9]
i = 0
for i in range(5):
    if a[i] == 5:
        break
    i += 1
print(i)""", language='python')
ans_4 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 1", "(B) 2", "(C) 3", "(D) 5"], key="q4")
st.write("---")

st.markdown("### 5. 第 5 題")
st.code("""a = [3, 1, 4, 1, 5, 9]
b = []
for x in a:
    if x > 3:
        b.append(x)
print(b)""", language='python')
ans_5 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) [4, 5, 9]", "(B) [3, 4, 5, 9]", "(C) [4, 5]", "(D) [1, 1]"], key="q5")
st.write("---")

st.markdown("### 6. 第 6 題")
st.code("""a = [1, 2, 3]
b = [4, 5, 6]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print(c[1])""", language='python')
ans_6 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 5", "(B) 7", "(C) 9", "(D) 8"], key="q6")
st.write("---")

st.markdown("### 7. 第 7 題")
st.code("""a = [8, 4, 6, 2, 7]
m = a[0]
for x in a:
    if x < m:
        m = x
print(m)""", language='python')
ans_7 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 8", "(B) 7", "(C) 2", "(D) 4"], key="q7")
st.write("---")

st.markdown("### 8. 第 8 題")
st.code("""a = [1, 2, 3, 4]
for i in range(len(a)-1):
    a[i], a[i+1] = a[i+1], a[i]
print(a)""", language='python')
ans_8 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) [4, 3, 2, 1]", "(B) [2, 3, 4, 1]", "(C) [2, 1, 4, 3]", "(D) [1, 2, 3, 4]"], key="q8")
st.write("---")

st.markdown("### 9. 第 9 題")
st.code("""a = [0] * 5
for i in range(5):
    a[i] = i * i
print(a[3])""", language='python')
ans_9 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 4", "(B) 9", "(C) 16", "(D) 6"], key="q9")
st.write("---")

st.markdown("### 10. 第 10 題")
st.code("""a = [2, 4, 6, 8, 10]
s = 0
for i in range(0, len(a), 2):
    s += a[i]
print(s)""", language='python')
ans_10 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 12", "(B) 18", "(C) 30", "(D) 20"], key="q10")
st.write("---")

st.markdown("### 11. 第 11 題")
st.code("""a = [5, 2, 9, 1, 7]
count = 0
for x in a:
    if x >= 5:
        count += 1
print(count)""", language='python')
ans_11 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 2", "(B) 3", "(C) 4", "(D) 5"], key="q11")
st.write("---")

st.markdown("### 12. 第 12 題")
st.code("""a = [1, 2, 3]
for i in range(2):
    a.append(a[i] * 10)
print(len(a))""", language='python')
ans_12 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 3", "(B) 4", "(C) 5", "(D) 6"], key="q12")
st.write("---")

st.markdown("### 13. 第 13 題")
st.code("""a = [12, 34, 56, 78]
s = ""
for x in a:
    s += str(x)
print(s)""", language='python')
ans_13 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 12345678", "(B) 1357", "(C) 2468", "(D) 12"], key="q13")
st.write("---")

st.markdown("### 14. 第 14 題")
st.code("""a = [1, -2, 3, -4, 5]
for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
print(sum(a))""", language='python')
ans_14 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 3", "(B) 9", "(C) 15", "(D) 5"], key="q14")
st.write("---")

st.markdown("### 15. 第 15 題")
st.code("""a = [1, 2, 3, 4, 5]
i = 4
for i in range(4,-1,-1):
    if a[i] % 2 == 0:
        print(a[i])
        break
    i -= 1""", language='python')
ans_15 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 2", "(B) 4", "(C) 5", "(D) 0"], key="q15")
st.write("---")

st.markdown("### 16. 第 16 題")
st.code("""a = [3, 3, 4, 5, 3]
c = 0
for x in a:
    if x == 3:
        c += 1
print(c)""", language='python')
ans_16 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 1", "(B) 2", "(C) 3", "(D) 4"], key="q16")
st.write("---")

st.markdown("### 17. 第 17 題")
st.code("""a = [1, 2, 3, 4, 5]
b = a[::-1]
print(b[1])""", language='python')
ans_17 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 1", "(B) 2", "(C) 4", "(D) 5"], key="q17")
st.write("---")

st.markdown("### 18. 第 18 題")
st.code("""a = [1, 5, 2, 5, 3]
m = max(a)
idx = 0
for i in range(len(a)):
    if a[i] == m:
        idx = i
        break
print(idx)""", language='python')
ans_18 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 1", "(B) 3", "(C) 5", "(D) 4"], key="q18")
st.write("---")

st.markdown("### 19. 第 19 題")
st.code("""a = [1, 2, 3]
for x in a:
    x = x + 10
print(a[0])""", language='python')
ans_19 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 11", "(B) 1", "(C) 10", "(D) 0"], key="q19")
st.write("---")

st.markdown("### 20. 第 20 題")
st.code("""a = [10, 20, 30]
a.pop(1)
a.append(40)
print(a)""", language='python')
ans_20 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) [10, 30, 40]", "(B) [10, 20, 40]", "(C) [20, 30, 40]", "(D) [10, 40]"], key="q20")
st.write("---")


# 送出按鈕與計分
if st.button("送出解答"):
    score = 0
    if ans_1 == "(B) 9": score += 5
    if ans_2 == "(B) 6": score += 5
    if ans_3 == "(A) 90": score += 5
    if ans_4 == "(B) 2": score += 5
    if ans_5 == "(A) [4, 5, 9]": score += 5
    if ans_6 == "(B) 7": score += 5
    if ans_7 == "(C) 2": score += 5
    if ans_8 == "(B) [2, 3, 4, 1]": score += 5
    if ans_9 == "(B) 9": score += 5
    if ans_10 == "(B) 18": score += 5
    if ans_11 == "(B) 3": score += 5
    if ans_12 == "(C) 5": score += 5
    if ans_13 == "(A) 12345678": score += 5
    if ans_14 == "(B) 9": score += 5
    if ans_15 == "(B) 4": score += 5
    if ans_16 == "(C) 3": score += 5
    if ans_17 == "(C) 4": score += 5
    if ans_18 == "(A) 1": score += 5
    if ans_19 == "(B) 1": score += 5
    if ans_20 == "(A) [10, 30, 40]": score += 5

    st.success(f"### 🎉 您的最終得分：{score} / 100 分")
    
    st.markdown("### 📌 20 題正確答案一覽")
    st.write("**第 1 題：** (B) 9" + " , 你的答案：" + str(ans_1))
    st.write("**第 2 題：** (B) 6" + " , 你的答案：" + str(ans_2))
    st.write("**第 3 題：** (A) 90" + " , 你的答案：" + str(ans_3))
    st.write("**第 4 題：** (B) 2" + " , 你的答案：" + str(ans_4))
    st.write("**第 5 題：** (A) [4, 5, 9]" + " , 你的答案：" + str(ans_5))
    st.write("**第 6 題：** (B) 7" + " , 你的答案：" + str(ans_6))
    st.write("**第 7 題：** (C) 2" + " , 你的答案：" + str(ans_7))
    st.write("**第 8 題：** (B) [2, 3, 4, 1]" + " , 你的答案：" + str(ans_8))
    st.write("**第 9 題：** (B) 9" + " , 你的答案：" + str(ans_9))
    st.write("**第 10 題：** (B) 18" + " , 你的答案：" + str(ans_10))
    st.write("**第 11 題：** (B) 3" + " , 你的答案：" + str(ans_11))
    st.write("**第 12 題：** (C) 5" + " , 你的答案：" + str(ans_12))
    st.write("**第 13 題：** (A) 12345678" + " , 你的答案：" + str(ans_13))
    st.write("**第 14 題：** (B) 9" + " , 你的答案：" + str(ans_14))
    st.write("**第 15 題：** (B) 4" + "  ,你的答案：" + str(ans_15))
    st.write("**第 16 題：** (C) 3" + " , 你的答案：" + str(ans_16))
    st.write("**第 17 題：** (C) 4" + " , 你的答案：" + str(ans_17))
    st.write("**第 18 題：** (A) 1" + " , 你的答案：" + str(ans_18))
    st.write("**第 19 題：** (B) 1" + " , 你的答案：" + str(ans_19))
    st.write("**第 20 題：** (A) [10, 30, 40]" + " , 你的答案：" + str(ans_20))
