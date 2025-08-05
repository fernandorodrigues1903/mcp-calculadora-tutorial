# Dockerfile
# Este arquivo define como construir o container Docker para nosso servidor MCP

# Usamos uma imagem base do Python 3.11 (mesma versão que você tem)
# A imagem "slim" é menor e mais eficiente
FROM python:3.11-slim

# Definimos informações sobre o container
LABEL maintainer="Fernando Rodrigues <fernandoantunesfju@gmail.com>"
LABEL description="Servidor MCP da Calculadora - Tutorial Iniciante"
LABEL version="1.0"

# Criamos um diretório de trabalho dentro do container
WORKDIR /app

# Copiamos o arquivo de dependências primeiro
# Isso permite que o Docker use cache se as dependências não mudaram
COPY requirements.txt .

# Instalamos as dependências Python
# --no-cache-dir evita armazenar cache desnecessário
# --upgrade garante que temos as versões mais recentes
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamos nossos arquivos Python para o container
COPY calculadora.py .
COPY servidor_mcp.py .

# Criamos um usuário não-root para segurança
# É uma boa prática não executar aplicações como root
RUN useradd --create-home --shell /bin/bash mcpuser && \
    chown -R mcpuser:mcpuser /app

# Mudamos para o usuário não-root
USER mcpuser

# Definimos a porta que o container irá expor (se necessário)
# Para MCP stdio, isso é mais informativo que funcional
EXPOSE 8000

# Definimos variáveis de ambiente
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Comando padrão para executar quando o container iniciar
# Usamos o modo de teste por padrão para verificar se tudo está funcionando
CMD ["python", "servidor_mcp.py", "test"]

# Para executar o servidor MCP real, use:
# docker run --rm -it nome_da_imagem python servidor_mcp.py