import streamlit as st

# 設定網頁標題
st.title("🚨變數與運算子")
st.write("請閱讀下方 20 道 Python 程式識讀題，並選出正確的輸出結果。全卷完成後點擊最下方按鈕送出。")
st.write("---")

# 每一題都以獨立線性程式碼呈現，確保無迴圈與函式呼叫
# ----------------------------------------------------
st.markdown("### 1. 第 1 題")
st.code("""a = 4
b = 5 + a * 3 - a // 3
a = a + b
print(a, b)""", language='python')
ans_1 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 24 20", "(B) 20 16", "(C) 21 17", "(D) 25 21", "(E) 執行錯誤"], key="q1")
st.write("---")

st.markdown("### 2. 第 2 題")
st.code("""a = (4 + 3) * (8 - 3 * 2)
b = (a - 2 * (a - 5)) * 2
print(a, b)""", language='python')
ans_2 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 14 -8", "(B) 14 0", "(C) 7 -4", "(D) 14 4", "(E) 執行錯誤"], key="q2")
st.write("---")

st.markdown("### 3. 第 3 題")
st.code("""x = 10
y = x + 2 = 12
print(x, y)""", language='python')
ans_3 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 10 12", "(B) 12 12", "(C) 10 14", "(D) 12 14", "(E) 執行錯誤"], key="q3")
st.write("---")

st.markdown("### 4. 第 4 題")
st.code("""x = 3
x = 4.5
y = 4 // 5 * 5
print(x, y)""", language='python')
ans_4 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 3 4", "(B) 4.5 4", "(C) 4.5 0", "(D) 3 0", "(E) 執行錯誤"], key="q4")
st.write("---")

st.markdown("### 5. 第 5 題，注意!!取餘數是找到比被除數還小的數字並檢查被除數與其的差距，而//其實是地板除法，除完如果不能整除則無條件往下一位")
st.code("""a = 17 % 5
b = -17 % 5
c = -17 // 5
print(a, b, c)""", language='python')
ans_5 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 2 -2 -3", "(B) 2 3 -4", "(C) 2 3 -3", "(D) 2 -2 -4", "(E) 執行錯誤"], key="q5")
st.write("---")

st.markdown("### 6. 第 6 題")
st.code("""x = 7
y = 4
x, y = y - 2, x - 2
print(x, y)""", language='python')
ans_6 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 2 5", "(B) 5 2", "(C) 2 2", "(D) 5 5", "(E) 執行錯誤"], key="q6")
st.write("---")

st.markdown("### 7. 第 7 題")
st.code("""a = 10
b = 20
a += b
b = a - b
a = a - b
print(a, b)""", language='python')
ans_7 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 10 20", "(B) 20 10", "(C) 30 20", "(D) 20 30", "(E) 執行錯誤"], key="q7")
st.write("---")

st.markdown("### 8. 第 8 題")
st.code("""a = True
b = False
c = not a or b and a
print(c)""", language='python')
ans_8 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) True", "(B) False", "(C) None", "(D) 0", "(E) 執行錯誤"], key="q8")
st.write("---")

st.markdown("### 9. 第 9 題")
st.code("""a = 5
b = 2
c = a ** b ** 2
print(c)""", language='python')
ans_9 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 25", "(B) 50", "(C) 625", "(D) 3125", "(E) 執行錯誤"], key="q9")
st.write("---")

st.markdown("### 10. 第 10 題")
st.code("""x = 5
y = 2
print(x / y, x // y)""", language='python')
ans_10 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 2.5 2", "(B) 2 2", "(C) 2.5 2.5", "(D) 2 2.5", "(E) 執行錯誤"], key="q10")
st.write("---")

st.markdown("### 11. 第 11 題")
st.code("""a = "10"
b = "20"
print(a + b)""", language='python')
ans_11 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 30", "(B) 1020", "(C) \"30\"", "(D) 2010", "(E) 執行錯誤"], key="q11")
st.write("---")

st.markdown("### 12. 第 12 題，注意!!4 >> 3 代表 4//2//2//2 , 4 << 3 代表4*2*2*2")
st.code("""a = 12
b = a >> 2
c = a << 1
print(b, c)""", language='python')
ans_12 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 3 24", "(B) 4 24", "(C) 3 48", "(D) 6 24", "(E) 執行錯誤"], key="q12")
st.write("---")

st.markdown("### 13. 第 13 題")
st.code("""x = 5
y = 10
z = x > 3 and y < 20 or x == 0
print(z)""", language='python')
ans_13 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) True", "(B) False", "(C) 1", "(D) 0", "(E) 執行錯誤"], key="q13")
st.write("---")

st.markdown("### 14. 第 14 題")
st.code("""a = 8
b = 3
a %= b + 2
print(a)""", language='python')
ans_14 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 0", "(B) 3", "(C) 2", "(D) 1", "(E) 執行錯誤"], key="q14")
st.write("---")

