# 🖼️ Background Remover (Auto EXE Build)

A simple tool for removing image backgrounds automatically.  
Just run the executable (`.exe`), and all images in the current folder will be processed.  
The background-removed results will be saved in the `output/` folder.  

---

## 🚀 Features
- Automatic background removal with **u2net** model (high quality)  
- Output resized to fixed **900px width** (height proportional)  
- Multi-core parallel processing (faster on stronger machines)  
- Output in **PNG** format with **72 DPI**  
- No Python installation required – just double-click the exe  

---

## 📥 Download (Windows)
You can download the latest executable from the **Releases** section:

👉 [Download Latest Release](https://github.com/amirsaeedsadeghi/remove-bg/releases/latest/download/RemoveBG.exe)

---

## 📂 How to Use
1. Place `RemoveBG.exe` in a folder.  
2. Copy all your input images (`.jpg`, `.jpeg`, `.png`) into the same folder.  
3. Double-click on `RemoveBG.exe`.  
4. After processing, the final images will appear in a new folder called `output/`.  

---

## ⚠️ Important Notes
- This program has been tested and built for **Windows 10 and 11**.  
- On **Windows 7** it may not work due to missing system DLLs.  
  - If you require Windows 7 support, you need to rebuild the exe on Windows 7 with Python 3.9 and PyInstaller.  

---

## 🛠️ Run from Source (For Developers)
If you want to run the Python source directly:  

```bash
git clone https://github.com/amirsaeedsadeghi/remove-bg.git
cd remove-bg
pip install -r requirements.txt
python RemoveBG.py
```

---

## 📜 License
This project is released under the MIT License.  
Feel free to use and modify, but please credit the source if you share it.