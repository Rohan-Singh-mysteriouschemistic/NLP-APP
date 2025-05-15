"""
This Python script creates a GUI-based NLP application using Tkinter and the NLP Cloud API.

Note:
- The GUI make take a while to give response because of the NLPCLOUD response speed.
- Use your own cloud token to start the GUI.
- If it not working reasons will be:- 
                        - Daily usage limit of the cloud token has been exhausted.
                        - NLP Cloud is not responding.
"""

from tkinter import *
from tkinter import messagebox
import nlpcloud
from mydatabase import Database

class Nlp_Project():
    __Cloud_Token="157035a6de3143ff35a893134b7a6f1be0e41995"

    def __init__(self):
        self.database= Database()
        self.root=Tk()
        self.__Main_heading= Label(self.root, text="NLP", bg="#2DDEEB", font=("Baufra", 20, "bold"))
        self.root.iconbitmap(r"D:\NLPApp\favicon.ico")
        self.root.title("NLPAPP")
        self.root.configure(bg="#2DDEEB")
        self.Login()
        self.root.mainloop()

    def Clear(self):
        cnt=0
        for i in self.root.pack_slaves():
            if cnt==0:
                cnt+=1
                continue
            i.destroy()

    def Login(self):
        self.Clear()
        self.__Main_heading.pack(pady=20)

        Label(self.root, text="User Email", bg="#2DDEEB", font=("Arial", 12)).pack(pady=5)
        self.Input_Email= Entry(self.root, width=40, font=("Arial", 11))
        self.Input_Email.pack(pady=5)

        Label(self.root, text="Passwrod", bg="#2DDEEB", font=("Arial", 12)).pack(pady=5)
        self.Input_Password= Entry(self.root, show='*', width=40, font=("Arial", 11))
        self.Input_Password.pack(pady=5)

        Button(self.root, text="Login", command=self.Check_Credentials, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

        Label(self.root, text="New User?", bg="#2DDEEB", font=("Arial", 11)).pack(pady=5)
        Button(self.root, text="Register Now", command=self.Register, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

    def Register(self):
        self.Clear()

        self.__Main_heading.pack(pady=20)

        Label(self.root, text="User Name", bg="#2DDEEB", font=("Arial", 12)).pack(pady=5)
        self.User_Name= Entry(self.root, width=40, font=("Arial", 11))
        self.User_Name.pack(pady=5)

        Label(self.root, text="Passwrod", bg="#2DDEEB", font=("Arial", 12)).pack(pady=5)
        self.Password= Entry(self.root, show='*', width=40, font=("Arial", 11))
        self.Password.pack(pady=5)

        Label(self.root, text="Email", bg="#2DDEEB", font=("Arial", 12)).pack(pady=5)
        self.Email= Entry(self.root, width=40, font=("Arial", 11))
        self.Email.pack(pady=5)

        Button(self.root, text="Register", command=self.Data_Register, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

    def Data_Register(self):
        name=self.User_Name.get()
        passw=self.Password.get()
        email=self.Email.get()

        response= self.database.File_Register(name, email, passw)

        if response==True:
            messagebox.showinfo("Success", "You have Successfully Registered!!")
            self.Login()
        else:
            messagebox.showerror("Error", "Email already exist!!")

    def Check_Credentials(self):
        inp_mail=self.Input_Email.get()
        inp_pass=self.Input_Password.get()

        response=self.database.Check_Credentials(inp_mail, inp_pass)

        if response==True:
            messagebox.showinfo("Success", "Successfully Logged-in")
            self.Home()
        else:
            messagebox.showerror("Error", "Invalid Credentials!!")

    def Home(self):
        self.Clear()

        self.__Main_heading.pack(pady=20)

        Button(self.root, text="Grammar And Spelling Check", command=self.Grammar_And_Spelling, bg="#007ACC", fg="white", width=40, font=("Arial", 11)).pack(pady=10)
        Button(self.root, text="NER(Entity Extraction)", command=self.Ner, bg="#007ACC", fg="white", width=40, font=("Arial", 11)).pack(pady=10)
        Button(self.root, text="Sentiment Analyse", command=self.Sentiment, bg="#007ACC", fg="white", width=40, font=("Arial", 11)).pack(pady=10)
        Button(self.root, text="Detect Language", command=self.Language_Detect, bg="#007ACC", fg="white", width=40, font=("Arial", 11)).pack(pady=10)
        Button(self.root, text="Generate Code", command=self.PseudoCode_Generation, bg="#007ACC", fg="white", width=40, font=("Arial", 11)).pack(pady=10)

    def Grammar_And_Spelling(self):

        self.Clear()
        self.__Main_heading.pack(pady=20)

        Label(self.root, text="Grammar And Spelling Check", bg="#2DDEEB", font=("Arial", 13)).pack(pady=5)
        Label(self.root, text="Enter text to check:", bg="#2DDEEB", font=("Arial", 11)).pack(pady=5)
        grammar_para = Entry(self.root, width=60, font=("Arial", 11))
        grammar_para.pack(pady=5)

        def correct_text():
            parag = grammar_para.get()
            client = nlpcloud.Client("finetuned-llama-3-70b", self.__Cloud_Token, gpu=True)
            response = client.gs_correction(parag)
            corrected = response.get("correction", "No correction returned.")
            Label(self.root, text=f"Corrected Text:\n{corrected}", bg="#DFF6FF", fg="#000000", wraplength=600, justify="left", font=("Arial", 11)).pack(pady=10)

        Button(self.root, text="Go Back", command=self.Home, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

        Button(self.root, text="Correct", command=correct_text, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

    def Ner(self):

        self.Clear()
        self.__Main_heading.pack(pady=20)

        Label(self.root, text="Named Entity Recognition (NER)", bg="#2DDEEB", font=("Arial", 13)).pack(pady=5)
        Label(self.root, text="Enter paragraph:", bg="#2DDEEB", font=("Arial", 11)).pack(pady=5)
        para_entry = Entry(self.root, width=60, font=("Arial", 11))
        para_entry.pack(pady=5)
        Label(self.root, text="Enter entity type (e.g., languages, persons, etc.):", bg="#2DDEEB", font=("Arial", 11)).pack(pady=5)
        entity_entry = Entry(self.root, width=30, font=("Arial", 11))
        entity_entry.pack(pady=5)

        def extract_entities():
            para = para_entry.get()
            entity_type = entity_entry.get()
            client = nlpcloud.Client("finetuned-llama-3-70b", self.__Cloud_Token, gpu=True)
            response = client.entities(para, searched_entity=entity_type)
            entities = [item["text"] for item in response.get("entities", [])]
            if entities:
                result_text = f"Extracted {entity_type}:\n" + ", ".join(entities)
            else:
                result_text = f"No entities of type '{entity_type}' found."
            Label(self.root, text=result_text, bg="#DFF6FF", fg="#000", wraplength=600, justify="left", font=("Arial", 11)).pack(pady=10)

        Button(self.root, text="Go Back", command=self.Home, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

        Button(self.root, text="Extract Entities", command=extract_entities, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

    def Sentiment(self):

        self.Clear()
        self.__Main_heading.pack(pady=20)

        Label(self.root, text="Sentiment Analysis", bg="#2DDEEB", font=("Arial", 13)).pack(pady=5)
        sentiment_entry = Entry(self.root, width=60, font=("Arial", 11))
        sentiment_entry.pack(pady=5)

        def analyze():
            para = sentiment_entry.get()
            client = nlpcloud.Client("finetuned-llama-3-70b", self.__Cloud_Token, gpu=True)
            response = client.sentiment(para, target="NLP Cloud")
            if "scored_labels" in response:
                result = "Sentiment Scores:\n"
                for item in response["scored_labels"]:
                    result += f"{item['label']}: {item['score']}\n"
            else:
                result = "No sentiment detected."
            Label(self.root, text=result, bg="#DFF6FF", fg="#000000", font=("Arial", 11), wraplength=600, justify="left").pack(pady=10)

        Button(self.root, text="Go Back", command=self.Home, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

        Button(self.root, text="Analyze", command=analyze, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

    def Language_Detect(self):

        self.Clear()
        self.__Main_heading.pack(pady=20)

        Label(self.root, text="Language Detection", bg="#2DDEEB", font=("Arial", 13)).pack(pady=5)
        lang_entry = Entry(self.root, width=60, font=("Arial", 11))
        lang_entry.pack(pady=5)

        def detect():
            para = lang_entry.get()
            client = nlpcloud.Client("python-langdetect", self.__Cloud_Token, gpu=False)
            response = client.langdetection(para)
            if "languages" in response and response["languages"]:
                lang_code, confidence = list(response["languages"][0].items())[0]
                result = f"Detected Language: {lang_code.upper()}\nConfidence Score: {confidence:.2f}"
            else:
                result = "Could not detect the language."
            Label(self.root, text=result, bg="#DFF6FF", fg="#000000", font=("Arial", 11), wraplength=600, justify="left").pack(pady=10)

        Button(self.root, text="Go Back", command=self.Home, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

        Button(self.root, text="Detect", command=detect, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

    def PseudoCode_Generation(self):

        self.Clear()
        self.__Main_heading.pack(pady=20)

        Label(self.root, text="Code Generation", bg="#2DDEEB", font=("Arial", 13)).pack(pady=5)
        code_prompt = Entry(self.root, width=60, font=("Arial", 11))
        code_prompt.pack(pady=5)

        def generate():
            para = code_prompt.get()
            client = nlpcloud.Client("finetuned-llama-3-70b", self.__Cloud_Token, gpu=True)
            response = client.code_generation(para)
            code = response.get("generated_code", "No code generated.")
            text_box = Text(self.root, height=15, width=80, font=("Courier", 10), wrap="word", bg="#F5F5F5")
            text_box.insert(END, code)
            text_box.config(state="disabled")
            text_box.pack(pady=10)

        Button(self.root, text="Go Back", command=self.Home, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

        Button(self.root, text="Generate Code", command=generate, bg="#007ACC", fg="white", width=20, font=("Arial", 11)).pack(pady=10)

obj1= Nlp_Project()
