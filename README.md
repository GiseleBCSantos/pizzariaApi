# 🍕 Pizzaria API

Esta é a API para gerenciamento de pedidos de uma pizzaria desenvolvida para a matéria Análise e Projeto de Sistemas.

## 🛠️ Tecnologias Utilizadas

- Django Rest Framework (DRF)
- Postgresql
- Railway para hospedagem

## 📃 Endpoints

### 👨‍💼 Clientes

- `GET /cliente/` - Lista todos os clientes
- `POST /cliente/` - Cria um novo cliente
- `GET /cliente/{id}/` - Retorna um cliente pelo ID
- `PUT /cliente/{id}/` - Atualiza um cliente pelo ID
- `DELETE /cliente/{id}/` - Remove um cliente pelo ID

### 🍕 Pizzas

- `GET /pizza/` - Lista todas as pizzas
- `POST /pizza/` - Cria uma nova pizza
- `GET /pizza/{id}/` - Retorna uma pizza pelo ID
- `PUT /pizza/{id}/` - Atualiza uma pizza pelo ID
- `DELETE /pizza/{id}/` - Remove uma pizza pelo ID

### 📏 Tamanhos

- `GET /tamanho/` - Lista todos os tamanhos
- `POST /tamanho/` - Cria um novo tamanho
- `GET /tamanho/{id}/` - Retorna um tamanho pelo ID
- `PUT /tamanho/{id}/` - Atualiza um tamanho pelo ID
- `DELETE /tamanho/{id}/` - Remove um tamanho pelo ID

### 📦 Pedidos

- `GET /pedido/` - Lista todos os pedidos
- `POST /pedido/` - Cria um novo pedido
- `GET /pedido/{id}/` - Retorna um pedido pelo ID
- `PUT /pedido/{id}/` - Atualiza um pedido pelo ID
- `DELETE /pedido/{id}/` - Remove um pedido pelo ID

### 🛒 Itens do Pedido

- `GET /itempedido/` - Lista todos os itens dos pedidos
- `POST /itempedido/` - Adiciona um item a um pedido
- `GET /itempedido/{id}/` - Retorna um item do pedido pelo ID
- `PUT /itempedido/{id}/` - Atualiza um item do pedido pelo ID
- `DELETE /itempedido/{id}/` - Remove um item do pedido pelo ID

## 📚 Models

### Cliente

```json
{
  "id": 1,
  "nome": "João Silva",
  "endereco": "Rua das Pizzas, 123",
  "telefone": "(11) 91234-5678",
  "bairro": "Centro"
}
```

### Pizza

```json
{
  "id": 1,
  "sabor": "Calabresa",
  "precoBase": 30.0
}
```

### Tamanho

```json
{
  "id": 1,
  "nome": "Grande",
  "modificador": 1.5
}
```

### Pedido

```json
{
  "id": 1,
  "cliente_nome": "João Silva",
  "data_pedido": "01/02/2025 15:30",
  "status": "aberto",
  "valor_total": 45.0,
  "itens_pedidos": [
    {
      "quantidade": 1,
      "pizza_nome": "Calabresa",
      "tamanho_nome": "Grande",
      "preco_total": 45.0
    }
  ]
}
```

## 👤 Desenvolvedora

- **Gisele Santos**

## 👉 Link da API na Web

https://pizzariaapi-production.up.railway.app/cliente/

- Em {cliente} substituir pela rota desejada.
