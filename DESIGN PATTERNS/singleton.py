# The Singleton Design Pattern is a creational design pattern 
# That restricts the instantiation of a class to a single instance. 
# This pattern is often used when a single instance of a class is needed to coordinate actions across the system.

import threading
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

class Singleton:
    """A thread-safe implementation of the Singleton design pattern."""
    __instance = None
    _lock = threading.Lock()  # Use a single underscore for internal use

    def __new__(cls):
        """Create a new instance only if it doesn't exist yet."""
        if cls.__instance is None:
            with cls._lock:
                if cls.__instance is None:  # Double-checked locking
                    cls.__instance = super().__new__(cls)
        return cls.__instance


def access_singleton():
    """Access the singleton instance and print its ID."""
    instance = Singleton()
    print(f"Singleton Instance ID: {id(instance)}")


def main():
    """Main function to demonstrate the Singleton pattern with multithreading."""
    futures = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit multiple tasks to access the singleton
        for _ in range(10):
            futures.append(executor.submit(access_singleton))

    # Wait for all threads to complete
    wait(futures, return_when=ALL_COMPLETED)
    print("All threads have completed.")


if __name__ == "__main__":
    main()
