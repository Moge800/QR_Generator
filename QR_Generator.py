import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk


def update_qr(event=None):
    global img_pil, img_tk  # グローバル変数としてPIL Imageオブジェクトを保持
    data = entry.get()
    if not data:  # 入力が空の場合は何もしない
        qr_label.config(image="")
        qr_label.image = None
        return
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img_pil = qr.make_image(fill="black", back_color="white")
    img_pil = img_pil.resize((512, 512), Image.LANCZOS)  # サイズを512x512に変更
    # PIL ImageをTkinter用に変換
    img_tk = ImageTk.PhotoImage(img_pil)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk


def save_qr(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img_pil.save(file_path)  # PIL Imageオブジェクトを保存


def clear_form(event=None):
    entry.delete(0, tk.END)  # 入力フォームをクリア
    qr_label.config(image="")  # QRコード表示をクリア


root = tk.Tk()
root.title("QRコード生成アプリ")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_qr)  # キーが離されたときにQRコードを更新

qr_label = tk.Label(root)
qr_label.pack(pady=10)
qr_label.bind("<Button-1>", save_qr)  # 左クリックイベントをバインド
qr_label.bind("<Button-3>", clear_form)  # 右クリックイベントをバインド

# 説明ラベルを追加
description_label = tk.Label(root, text="左クリック=保存 / 右クリック=クリア")
description_label.pack(pady=10)

root.mainloop()
