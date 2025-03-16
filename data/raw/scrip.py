import os
import requests

# URL del dataset
url = "https://raw.githubusercontent.com/4GeeksAcademy/logistic-regression-project-tutorial/main/bank-marketing-campaign-data.csv"
file_path = os.path.join("data", "raw", "bank-marketing-campaign-data.csv")
os.makedirs(os.path.dirname(file_path), exist_ok=True)

response = requests.get(url)

if response.status_code == 200:
    content = response.text.replace(";", ",")
    with open(file_path, "w") as file:
        file.write(content)
    print(f"✅ Archivo modificado (comas) guardado en {file_path}")
else:
    print("❌ Error al descargar el archivo")