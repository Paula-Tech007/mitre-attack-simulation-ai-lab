# 🛡️ AI-Powered SOC Incident Response Lab — MITRE ATT&CK Simulation
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![n8n](https://img.shields.io/badge/n8n-Automation-orange)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![License](https://img.shields.io/badge/License-Educational-green)

## 🧠 Arquitetura do Laboratório

Laboratório prático de Segurança Cibernética que simula um ambiente moderno de SOC (Security Operations Center) utilizando Inteligência Artificial, automação e análise baseada no framework MITRE ATT&CK.

O projeto demonstra como sistemas modernos podem detectar, analisar e responder automaticamente a incidentes — conceito fundamental em plataformas SOAR.

---

## 🎯 Objetivo

Construir um pipeline automatizado capaz de:

- Simular ataques cibernéticos realistas
- Classificar eventos de segurança
- Analisar riscos com IA
- Gerar recomendações de mitigação
- Orquestrar respostas automatizadas
- Demonstrar conceitos de SOC e SOAR

---

## 💼 Casos de Uso

- Ambientes de treinamento SOC
- Simulações de resposta a incidentes
- Demonstração de conceitos SOAR
- Análise de segurança assistida por IA
- Laboratórios educacionais de cibersegurança

---

## 🧩 Habilidades Demonstradas

- Automação de resposta a incidentes
- Design de workflows SOC
- Desenvolvimento de APIs
- Simulação de eventos de segurança
- Integração com IA generativa
- Análise de ameaças
- Arquitetura pronta para cloud

---

## 🧠 Arquitetura do Sistema

O laboratório é composto por três camadas principais:

### ⚡ API de Simulação e Análise (Flask)

- Simulação de ataques baseados no MITRE ATT&CK
- Geração de eventos estruturados
- Envio para análise por IA
- Retorno de relatórios estilo analista SOC

### 🔄 Motor de Automação (n8n)

- Recebimento de eventos via Webhook
- Processamento do incidente
- Integração com a API de análise
- Geração de respostas automatizadas

### 🤖 Inteligência Artificial (Gemini)

- Avaliação de risco
- Impacto no negócio
- Recomendações de mitigação
- Sugestões de melhoria de detecção

---

## 🧩 Fluxo do Sistema

1. Um ataque é simulado via API  
2. Um evento estruturado é gerado  
3. O evento é enviado ao workflow do n8n  
4. A IA analisa o incidente  
5. O sistema retorna recomendações  

---

## 🟢 Status da API

Endpoint raiz usado como verificação de funcionamento (health check):

![API Status](images/api-status.png)

---

## 🧪 Demonstração

### 🧠 Workflow Automatizado (n8n)

![Workflow n8n](docs/fluxo-n8n.png)

---

### ⚡ Teste da API — Simulação de Ataque

![Teste da API](docs/api-test-thunder.png)

---

### 🟢 Status da API (Servidor Rodando)

![API Status](docs/api-status.png)
---

## 🧨 Técnicas MITRE ATT&CK Simuladas

| Ataque      | Técnica | Descrição                 | Severidade |
|------------|----------|---------------------------|------------|
| Phishing   | T1566    | Phishing                  | High       |
| Ransomware | T1486    | Data Encrypted for Impact | Critical   |
| Brute Force| T1110    | Brute Force               | Medium     |

Framework mantido pela MITRE Corporation.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Flask
- n8n (Automação / SOAR)
- Google Gemini API
- Docker (opcional)
- Thunder Client / Postman
- JSON
- MITRE ATT&CK

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Paula-Tech007/mitre-attack-simulation-ai-lab.git
cd mitre-attack-simulation-ai-lab
2️⃣ Criar ambiente virtual
python -m venv venv

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Configurar variáveis de ambiente

Crie um arquivo .env:

GEMINI_API_KEY=SUA_CHAVE_AQUI

⚠️ Nunca publique sua chave no GitHub.

▶️ Execução
python app.py

Servidor disponível em:

http://127.0.0.1:5000
📡 Endpoints
🧨 Simular ataque

POST /simulate

{
  "attack_type": "phishing"
}
🤖 Analisar incidente com IA

POST /analyze

{
  "attack_type": "phishing",
  "mitre_technique": "T1566",
  "severity": "High",
  "country": "Brazil"
}
🔐 Segurança

Chaves armazenadas em variáveis de ambiente

Estrutura pronta para deploy seguro

Separação entre simulação e análise

Compatível com ambientes cloud

🚀 Possíveis Expansões

Integração com SIEM (Splunk, ELK)

Integração com plataformas SOAR

Alertas via Slack ou Email

Dashboard de incidentes

Deploy em AWS / Azure / GCP

Monitoramento contínuo

🎓 Objetivo Educacional

Projeto desenvolvido para:

Estudo prático de SOC

Demonstração de habilidades em cibersegurança

Portfólio técnico

Testes de automação e IA aplicada à segurança

👩‍💻 Autora

Paula Sabino
Cybersecurity • Automation • AI Engineering

GitHub: https://github.com/Paula-Tech007

📄 Licença

Uso educacional e de pesquisa.
