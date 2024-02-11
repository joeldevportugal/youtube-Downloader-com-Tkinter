# importar as Bibliotecas a usar ---------------------------------------------------
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import messagebox
from pytube import YouTube
import threading
import os
#-------------------------------------------------------------------------------------
# criar a função iniciar Download ----------------------------------------------------
def iniciar_download():
    url = Eurl.get()
    if url:
        try:
            yt = YouTube(url)
            if rdMp3_var.get():
                stream = yt.streams.filter(only_audio=True).first()
                file_extension = "mp3"
            elif rdMp4_var.get():
                stream = yt.streams.get_highest_resolution()
                file_extension = "mp4"
            else:
                messagebox.showwarning("Aviso", "Por favor, selecione um formato de download.")
                return

            file_path = filedialog.asksaveasfilename(defaultextension=f".{file_extension}")

            if not file_path:
                return

            progresso['value'] = 0
            progresso.start()
            threading.Thread(target=baixar_video, args=(stream, file_path)).start()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida.")
#--------------------------------------------------------------------------------------
# função para Limpar ------------------------------------------------------------------         
def limpar_objetos():
    rdMp3_var.set(0)
    rdMp4_var.set(0)
    Eurl.delete(0, END)
    progresso["value"] = 0
#--------------------------------------------------------------------------------------   
# criar a funcao para baixar Video ---------------------------------------------------- 
def baixar_video(stream, file_path):
    global progresso
    try:
        file_size = stream.filesize
        stream.download(output_path=os.path.dirname(file_path), filename=os.path.basename(file_path))
        messagebox.showinfo("Sucesso", "Download efetuado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o download: {str(e)}")
    finally:
        progresso.stop()
        progresso['value'] = file_size
#----------------------------------------------------------------------------------------        
# criar a função sair da aplicação ------------------------------------------------------
def sair_aplicacao():
    resposta = messagebox.askyesno("SAIR", "Tem certeza que deseja sair? sim /nâo")
    if resposta:
        Janela.destroy()
#---------------------------------------------------------------------------------------
# aqui vamos defenir as Nossa Cores a Usar --------------------------------------------- 
co0 ='#eeeee4' # cor para a entry
co1 ='#e07b39' # cor para os botões 
co2 ='#FFFFFF' # fundo da janela
#---------------------------------------------------------------------------------------
# Aqui vamos configurar a Nossa Janela ------------------------------------------------- 
Janela = Tk()
Janela.geometry('666x200+100+100')
Janela.title('Youtube downloader V1 dev Joel 2024 ©')
Janela.resizable(False, False)
Janela.configure(bg=co2)
Janela.iconbitmap('C:\\Users\HP\\Desktop\\Projectos\\Download\\icon.ico')
#----------------------------------------------------------------------------------------
# aqui vamos cria as variaveis de Controle dos Radiobutons-------------------------------
rdMp3_var = IntVar()
rdMp4_var = IntVar()
#----------------------------------------------------------------------------------------
# aqui vamos criar a entry para a url ---------------------------------------------------
Eurl = Entry(Janela, width=57, font=('arial 14'), bg=co0)
Eurl.place(x=10, y=10)
#-----------------------------------------------------------------------------------------
# Aqui vamos criar os nossos Botões Radiobuton -------------------------------------------
rdMp3 = Radiobutton(Janela, text='Formato Mp3', font=('arial 14'), variable=rdMp3_var, value=1, bg=co2)
rdMp3.place(x=10, y=40)
rdMp4 = Radiobutton(Janela, text='Formato Mp4', font=('arial 14'), variable=rdMp4_var, value=1, bg=co2)
rdMp4.place(x=155, y=40)
#-------------------------------------------------------------------------------------------
# Aqui vamos criar os nossos Botões --------------------------------------------------------
Bdown = Button(Janela, text='Download', relief=RAISED, overrelief=RIDGE, font=('arial 13'), command=iniciar_download, bg=co1)
Bdown.place(x=10, y=95)
Blimpar = Button(Janela, text='Limpar Obejectos', relief=RAISED, overrelief=RIDGE, font=('arial 13'), command=limpar_objetos, bg=co1)
Blimpar.place(x=100, y=95)
BSair = Button(Janela, text='Fechar Aplicacao', relief=RAISED, overrelief=RIDGE, font=('arial 13'), command=sair_aplicacao, bg=co1)
BSair.place(x=245, y=95)
#-------------------------------------------------------------------------------------------
# aqui vamos criar a nossa Barra de progresso ----------------------------------------------
progresso = Progressbar(Janela, orient=HORIZONTAL, length=630, mode='determinate')
progresso.place(x=10, y=150)
#-------------------------------------------------------------------------------------------
# aqui vamos Iniciar a Nossa Janela --------------------------------------------------------
Janela.mainloop()
#-------------------------------------------------------------------------------------------