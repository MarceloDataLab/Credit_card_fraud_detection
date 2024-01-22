import tkinter as tk
from tkinter import filedialog
import pandas as pd
import pickle

# Função para carregar o modelo
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

# Função que será chamada quando o botão "Predict" for clicado
def predict():
    try:
        # Carrega os dados
        data = pd.read_csv(filepath)
        # Faz a previsão
        prediction = model.predict(data)
        # Verifica o resultado da previsão e define a mensagem
        if prediction[0] == 1:
            result.set("This transaction is fraudulent")
        else:
            result.set("This transaction is Not fraudulent")
    except Exception as e:
        result.set(f"An error occurred: {e}")

# Função para abrir o seletor de arquivos
def browse_file():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        file_label.config(text="File loaded: " + filepath.split('/')[-1])

# Carrega o modelo
model_path = 'Credit_card_fraud_detection/credit_card_fraud_detection.pkl'
model = load_model(model_path)

# Cria a janela principal
root = tk.Tk()
root.title("Credit Card Fraud Detection")
root.geometry("470x240")
root.configure(background='#333333')

# Define a variável para armazenar o resultado
result = tk.StringVar()

# Cria os widgets
title_label = tk.Label(root, text="Credit Card Fraud Detection", bg='#333333', fg='white')
title_label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file, bg='#555555', fg='white')
browse_button.pack()

file_label = tk.Label(root, text="No file loaded", bg='#333333', fg='white')
file_label.pack(pady=10)

predict_button = tk.Button(root, text="Predict", command=predict, bg='#555555', fg='white')
predict_button.pack(pady=10)

result_label = tk.Label(root, textvariable=result, bg='#333333', fg='red')
result_label.pack(pady=10)

# Executa o loop principal
root.mainloop()
