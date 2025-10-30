import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01_k24014():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    

    # カメラ画像をGoogleロゴと同じサイズにリサイズ
    capture_img_resized = cv2.resize(capture_img, (g_width, g_hight))
    print("リサイズ後のカメラ画像サイズ:", capture_img_resized.shape)
    
    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # リサイズ済みのカメラキャプチャ画像の対応する位置のピクセルで置き換え
                google_img[y, x] = capture_img_resized[y, x]

    # 書き込み処理
    cv2.imwrite('output_images/lecture05_01_k24014.png', google_img)
    app.write_image('output_images/lecture05_01_k24014.png')

if __name__ == "__main__":
    lecture05_01_k24014()
