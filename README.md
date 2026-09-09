# Payment-System

![GitHub stars](https://img.shields.io/github/stars/samyr-melo/Payment-System?style=for-the-badge&logo=github) ![GitHub forks](https://img.shields.io/github/forks/samyr-melo/Payment-System?style=for-the-badge&logo=github) ![GitHub issues](https://img.shields.io/github/issues/samyr-melo/Payment-System?style=for-the-badge&logo=github) ![Last commit](https://img.shields.io/github/last-commit/samyr-melo/Payment-System?style=for-the-badge&logo=github)

## 📑 Table of Contents

- [Description](#description)
- [Context and Problem](#Context-and-Problem)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [Contributing](#contributing)

## 📝 Description

Serviço de pagamento

Laboratório prático construído em FastAPI para demonstrar o impacto arquitetural, consumo de banda e sobrecarga de processamento entre dois modelos de comunicação assíncrona entre microsserviços: Polling Ativo via API vs. Notificação Reativa via Webhook.

## Context and Problem

Em fluxos de solicitação de serviços de longa duração (ex.: processamento de pagamentos, provisionamento de infraestrutura ou exportação de relatórios), o sistema solicitante precisa saber quando a tarefa foi concluída.

Abordagem Tradicional (Polling): O cliente bombardeia a API repetidamente perguntando se a tarefa terminou (GET /status).

Abordagem Reativa (Webhook): O cliente registra o pedido, libera recursos e o provedor faz uma chamada POST única no momento exato da mutação de estado.

Este repositório contém dois servidores simulando o fluxo de solicitação de serviço/pagamento para evidenciar a economia de I/O e tráfego.

## ⚡ Quick Start

```bash

# 1. Clone the repository
git clone https://github.com/samyr-melo/Payment-System.git

# See the Development Setup section below
```

## 📁 Project Structure

```
.
├── metodo_api
│   ├── my_system.py
│   └── stripe_server.py
└── metodo_webhook
    ├── my_system_webhook.py
    └── stripe_server_webhook.py
```

## 👥 Contributors

Thanks to everyone who has contributed to this project:

<p align="left">
<a href="https://github.com/samyr-melo" title="samyr-melo"><img src="https://avatars.githubusercontent.com/u/153466790?v=4&s=64" width="64" height="64" alt="samyr-melo" style="border-radius:50%" /></a>
</p>

[See the full list of contributors →](https://github.com/samyr-melo/Payment-System/graphs/contributors)

## 👥 Contributing

Contributions are welcome! Here's the standard flow:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/samyr-melo/Payment-System.git`
3. **Branch**: `git checkout -b feature/your-feature`
4. **Commit**: `git commit -m 'feat: add some feature'`
5. **Push**: `git push origin feature/your-feature`
6. **Open** a pull request

Please follow the existing code style and include tests for new behavior where applicable.

---

<div align="center">

[![Made with ReadmeBuddy](https://img.shields.io/badge/Made%20with-ReadmeBuddy-8B5CFF?style=for-the-badge&logo=markdown&logoColor=white)](https://readmebuddy.com)

<sub>Generate beautiful READMEs in seconds → <a href="https://readmebuddy.com">readmebuddy.com</a></sub>

</div>
