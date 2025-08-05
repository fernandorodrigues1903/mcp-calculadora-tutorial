@echo off
echo Construindo imagem Docker da Calculadora MCP...
docker build -t mcp-calculadora:1.0 .
echo.
echo Imagem construída com sucesso!
echo Para testar: docker run --rm mcp-calculadora:1.0
echo Para executar: docker run --rm -it mcp-calculadora:1.0 python servidor_mcp.py
pause