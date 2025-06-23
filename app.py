import ollama

client = ollama.Client()

#se le agrega pregurnta de usuario
pregunta_usuario = input("Pregunta sobre que camino de aprendizaje quieres hacer \n")

response = client.generate(model="llama3.2:1b", prompt=pregunta_usuario)

print("Codigo generado")
print(response['response'])