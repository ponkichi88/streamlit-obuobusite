import streamlit as st
from PIL import Image
import numpy as np # 画像を数値データとして扱うため

st.set_page_config(
    page_title="モザイクアートメーカー",
    layout="centered" # 中央に寄せるレイアウト
)

st.title('🎨 モザイクアートメーカー')
st.markdown('画像をアップロードして、あなただけのモザイクアートを作ってみましょう！')

# ----------------------------------------------------
# 1. 画像のアップロード
# ----------------------------------------------------
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # アップロードされたファイルをPIL Imageとして開く
    original_image = Image.open(uploaded_file)
    
    st.subheader("アップロードされた元の画像")
    st.image(original_image, caption="元の画像", use_column_width=True)
    
    st.markdown("---")

    # ----------------------------------------------------
    # 2. モザイクの粗さの調整
    # ----------------------------------------------------
    st.subheader("モザイクの粗さを調整")
    pixel_size = st.slider(
        "モザイクのピクセルサイズ (値が大きいほど粗くなります)",
        min_value=1,
        max_value=50, # モザイクの最大サイズ
        value=10,     # デフォルトのモザイクサイズ
        step=1
    )

    # ----------------------------------------------------
    # 3. モザイクアートの作成
    # ----------------------------------------------------
    st.subheader("モザイクアート")
    
    if st.button("モザイクアートを作成"):
        with st.spinner('モザイクアートを生成中...'):
            # 画像をNumPy配列に変換
            img_np = np.array(original_image)
            
            # モザイク処理の実行
            # 画像を pixel_size x pixel_size のブロックに分割し、各ブロックの平均色で塗りつぶす
            height, width, _ = img_np.shape
            
            # 出力画像用の配列を初期化
            mosaic_img_np = np.zeros_like(img_np)
            
            for y in range(0, height, pixel_size):
                for x in range(0, width, pixel_size):
                    # 各ブロックの領域を定義
                    y_end = min(y + pixel_size, height)
                    x_end = min(x + pixel_size, width)
                    
                    # ブロック内の平均色を計算
                    block = img_np[y:y_end, x:x_end]
                    avg_color = block.mean(axis=(0, 1)).astype(np.uint8)
                    
                    # ブロックを平均色で塗りつぶす
                    mosaic_img_np[y:y_end, x:x_end] = avg_color
            
            # NumPy配列をPIL Imageに戻す
            mosaic_image = Image.fromarray(mosaic_img_np)
            
            st.image(mosaic_image, caption=f"モザイクサイズ: {pixel_size}", use_column_width=True)
            
            # ダウンロードボタンの追加 (オプション)
            # 画像をバイトデータに変換してダウンロードできるようにする
            from io import BytesIO
            buf = BytesIO()
            mosaic_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(
                label="モザイクアートをダウンロード (PNG)",
                data=byte_im,
                file_name="mosaic_art.png",
                mime="image/png"
            )
else:
    st.info('まだ画像がアップロードされていません。')