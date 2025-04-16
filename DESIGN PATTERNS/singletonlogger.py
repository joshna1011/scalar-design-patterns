import threading
import logging

class SingletonLogger:
    """A thread-safe singleton logger class."""
    __instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls._lock:
                if cls.__instance is None:  # Double-checked locking
                    cls.__instance = super().__new__(cls)
                    cls.__instance._initialize_logger()
        return cls.__instance

    def _initialize_logger(self):
        """Initializes the logger settings."""
        self.logger = logging.getLogger("SingletonLogger")
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(ch)

    def log(self, message, level=logging.INFO):
        """Log a message with the specified level."""
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)


# Usage
if __name__ == "__main__":
    logger1 = SingletonLogger()
    logger2 = SingletonLogger()

    logger1.log("This is an info message.")
    logger2.log("This is a warning message.", level=logging.WARNING)

    # Verify that both variables refer to the same instance
    print(logger1 is logger2)  # Output: True
