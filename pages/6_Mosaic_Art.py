import streamlit as st
from PIL import Image
import numpy as np
import os
import glob
from io import BytesIO

# --- (1) 事前準備: タイル画像フォルダのパス ---
TILE_DIR = "tile_images" 
# ※ このフォルダをアプリのルートディレクトリに作成し、
#    みんなの投稿写真をPNG/JPG形式で入れてください。

# --- (2) タイル画像の読み込みと平均色の計算 ---
@st.cache_resource
def load_and_analyze_tiles():
    tile_files = glob.glob(os.path.join(TILE_DIR, "*.[pj][np]g*")) # jpg, pngを検索
    
    if not tile_files:
        st.error(f"'{TILE_DIR}' フォルダにタイル画像が見つかりません。")
        return None, None
        
    tiles = []
    avg_colors = []
    
    for file_path in tile_files:
        try:
            tile = Image.open(file_path).convert("RGB")
            # すべてのタイルを同じサイズにリサイズ
            tile = tile.resize((16, 16)) # 例として16x16ピクセルに統一
            
            tile_np = np.array(tile)
            
            # 平均色を計算 (R, G, Bの平均値)
            avg_color = tile_np.mean(axis=(0, 1))
            
            tiles.append(tile)
            avg_colors.append(avg_color)
            
        except Exception as e:
            st.warning(f"タイル画像 {file_path} の読み込みに失敗しました: {e}")
            
    return tiles, np.array(avg_colors)

# --- (3) 最も近いタイルを見つける関数 ---
def get_closest_tile(target_color, avg_colors_np, tiles):
    # ユークリッド距離 (色の差) を計算
    # np.sum() を使うと高速に距離を計算できます
    distances = np.sum((avg_colors_np - target_color) ** 2, axis=1)
    
    # 距離が最小のインデックスを取得
    closest_index = np.argmin(distances)
    
    return tiles[closest_index]

# --- メインロジック ---

st.set_page_config(page_title="フォトモザイクアートメーカー", layout="wide")
st.title('🖼️ みんなの写真でモザイクアート')
st.markdown('写真をアップロードすると、みんなが投稿した写真を使ってモザイク化します。')

# タイルデータの準備
tiles, avg_colors = load_and_analyze_tiles()

if tiles is None:
    st.stop() # タイル画像がなければ停止

uploaded_file = st.file_uploader("元となる画像をアップロードしてください", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    original_image = Image.open(uploaded_file).convert("RGB")
    
    # --- サイドバーでの設定 ---
    with st.sidebar:
        st.header("設定")
        # タイルサイズ (タイル画像のサイズと同じ 16x16 を前提とする)
        tile_size = 16 
        
        # モザイクの粗さ (元画像を何分の1に縮小するか)
        # 10の場合、元画像が1/10のサイズになり、そこにタイルが敷き詰められる
        reduction_factor = st.slider(
            "モザイクの粗さ (値が大きいほどタイルが細かくなります)",
            min_value=5,
            max_value=50,
            value=20,
            step=5
        )
        
        # 処理開始ボタン
        process_button = st.button("モザイクアートを生成開始")

    if process_button:
        with st.spinner('モザイクアートを生成中...'):
            # 元画像を縮小 (処理速度のため)
            w, h = original_image.size
            new_w = w // reduction_factor
            new_h = h // reduction_factor
            
            # 縮小された画像がモザイクの設計図となる
            resized_img = original_image.resize((new_w, new_h))
            resized_np = np.array(resized_img)
            
            # モザイクアートの最終サイズ (タイルサイズ * 設計図のサイズ)
            final_w = new_w * tile_size
            final_h = new_h * tile_size
            
            # 最終的なモザイクアートを格納する画像
            mosaic_art = Image.new('RGB', (final_w, final_h))

            # 設計図（resized_np）の各ピクセルに対して、最も近い色のタイルを貼り付ける
            for y in range(new_h):
                for x in range(new_w):
                    # 設計図のピクセルの色を取得
                    target_color = resized_np[y, x]
                    
                    # 最も近いタイルを選択
                    closest_tile = get_closest_tile(target_color, avg_colors, tiles)
                    
                    # モザイクアートの対応する位置にタイル画像を貼り付ける
                    mosaic_art.paste(
                        closest_tile, 
                        (x * tile_size, y * tile_size)
                    )

            # 最終結果の表示
            st.image(mosaic_art, caption="完成したモザイクアート", use_column_width=True)
            
            # ダウンロードボタン
            buf = BytesIO()
            mosaic_art.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(
                label="モザイクアートをダウンロード (PNG)",
                data=byte_im,
                file_name="photo_mosaic_art.png",
                mime="image/png"
            )

st.markdown("---")
st.info('※ モザイクアート機能を実現するには、ルートディレクトリに `tile_images` フォルダを作成し、タイルとして使う画像（みんなの投稿写真）を入れてデプロイする必要があります。')
