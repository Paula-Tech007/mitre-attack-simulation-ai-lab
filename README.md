# 🛡️ AI SOC — Incident Response Lab
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![n8n](https://img.shields.io/badge/n8n-Automation-orange)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![License](https://img.shields.io/badge/License-Educational-green)
Laboratório prático de Segurança Cibernética que simula um ambiente moderno de SOC (Security Operations Center) utilizando Inteligência Artificial, automação e análise baseada no framework MITRE ATT&CK.

Este projeto demonstra como um sistema real pode detectar, analisar e responder automaticamente a incidentes de segurança — conceito fundamental em plataformas SOAR modernas.

---

## 🎯 Objetivo

Construir um pipeline automatizado de resposta a incidentes capaz de:

* Simular ataques cibernéticos realistas
* Classificar eventos de segurança
* Analisar riscos utilizando IA
* Gerar recomendações de mitigação
* Orquestrar respostas automatizadas
* Demonstrar conceitos de SOC e SOAR

---

## 🧠 Arquitetura do Sistema

O laboratório é composto por três camadas principais:

### ⚡ API de Simulação e Análise (Flask)

Responsável por:

* Simular ataques baseados no MITRE ATT&CK
* Gerar eventos de segurança estruturados
* Enviar dados para análise por IA
* Retornar relatórios estilo analista SOC

---

### 🔄 Motor de Automação (n8n)

Pipeline automatizado responsável por:

* Receber eventos via Webhook
* Processar dados do incidente
* Integrar com a API de análise
* Gerar respostas automatizadas

---

### 🤖 Inteligência Artificial (Gemini)

Utilizada para:

* Avaliação de risco
* Impacto no negócio
* Recomendações de mitigação
* Sugestões de melhoria de detecção

---

## 🧩 Fluxo do Sistema

1. Um ataque é simulado via API
2. Um evento estruturado é gerado
3. O evento é enviado ao workflow do n8n
4. A IA analisa o incidente
5. O sistema retorna recomendações de resposta

---

## 🟢 Status da API

Endpoint raiz utilizado como verificação de funcionamento (health check):

![API Status](images/api-status.png)

Exemplo de resposta:

```json
{
  "project": "Cyber Attack Simulation Lab",
  "status": "running",
  "version": "2.0 SOC Edition"
}
```

---

## 🧪 Demonstração do Workflow

### 🧠 Pipeline Automatizado (n8n)

![Workflow](images/workflow.png)

---

### ⚡ Teste da API — Simulação de Ataque

![API Test](images/api-test.png)

---

## 🧨 Técnicas MITRE ATT&CK Simuladas

| Ataque      | Técnica | Descrição                 | Severidade |
| ----------- | ------- | ------------------------- | ---------- |
| Phishing    | T1566   | Phishing                  | High       |
| Ransomware  | T1486   | Data Encrypted for Impact | Critical   |
| Brute Force | T1110   | Brute Force               | Medium     |

---

## 🛠️ Tecnologias Utilizadas

* Python
* Flask
* n8n (Automação / SOAR)
* Google Gemini API
* Docker (opcional)
* Thunder Client / Postman
* JSON
* MITRE ATT&CK Framework

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/ai-soc-lab.git
cd ai-soc-lab
```

---

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env`:

```
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

⚠️ Nunca publique sua chave no GitHub.

Recomenda-se incluir um arquivo `.env.example` no repositório.

---

## ▶️ Execução

Inicie a API:

```bash
python app.py
```

Servidor disponível em:

```
http://127.0.0.1:5000
```

---

## 📡 Endpoints

### 🧨 Simular ataque

**POST** `/simulate`

Exemplo de body:

```json
{
  "attack_type": "phishing"
}
```

---

### 🤖 Analisar incidente com IA

**POST** `/analyze`

Exemplo de body:

```json
{
  "attack_type": "phishing",
  "mitre_technique": "T1566",
  "severity": "High",
  "country": "Brazil"
}
```

---

## 🔐 Segurança

* Chaves de API armazenadas em variáveis de ambiente
* Código preparado para deploy seguro
* Separação entre simulação e análise
* Estrutura compatível com ambientes cloud

---

## 🚀 Possíveis Expansões

* Integração com SIEM (Splunk, ELK)
* Integração com plataformas SOAR
* Alertas via Slack ou Email
* Dashboard de incidentes
* Deploy em Cloud (AWS / Azure / GCP)
* Monitoramento contínuo

---

## 🎓 Objetivo Educacional

Este laboratório foi desenvolvido para:

* Estudo prático de SOC
* Demonstração de habilidades em cibersegurança
* Portfólio técnico
* Testes de automação e IA aplicada à segurança

---

## 👩‍💻 Autora

Paula Sabino
Foco em Automação, Cibersegurança e Inteligência Artificial aplicada.

---

## 📄 Licença

Uso educacional e de pesquisa.
