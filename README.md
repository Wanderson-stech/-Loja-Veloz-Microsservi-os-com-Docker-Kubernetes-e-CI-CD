# 🚀 Loja Veloz - Cloud DevOps & Microservices

> Projeto de modernização de arquitetura monolítica para microsserviços distribuídos, utilizando práticas de DevOps, Containerização e Orquestração.

---

## 📋 Sobre o Projeto
Este projeto foi desenvolvido como parte da avaliação de **Cloud DevOps & Orchestration**. O objetivo é simular um ambiente real de e-commerce ("Loja Veloz") que sofria com problemas de escalabilidade e *downtime*.

A solução proposta migra o sistema para uma arquitetura Cloud Native robusta, focada em:
* **Alta Disponibilidade:** Self-healing com Kubernetes.
* **Escalabilidade:** Autoscaling (HPA) baseado em uso de CPU.
* **Observabilidade:** Healthchecks e Logs estruturados.
* **Automação:** Pipeline de CI/CD para build e testes.
* **Infraestrutura como Código:** Provisionamento via Terraform.

---

## 🏗 Arquitetura da Solução

O sistema é composto pelos seguintes microsserviços:

1.  **API Gateway (Python/Flask):** Ponto único de entrada. Redireciona chamadas e balanceia a carga.
2.  **Pedido Service (Python/Flask):** Gerencia a criação e processamento de pedidos.
3.  **Database (PostgreSQL):** Banco de dados relacional para persistência.

### Tecnologias Utilizadas
* **Docker & Docker Compose:** Padronização do ambiente de desenvolvimento.
* **Kubernetes (K8s):** Orquestração em produção (Deployments, Services, ConfigMaps, Secrets, HPA).
* **Terraform:** Infraestrutura como Código (IaC) para provisionamento na AWS.
* **GitHub Actions:** Pipeline de CI/CD automatizado.
* **Python 3.9:** Linguagem base dos microsserviços.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Docker e Docker Compose instalados.
* (Opcional) Minikube ou Kind para rodar o Kubernetes localmente.
* (Opcional) Terraform instalado.

### 1. Ambiente Local (Docker Compose)
Para subir todo o ambiente de desenvolvimento (API, Pedidos e Banco) com um único comando:

```bash
# Na raiz do projeto
docker-compose up --build
Testando a Aplicação:

Status da API: Acesse http://localhost:8080/

Criar um Pedido:

Bash
curl -X POST http://localhost:8080/comprar
Resposta esperada: {"mensagem": "Pedido criado com sucesso!", ...}

2. Ambiente de Produção (Kubernetes)
Para realizar o deploy no cluster Kubernetes:

Bash
# Aplica os manifestos (ConfigMaps, Secrets, Deployments, Services, HPA)
kubectl apply -f k8s/
Verificando os Pods e o Autoscaling:

Bash
kubectl get pods
kubectl get hpa
3. Infraestrutura (Terraform)
Para visualizar o plano de execução da infraestrutura na nuvem (AWS EKS + RDS):

Bash
cd terraform
terraform init
terraform plan
🛡️ Segurança e Boas Práticas
Containers Seguros: As imagens Docker rodam com usuário não-root (appuser) para mitigar riscos de segurança.

Gerenciamento de Segredos: Senhas de banco de dados não estão "hardcoded" na aplicação; são injetadas via Kubernetes Secrets.

Healthchecks: Implementados probes de liveness e readiness para garantir que o tráfego só seja enviado para containers saudáveis.

🔄 Pipeline CI/CD
O arquivo .github/workflows/main.yml define a esteira de automação que:

Faz o checkout do código.

Instala dependências Python.

Executa testes automatizados.

Constrói e publica as imagens Docker (Build & Push).

Autor: Francisco Wanderson Silva Miranda
Disciplina: Cloud DevOps & Orchestration
