import tkinter as tk
from tkinter import filedialog
import sys
from gather import getCotes
from convert import toCsv


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.folder_path = None
        self.title("Extracteur de données tridim")
        self.geometry("400x300")
        
        #Entrée cotes
        self.coteFrame = tk.Frame(self)
        self.label = tk.Label(self.coteFrame, text="cotes id (séparées avec \",\" sans espace)")
        self.label.pack(side=tk.LEFT)
        
        self.cotesText = tk.Entry(self.coteFrame)
        self.cotesText.pack(side=tk.LEFT)
        self.coteFrame.pack(pady=5)
        
        #Entrée dossier data
        self.fileFrame = tk.Frame(self)
        
        self.fileLabel = tk.Label(self.fileFrame, text="Séléctionnez un dossier")
        self.fileLabel.pack(side=tk.LEFT)
        
        self.button = tk.Button(self.fileFrame, text="Ouvrir", command=self.getFolder)
        self.button.pack(side=tk.LEFT)
        
        self.fileFrame.pack(pady=5)
        
        # #Entrée fichier modèle
        # self.fileFrame2 = tk.Frame(self)
        
        # self.fileLabel2 = tk.Label(self.fileFrame2, text="Séléctionnez un modèle")
        # self.fileLabel2.pack(side=tk.LEFT)
        
        # self.button2 = tk.Button(self.fileFrame2, text="Ouvrir", command=self.getFile)
        # self.button2.pack(side=tk.LEFT)
        
        # self.fileFrame2.pack(pady=5)
        
        #bouton valider
        self.startButton = tk.Button(self, text="Go !", command=self.convert)
        self.startButton.pack()
        
        #output
        
        self.text_widget = tk.Text(self, height=8, width=40)  # Adjust the height value here
        self.text_widget.pack(pady=10)
        
        # Redirect the standard output to the text widget
        sys.stdout = self.TextRedirector(self.text_widget)
        
        print("1 : Renseigner les cotes séparées UNIQUEMENT par une virgule\n2 : Choisir le dossier dans lequel la data se trouve")
    
    # def getFile(self):
    #     self.file_path = filedialog.askopenfilename()
    #     print("Modèle pris en compte : " + self.file_path)
    #     if self.file_path:
    #         self.fileLabel2.config(text="Modèle sélectionné : " + self.file_path[:35] + "...")
            
    def getFolder(self):
        self.folder_path = filedialog.askdirectory()
        print("Dossier contenant les data pris en compte : " + self.folder_path)
        if self.folder_path:
            self.fileLabel.config(text="Dossier sélectionné : " + self.folder_path[:35] + "...")
    
    def convert(self):
        print("En cours, veuillez patienter")
        cotes = getCotes(self.cotesText.get().split(","), self.folder_path,True)
        toCsv(cotes)
        
    class TextRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget
        
        def write(self, message):
            self.text_widget.insert(tk.END, message)
            self.text_widget.see(tk.END)
            
        def flush(self):
            pass