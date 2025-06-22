import ollama

client = ollama.Client()

response = client.generate(model="llama3.2:1b", prompt="Crea una funcion en python para poder realizar un saludo")

print("Codigo generado")
print(response['response'])