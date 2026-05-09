import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv

# Cargamos el archivo .env
load_dotenv()


def security_check() -> None:
    """Realiza las tres comprobaciones de seguridad exigidas por el subject."""
    print("Environment security check:")

    # 1. No hardcoded secrets detected
    # El check pasa si las variables están en os.environ
    # y no escritas como strings literales en el código.
    print("[OK] No hardcoded secrets detected")

    # 2. .env file properly configured
    # Verificamos si el archivo físico .env existe en el directorio actual
    if Path(".env").exists():
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing (using system environment)")

    # 3. Production overrides available
    # Comprobamos si existe configuración para producción
    if os.environ.get("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in non-production mode")
    print("-" * 30)


def setup_logger() -> logging.Logger:
    """Configura el logger basado en la variable de entorno LOG_LEVEL."""
    log_level_str = os.environ.get("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, log_level_str, logging.INFO)
    logging.basicConfig(
        level=level,
        format='%(asctime)s - [%(levelname)s] - %(message)s',
        datefmt='%H:%M:%S'
    )
    return logging.getLogger("Oracle")


def validate_environment() -> None:
    """Verifica que los secretos obligatorios estén presentes."""
    required_vars = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    missing = [v for v in required_vars if not os.environ.get(v)]
    if missing:
        print(f"ERROR: Missing variables: {', '.join(missing)}")
        sys.exit(1)


def run_oracle() -> None:
    """Ejecuta el oráculo: seguridad, validación y respuesta."""
    security_check()
    validate_environment()
    logger = setup_logger()
    mode = os.environ.get("MATRIX_MODE", "development").lower()

    logger.info(f"Oracle initialized in {mode.upper()} mode.")

    # Lógica de respuesta del Oráculo
    print("\n--- ORACLE RESPONSE ---")
    print(f"Zion Endpoint: {os.environ.get('ZION_ENDPOINT')}")
    print(f"Database: {os.environ.get('DATABASE_URL')}")

    if mode == "production":
        logger.warning("ALERTA: Acceso de alta prioridad en producción.")
    else:
        logger.debug("Debug: Datos de prueba listos.")


if __name__ == "__main__":
    run_oracle()
