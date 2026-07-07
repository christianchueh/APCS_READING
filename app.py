import streamlit as st

# 1. 網頁基本設定
st.set_page_config(
    page_title="Python 程式設計識讀模擬測驗",
    page_icon="🐍",
    layout="wide"
)

# 2. 自訂 CSS 樣式（美化排版與配色）
st.markdown("""
    <style>
    .main-title {
        font-size: 42px !important;
        font-weight: 700;
        color: #3776AB;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 24px !important;
        color: #787878;
        margin-bottom: 30px;
    }
    .section-header {
        font-size: 28px !important;
        font-weight: 600;
        color: #1E293B;
        border-left: 6px solid #3776AB;
        padding-left: 12px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .highlight-text {
        color: #3776AB;
        font-weight: bold;
    }
    .custom-card {
        background-color: #F8FAFC;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        height: 100%;
    }
    .custom-card h4 {
        color: #3776AB;
        margin-top: 0;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== 主頁內容開始 ====================

# 頂部標題區
st.markdown('<div class="main-title">🐍 Python 程式設計基礎能力與識讀模擬測驗</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">專為「初學程式一學期」考生打造的邏輯思維指標</div>', unsafe_allow_html=True)

st.info("💡 **歡迎來到本測驗系統！** 本題庫專為 Python 初學者精心設計。我們不考刁鑽罕見的語法，而是專注於核心基礎，旨在精準評估考生的「基礎語法熟稔度」與「程式邏輯識讀能力」。")

# 區段一：為什麼這份測驗對你至關重要？
st.markdown('<div class="section-header">🎯 為什麼這份測驗對你至關重要？</div>', unsafe_allow_html=True)

st.write(
    "市面上許多檢定往往陷入「語法細節的死記硬背」，這反而加重了初學者的認知負擔。然而，"
    "程式設計的本質是**邏輯與流程的掌握**。因此，本測驗特別針對兩大核心能力進行深度評估："
)

# 使用 Columns 呈現兩大核心能力
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="custom-card">
        <h4>📦 核心語法與常用函數的實戰應用</h4>
        <p>嚴格篩選精簡、高頻率的內建指令，確保考生掌握最扎實的必備基本功，不被海量函式淹沒。</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="custom-card">
        <h4>🧠 關鍵程式邏輯與流程識讀能力</h4>
        <p>專注測試考生能否準確看懂一小段程式碼的運行軌跡與結果。<b>這是從「程式初學者」邁向「獨立解決問題者」最關鍵的邏輯分水嶺！</b></p>
    </div>
    """, unsafe_allow_html=True)

# 區段二：APCS 考前必練的黃金模擬指標
st.markdown('<div class="section-header">🏆 APCS 考前必練的黃金模擬指標</div>', unsafe_allow_html=True)

st.write(
    "如果您正準備參與 **APCS（大學程式設計先修檢測）**，這份題庫將是您不可或缺的策略性工具："
)

# 使用 st.success 區塊強調 APCS 的關聯性
st.success("""
* **緊扣最新趨勢：** 出題嚴格參考官方公告之**新制檢測題型與檢測範圍**，極具考前衝刺的參考價值。
* **跨語言的邏輯淬鍊：** 由於 APCS 需兼顧 C 語言與 Python 的跨平台對等性，實際考試範圍往往比想像中更精煉。本題庫精準鎖定這個交集，過濾掉不適合跨語言考查的語法特性，更全面性地涵蓋了 APCS 必考的邏輯核心。
""")

# 核心理念的金句強調節奏
st.warning("📣 **我們的核心理念：** 豐富的函數與多變的用法需要時間累積，不該成為初學者的絆腳石；但「看懂程式在做什麼」的邏輯思維，一刻都不能等。")

# 區段三：測驗範圍限定公告
st.markdown('<div class="section-header">📐 測驗範圍限定公告</div>', unsafe_allow_html=True)

st.write(
    "為了讓考生的複習方向更為聚焦，本系統對題目中出現的指令與函數進行了**嚴格限定**。"
    "我們將範圍限縮在最常用、最核心的基礎指令。範圍外的高階語法絕不出現，讓您能看清邊界、精準打擊弱點！"
)

# 底部導引呼籲 (CTA)
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h3 style="color: #FFD43B;">🚀 準備好挑戰您的識讀能力了嗎？</h3>
        <p style="font-size: 18px; color: #475569;">這不只是一份考卷，更是一次對思維深度的檢閱。</p>
    </div>
""", unsafe_allow_html=True)

# 提示引導至側邊欄的 Pages
st.info("👉 **開始測驗：** 請點選左側側邊欄的 **`Pages`（題目列表）** 開始挑戰您的程式識讀能力！")
