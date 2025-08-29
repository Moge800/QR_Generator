# QR Code Generator / QRコード生成アプリ

## English

### Description
A simple QR code generator application built with Python and Tkinter. This application allows you to generate QR codes in real-time as you type and save them as PNG files.

### Features
- Real-time QR code generation as you type
- Save QR codes as PNG files
- Clear input with right-click
- Simple and intuitive GUI interface

### Requirements
- Python 3.7 or higher
- Required packages (see requirements.txt.txt)

### Installation
1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt.txt
   ```

### Usage
1. Run the application:
   ```bash
   python QR_Generator.py
   ```
2. Enter text in the input field - QR code will be generated automatically
3. Left-click on the QR code to save it as a PNG file
4. Right-click on the QR code to clear the input field

### Building Executable (Optional)
To create a standalone executable, you can use Nuitka:
```bash
nuitka --standalone --onefile --follow-imports --remove-output --windows-console-mode=disable --lto=yes --enable-plugin=tk-inter QR_Generator.py
```

### License
Licensed under the Apache License 2.0. See `license.txt` for details.

---

## 日本語

### 説明
PythonとTkinterで作られたシンプルなQRコード生成アプリケーションです。入力したテキストからリアルタイムでQRコードを生成し、PNGファイルとして保存することができます。

### 機能
- 入力と同時にリアルタイムでQRコード生成
- QRコードをPNGファイルとして保存
- 右クリックで入力をクリア
- シンプルで直感的なGUIインターフェース

### 必要環境
- Python 3.7以上
- 必要なパッケージ（requirements.txt.txtを参照）

### インストール
1. このリポジトリをクローンまたはダウンロード
2. 必要な依存関係をインストール:
   ```bash
   pip install -r requirements.txt.txt
   ```

### 使用方法
1. アプリケーションを実行:
   ```bash
   python QR_Generator.py
   ```
2. 入力フィールドにテキストを入力 - QRコードが自動的に生成されます
3. QRコードを左クリックしてPNGファイルとして保存
4. QRコードを右クリックして入力フィールドをクリア

### 実行ファイルの作成（オプション）
Nuitkaを使用してスタンドアロンの実行ファイルを作成できます:
```bash
nuitka --standalone --onefile --follow-imports --remove-output --windows-console-mode=disable --lto=yes --enable-plugin=tk-inter QR_Generator.py
```

### ライセンス
Apache License 2.0でライセンスされています。詳細は`license.txt`をご覧ください。