"""
Ponto de entrada principal da aplicação.

Este módulo inicializa:
- Configurações (env, .env, argumentos CLI)
- Logging estruturado
- Injeção de dependências
- Execução segura com tratamento de exceções
"""

from __future__ import annotations
import sys
import logging

from config.logging_config import configure_logging


def main() -> int:
    """Função main profissional — contém apenas orquestração, não lógica."""
    try:
        configure_logging()
        logging.info("Inicializando aplicação...")
        return 0

    except (ValueError, OSError) as e:
        logging.exception("Erro crítico na execução da aplicação: %s", e)
        return 1

    except KeyboardInterrupt:
        logging.info("Execução interrompida pelo usuário.")
        return 2


if __name__ == "__main__":
    sys.exit(main())
