# 🛡️ AI-Powered SOC Incident Response Lab — MITRE ATT&CK Simulation
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![n8n](https://img.shields.io/badge/n8n-Automation-orange)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![License](https://img.shields.io/badge/License-Educational-green)

Laboratório prático de Segurança Cibernética que simula um ambiente moderno de SOC (Security Operations Center) utilizando Inteligência Artificial, automação e análise baseada no framework MITRE ATT&CK.

Este projeto demonstra como um sistema real pode detectar, analisar e responder automaticamente a incidentes de segurança — conceito fundamental em plataformas SOAR modernas.

🎯 Objetivo

Construir um pipeline automatizado de resposta a incidentes capaz de:

Simular ataques cibernéticos realistas

Classificar eventos de segurança

Analisar riscos utilizando IA

Gerar recomendações de mitigação

Orquestrar respostas automatizadas

Demonstrar conceitos de SOC e SOAR

🧠 Arquitetura do Sistema

O laboratório é composto por três camadas principais:

⚡ API de Simulação e Análise (Flask)

Responsável por:

Simular ataques baseados no MITRE ATT&CK

Gerar eventos de segurança estruturados

Enviar dados para análise por IA

Retornar relatórios estilo analista SOC

🔄 Motor de Automação (n8n)

Pipeline automatizado responsável por:

Receber eventos via Webhook

Processar dados do incidente

Integrar com a API de análise

Gerar respostas automatizadas

🤖 Inteligência Artificial (Gemini)

Utilizada para:

Avaliação de risco

Impacto no negócio

Recomendações de mitigação

Sugestões de melhoria de detecção

🧩 Fluxo do Sistema

Um ataque é simulado via API

Um evento estruturado é gerado

O evento é enviado ao workflow do n8n

A IA analisa o incidente

O sistema retorna recomendações de resposta

🟢 Status da API

Endpoint raiz utilizado como verificação de funcionamento (health check):

Exemplo de resposta:

{
  "project": "Cyber Attack Simulation Lab",
  "status": "running",
  "version": "2.0 SOC Edition"
}
🧪 Demonstração do Workflow
🧠 Pipeline Automatizado (n8n)

⚡ Teste da API — Simulação de Ataque

🧨 Técnicas MITRE ATT&CK Simuladas
Ataque	Técnica	Descrição	Severidade
Phishing	T1566	Phishing	High
Ransomware	T1486	Data Encrypted for Impact	Critical
Brute Force	T1110	Brute Force	Medium
🛠️ Tecnologias Utilizadas

Python

Flask

n8n (Automação / SOAR)

Google Gemini API

Docker (opcional)

Thunder Client / Postman

JSON

MITRE ATT&CK Framework

💼 Casos de Uso

Ambientes de treinamento para SOC

Simulações de resposta a incidentes

Demonstração de conceitos de SOAR

Análise de segurança assistida por IA

Laboratórios educacionais de cibersegurança

🧩 Habilidades Demonstradas

Automação de Resposta a Incidentes

Design de Workflows de SOC

Desenvolvimento de APIs

Simulação de Eventos de Segurança

Integração com Inteligência Artificial

Análise de Ameaças

Arquitetura pronta para Cloud

🎯 Framework MITRE ATT&CK

Este projeto é baseado no framework MITRE ATT&CK, uma base de conhecimento global de táticas e técnicas utilizadas por adversários reais, construída a partir de observações do mundo real.

Framework mantido pela MITRE Corporation — referência internacional em pesquisa e desenvolvimento em segurança cibernética.

⚙️ Instalação
1️⃣ Clonar o repositório
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

Recomenda-se incluir um arquivo .env.example no repositório.

▶️ Execução

Inicie a API:

python app.py

Servidor disponível em:

http://127.0.0.1:5000
📡 Endpoints
🧨 Simular ataque

POST /simulate

Exemplo de body:

{
  "attack_type": "phishing"
}
🤖 Analisar incidente com IA

POST /analyze

Exemplo de body:

{
  "attack_type": "phishing",
  "mitre_technique": "T1566",
  "severity": "High",
  "country": "Brazil"
}
🔐 Segurança

Chaves de API armazenadas em variáveis de ambiente

Código preparado para deploy seguro

Separação entre simulação e análise

Estrutura compatível com ambientes cloud

🚀 Possíveis Expansões

Integração com SIEM (Splunk, ELK)

Integração com plataformas SOAR

Alertas via Slack ou Email

Dashboard de incidentes

Deploy em Cloud (AWS / Azure / GCP)

Monitoramento contínuo

🎓 Objetivo Educacional

Este laboratório foi desenvolvido para:

Estudo prático de SOC

Demonstração de habilidades em cibersegurança

Portfólio técnico

Testes de automação e IA aplicada à segurança

👩‍💻 Autora

Paula Sabino
Cibersegurança • Automação • Engenharia de IA

GitHub: https://github.com/Paula-Tech007

📄 Licença

Uso educacional e de pesquisa.
