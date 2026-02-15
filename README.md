# Loja Veloz - Microsserviços DevOps

Projeto desenvolvido para a disciplina de Cloud DevOps & Orchestration.

## 🏗 Arquitetura
Microsserviços Python/Flask conteinerizados:
- **API Gateway**
- **Pedido Service**
- **Database PostgreSQL**

## 🚀 Como Rodar (Local)
1. Instale Docker e Docker Compose
2. Execute:
   ```bash
   docker-compose up --build
   ```
3. Acesse:
   - Status: http://localhost:8080/
   - Criar Pedido: POST http://localhost:8080/comprar

## ☸️ Kubernetes
```bash
kubectl apply -f k8s/
kubectl get pods
```
