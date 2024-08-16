import logging
import os
from datetime import datetime
from PIL import ImageGrab

# Create 'log' directory if it doesn't exist
log_dir = 'log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


def setup_logger(name, log_file=None, level=logging.INFO, console=True):
    """Function to setup a logger"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler
    if log_file and not any(isinstance(handler, logging.FileHandler) for handler in logger.handlers):
        file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Console handler
    if console and not any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def capture_screenshot():
    screenshot = ImageGrab.grab()
    filename = os.path.join(
        log_dir, datetime.now().strftime("%Y%m%d_%H%M%S.png"))
    screenshot.save(filename)
    return filename


app_logger = setup_logger('app_logger', 'app.log')
