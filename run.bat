@echo off
echo Iniciando servidor MCP da Calculadora no Docker...
echo.
echo Para parar o servidor, pressione Ctrl+C
echo.
docker run --rm -it mcp-calculadora:1.0 python servidor_mcp.py