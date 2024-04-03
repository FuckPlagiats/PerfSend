import csv
import requests
import time 
import os

def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

def demander_ip_port():
    ip_port = input("Enter IP:port: ")
    return ip_port

def envoyer_sms_depuis_fichier_texte(username, password, ip_port):
    fichier_numeros = input("Enter name of txt file: ")
    cls()
    message = input("Enter message text : ")
    cls()
    try:
        with open(fichier_numeros, 'r') as f:
            for ligne in f:
                numero = ligne.strip()
                if not numero:
                    continue
                url = f"http://{ip_port}/SendSMS?username={username}&password={password}&phone={numero}&message={message}"
                response = requests.get(url)
                time.sleep(1)
                print(f"Sms sent to {numero} with message : {message}")

    except FileNotFoundError:
        print("File not found.")

def envoyer_sms_depuis_fichier_csv(username, password, ip_port):
    fichier_csv = input("Enter name of csv file ")
    cls()
    colonne_numero = input("Enter the name of the column that contains the numbers ")
    cls()
    message = input("Enter message (use $variable_name to include variable):")
    cls()

    with open(fichier_csv, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            numero = row[colonne_numero]
            message_final = message
            for key, value in row.items():
                message_final = message_final.replace(f"${key.lower()}", value)
            
            url = f"http://{ip_port}/SendSMS?username={username}&password={password}&phone={numero}&message={message_final}"
            response = requests.get(url)
            time.sleep(1)
            print(f"Sms sent to {numero} with message : {message_final}")

cls()

ip_port = demander_ip_port()
username = input("Enter username (FROM APPLICATION): ")
password = input("Enter password (FROM APPLICATION): ")
cls()

print("Select the option to send SMS:")
print("1. from .txt (only phone)")
print("2. from CSV with variables in the message")

choix = input("(1 or 2): ")
cls()

if choix == '1':
    cls()
    envoyer_sms_depuis_fichier_texte(username, password, ip_port)
elif choix == '2':
    cls()
    envoyer_sms_depuis_fichier_csv(username, password, ip_port)
else:
    print("Invalid option.")
