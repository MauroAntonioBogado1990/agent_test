from types import AsyncGeneratorType
from langchain_ollama import ChatOllama
from langchain_community.tools import YoutubeSearchTool, DuckDuckGoSearchResults

from langchain_core.messages import SystemMessage

from langgraph.prebuilt import create_react_agent

pregunta_usuario = input("Pregunta sobre que camino de aprendizaje quieres hacer \n")

system_promt = SystemMessage('''
Eres un asitente llamado Asi que sirve para que las personas que quieran aprender
alguna ruta de aprendizaje de cualquier tema ellos lo puedan crear.

Te debes presentar siempre al usuario.

Tu tarea es explicar los temas, que el usuario te solicita complementadolos con
enlaces relacionados a cursos gratuitos, pueden ser videos o textos.

Debes ser detallado en la distribución de temas, de como el usuario debe seguir la ruta.

1.Titulo del aprendizaje
2.Desripción de la ruta de aprendizaje
3.Explicación de los temas de aprendizaje, detallando los temas y distribuyendolós en semanas y meses.
4.Enlaces de los cursos o artículos(Tienen que ser enlaces reales sino no lo coloques)
5.Proporciona ejercicios que se puedan poner en práctica
6.Siempre finaliza sugiriendo que proyectos se pueden realizar para poner en practica los conocimientos adquiridos.

Usa las herramientas disponibles para hacer la busqueda. No inventes nada.

Debes despedirte del usuario

''')

youtube = YoutubeSearchTool(description="Una herramienta de busqueda de videos de Youtube. Entrega enlaces de videos en Español sobre el tema solicitado por el usuario y actualizados. Ten en cuenta traer cursos, rutas de aprendizaje relacionados y proyectos")

search = DuckDuckGoSearchResults(description="Una herrramienta para la búsqueda de información de apoyo usando el buscador duckduckgo, agrega siempre 5 cursos, proyectos o ejercicios relacionados con la solicitud de la ruta de aprendizaje que desea el usuario. Para complementar el resultado. Entrega busquedas en Español. No olvides de buscar siempre información actualizada. Valida que los enlaces esten funcionando ")

tools = [youtube, search]

llm = ChatOllama(model="llama3.1").bind_tools(tools)

agente = create_react_agent(llm,tools,state_modifier=system_promt, debug=True)

resultado = agente.invoke({"messages":pregunta_usuario})

print(resultado["messages"][-1].content)