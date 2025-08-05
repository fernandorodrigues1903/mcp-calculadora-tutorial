# 🧮 Servidor MCP da Calculadora

Um servidor Model Context Protocol (MCP) simples que expõe operações de calculadora para assistentes de IA como o Gemini CLI.

## 📋 Descrição

Este projeto demonstra como criar um servidor MCP básico em Python que permite que assistentes de IA realizem operações matemáticas simples através do protocolo MCP. É ideal para iniciantes que querem aprender sobre MCP e integração de IA.

## ✨ Funcionalidades

- ➕ **Adição**: Soma dois números
- ➖ **Subtração**: Subtrai dois números  
- ➗ **Divisão**: Divide dois números (com proteção contra divisão por zero)
- ℹ️ **Informações**: Mostra detalhes sobre as operações disponíveis

# 🛠️ Tecnologias Utilizadas

- **Python 3.11+**: Linguagem de programação principal
- **MCP (Model Context Protocol)**: Protocolo para integração com IA
- **FastMCP**: Framework simplificado para servidores MCP
- **Docker**: Containerização para portabilidade
- **Gemini CLI**: Cliente para interação com o servidor MCP

## 📦 Pré-requisitos

- Python 3.11 ou superior
- Node.js 20+ (para Gemini CLI)
- Docker (opcional, para containerização)
- Git

## 🚀 Instalação e Uso

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mcp-calculadora-tutorial.git
cd mcp-calculadora-tutorial
