import tkinter as tk
from tkinter import messagebox
import Data_Merge_in_dir
import os

# 윈도우 생성
window = tk.Tk()
window.title("데이터 정리")
window.geometry("350x450")
window.option_add("*Font", "맑은고딕 10")
window.resizable(True, True)
button_value = 0
path = ""

# Entry 위젯에서 경로를 가져옴
def list_files_in_directory():
    
    global path
    path = path_entry.get()
    if path:
        try:
            files = os.listdir(path)
            files_listbox.delete(0, tk.END)
            for file in files:
                files_listbox.insert(tk.END, file)
        except FileNotFoundError:
            messagebox.showerror("오류", f"지정된 경로 '{path}'를 찾을 수 없습니다.")
        except NotADirectoryError:
            messagebox.showerror("오류", f"'{path}'는 디렉토리가 아닙니다.")
        except PermissionError:
            messagebox.showerror("오류", f"'{path}'에 접근할 권한이 없습니다.")


# 버튼 클릭 이벤트 함수
   
def on_button1_click():
    messagebox.showinfo("알림", "ALL")
    global button_value
    button_value = 1
    Data_Merge_in_dir.Data_Merge_files(button_value, path)  
def on_button2_click():
    messagebox.showinfo("알림", "I-V")
    global button_value
    button_value = 2
    Data_Merge_in_dir.Data_Merge_files(button_value, path)
def on_button3_click():
    messagebox.showinfo("알림", "G-V")
    global button_value
    button_value = 3
    Data_Merge_in_dir.Data_Merge_files(button_value, path)
    
# 경로 입력
path_label = tk.Label(window, text = "경로 입력", font = ('15'))
path_entry = tk.Entry(window, font=('15') , width = 30)
check_button = tk.Button(window, text="확인", font = ('15'), command=list_files_in_directory)
files_listbox = tk.Listbox(window, width=20, height=10)

# 버튼 생성
button1 = tk.Button(window, text="ALL", command=on_button1_click, width = 15, height = 2)
button2 = tk.Button(window, text="I-V", command=on_button2_click, width = 15, height = 2)
button3 = tk.Button(window, text="G-V", command=on_button3_click, width = 15, height = 2)


# 버튼 배치
path_label.pack(pady=(5,5))
path_entry.pack(pady=10)
check_button.pack(pady=10)
files_listbox.pack(pady=10)

button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)


# 윈도우 실행
window.mainloop()