st.markdown("### 15. 第 15 題")
st.code("""x = "Python"
y = x * 2
print(y)""", language='python')
ans_15 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) PythonPython", "(B) Python 2", "(C) Python2", "(D) 執行錯誤", "(E) 以上皆非"], key="q15")
st.write("---")

st.markdown("### 16. 第 16 題")
st.code("""a = 15
b = 4
print(float(a // b))""", language='python')
ans_16 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 3.75", "(B) 3.0", "(C) 3", "(D) 4.0", "(E) 執行錯誤"], key="q16")
st.write("---")

st.markdown("### 17. 第 17 題")
st.code("""x = 5
y = 3
x, y = y, x
x = x + 1
print(x, y)""", language='python')
ans_17 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 4 5", "(B) 6 3", "(C) 4 3", "(D) 6 5", "(E) 執行錯誤"], key="q17")
st.write("---")

st.markdown("### 18. 第 18 題，注意!!數字做&運算須將數字轉為2進制")
st.code("""a = 6
b = 11
c = a & b
print(c)""", language='python')
ans_18 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 2", "(B) 6", "(C) 15", "(D) 0", "(E) 執行錯誤"], key="q18")
st.write("---")

st.markdown("### 19. 第 19 題")
st.code("""x = int("10") + float("2.5")
print(x)""", language='python')
ans_19 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 12.5", "(B) 12", "(C) \"12.5\"", "(D) 執行錯誤", "(E) 以上皆非"], key="q19")
st.write("---")

st.markdown("### 20. 第 20 題")
st.code("""a = 9
b = 2
print(a / b + a % b)""", language='python')
ans_20 = st.radio("執行上述程式碼後，輸出的結果為何？", ["(A) 5.5", "(B) 5.0", "(C) 4.5", "(D) 6.0", "(E) 執行錯誤"], key="q20")
st.write("---")


# 送出按鈕與計分
if st.button("送出解答"):
    score = 0
    if ans_1 == "(B) 20 16": score += 5
    if ans_2 == "(A) 14 -8": score += 5
    if ans_3 == "(E) 執行錯誤": score += 5
    if ans_4 == "(C) 4.5 0": score += 5
    if ans_5 == "(B) 20 16": score += 0 # 修正第5題計分基準
    if ans_5 == "(B) 2 3 -4": score += 5
    if ans_6 == "(A) 2 5": score += 5
    if ans_7 == "(B) 20 10": score += 5
    if ans_8 == "(B) False": score += 5
    if ans_9 == "(C) 625": score += 5
    if ans_10 == "(A) 2.5 2": score += 5
    if ans_11 == "(B) 1020": score += 5
    if ans_12 == "(A) 3 24": score += 5
    if ans_13 == "(A) True": score += 5
    if ans_14 == "(B) 3": score += 5
    if ans_15 == "(A) PythonPython": score += 5
    if ans_16 == "(B) 3.0": score += 5
    if ans_17 == "(A) 4 5": score += 5
    if ans_18 == "(A) 2": score += 5
    if ans_19 == "(A) 12.5": score += 5
    if ans_20 == "(A) 5.5": score += 5

    st.success(f"### 🎉 您的最終得分：{score} / 100 分")
    
    st.markdown("### 📌 20 題正確答案一覽")
    st.write("**第 1 題：** (B) 20 16" + ",你的答案：" + ans_1)
    st.write("**第 2 題：** (A) 14 -8" + ",你的答案：" + ans_2)
    st.write("**第 3 題：** (E) 執行錯誤" + ",你的答案：" + ans_3)
    st.write("**第 4 題：** (C) 4.5 0" + ",你的答案：" + ans_4)
    st.write("**第 5 題：** (B) 2 3 -4" + ",你的答案：" + ans_5)
    st.write("**第 6 題：** (A) 2 5" + ",你的答案：" + ans_6)
    st.write("**第 7 題：** (B) 20 10" + ",你的答案：" + ans_7)
    st.write("**第 8 題：** (B) False" + ",你的答案：" + ans_8)
    st.write("**第 9 題：** (C) 625" + ",你的答案：" + ans_9)
    st.write("**第 10 題：** (A) 2.5 2" + ",你的答案：" + ans_10)
    st.write("**第 11 題：** (B) 1020" + ",你的答案：" + ans_11)
    st.write("**第 12 題：** (A) 3 24" + ",你的答案：" + ans_12)
    st.write("**第 13 題：** (A) True" + ",你的答案：" + ans_13)
    st.write("**第 14 題：** (B) 3" + ",你的答案：" + ans_14)
    st.write("**第 15 題：** (A) PythonPython" + ",你的答案：" + ans_15)
    st.write("**第 16 題：** (B) 3.0" + ",你的答案：" + ans_16)
    st.write("**第 17 題：** (A) 4 5" + ",你的答案：" + ans_17)
    st.write("**第 18 題：** (A) 2" + ",你的答案：" + ans_18)
    st.write("**第 19 題：** (A) 12.5" + ",你的答案：" + ans_19)
    st.write("**第 20 題：** (A) 5.5" + ",你的答案：" + ans_20)
