"""
Ponto de entrada principal da aplicação.

Este módulo inicializa:
- Configurações (env, .env, argumentos CLI)
- Logging estruturado
- Injeção de dependências
- Execução segura com tratamento de exceções
"""

from __future__ import annotations
import argparse
import logging
import sys
from pathlib import Path


def configure_logging(level: str = "INFO") -> None:
    """Configura logging profissional, com formatação consistente."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def parse_cli_arguments() -> argparse.Namespace:
    """Parser CLI padrão profissional."""
    parser = argparse.ArgumentParser(
        description="Aplicação ultra profissional.")
    parser.add_argument(
        "--env", default="dev",
        choices=["dev", "staging", "prod"],
        help="Define o ambiente da aplicação."
    )
    parser.add_argument(
        "--config", type=Path,
        help="Caminho opcional para arquivo de configuração personalizado."
    )
    return parser.parse_args()


def main() -> int:
    """Função main profissional — contém apenas orquestração, não lógica."""
    try:
        configure_logging()
        args = parse_cli_arguments()
        print(f'Application args are-> {args}!')
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
