from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Você é um assistente especializado em segurança cibernética. Responda com base nas diretrizes do NIST."),
    HumanMessage("Quais são os principais controles do NIST para proteção de dados?")
]

modelo = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = modelo | parser

#resposta = modelo.invoke(mensagens)

#texto = parser.invoke(resposta)

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente especializado em segurança cibernética. Responda com base nas diretrizes do {framework}"),
    ("user", "Quais são os principais controles do {framework} para {tema}"),
])

#template_mensagem.invoke({"framework": "NIST", "tema":"Phishing"})

chain = template_mensagem | modelo | parser

#texto = chain.invoke({"framework": "NIST", "tema":"Phishing"})

#print(texto)
