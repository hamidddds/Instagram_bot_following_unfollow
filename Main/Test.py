from Logger import app_logger
import Logger


def main():

    # Example log messages
    app_logger.info('This is an info message')
    app_logger.warning('This is a warning message')
    app_logger.error('This is an error message')

    # Capture a screenshot and log its path
    screenshot_path = Logger.capture_screenshot()
    app_logger.info(f'Screenshot captured: {screenshot_path}')


if __name__ == "__main__":
    main()
