import tkinter
import tkinter.messagebox
import tkinter.filedialog
import os

def select_text():
    root = tkinter.Tk()
    root.withdraw()
    fTyp = [("テキストファイル", "*.txt")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('NolaテキストUTF-16化・移動','テキストを選択！')
    text_pathes = tkinter.filedialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)
    root.quit()
    
    return list(text_pathes)

def fin():
    tk_second_root = tkinter.Tk()
    tk_second_root.title('おわったよ！')
    frame_second_main = tkinter.Frame(tk_second_root)
    frame_second_main.pack()
    
    text_label = tkinter.Label(frame_second_main, text = 'UTF-16化・移動完了', font=('', 30))
    text_label.pack(anchor = 'center')
    
    do_quit = tkinter.Button(frame_second_main, text = '閉じる', command = tk_second_root.quit)
    do_quit.pack(anchor='center')
    
    tk_second_root.mainloop()
    
def stop():
    tk_second_root = tkinter.Tk()
    tk_second_root.title('キャンセル')
    frame_second_main = tkinter.Frame(tk_second_root)
    frame_second_main.pack()
    
    text_label = tkinter.Label(frame_second_main, text = 'キャンセルされだよ！', font=('', 30))
    text_label.pack(anchor = 'center')
    
    do_quit = tkinter.Button(frame_second_main, text = '閉じる', command = tk_second_root.quit)
    do_quit.pack(anchor='center')
    
    tk_second_root.mainloop()