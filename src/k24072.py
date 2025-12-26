import numpy as np
import cv2
from my_module.K24072.lecture05_camera_image_capture import MyVideoCapture  # ← 自分の学籍番号に合わせて

def lecture05_01():
    # --- カメラキャプチャ実行 ---
    app = MyVideoCapture()
    app.run()  # qキーで撮影終了

    # --- 画像読み込み ---
    google_img: cv2.Mat = cv2.imread('images/google.png')
    capture_img: cv2.Mat = app.get_img()  # ← () を忘れずに！

    # --- キャプチャ画像がNoneならエラー表示して終了 ---
    if capture_img is None:
        print("エラー: カメラ画像が取得できませんでした。run() 内で 'q' を押しましたか？")
        return

    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape

    print("google.png :", google_img.shape)
    print("capture_img:", capture_img.shape)

    # --- キャプチャ画像を敷き詰める ---
    tiled_img = np.zeros_like(google_img)
    for y in range(0, g_height, c_height):
        for x in range(0, g_width, c_width):
            h_end = min(y + c_height, g_height)
            w_end = min(x + c_width, g_width)
            tiled_img[y:h_end, x:w_end] = capture_img[0:h_end - y, 0:w_end - x]

    # --- 白色部分を置換 ---
    white_mask = np.all(google_img == [255, 255, 255], axis=2)
    result_img = google_img.copy()
    result_img[white_mask] = tiled_img[white_mask]

    # --- 出力フォルダ作成（os未使用） ---
    try:
        __import__('pathlib').Path('output_images').mkdir()
    except:
        pass

    # --- 画像保存 ---
    output_path = 'output_images/lecture05_01_K24072.png'
    cv2.imwrite(output_path, result_img)
    print(f"保存完了: {output_path}")

if __name__ == "__main__":
    lecture05_01()