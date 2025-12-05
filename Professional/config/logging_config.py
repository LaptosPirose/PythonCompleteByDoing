"""
Logging config
"""
import logging

def configure_logging(level: str = "INFO") -> None:
    """Configura logging profissional, com formatação consistente."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
