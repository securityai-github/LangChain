from langserve import RemoteRunnable

chain_remota = RemoteRunnable('http://localhost:8000/cyber')
texto = chain_remota.invoke({"framework": "NIST", "tema":"Ramsonware"})
print(texto)