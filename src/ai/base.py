from abc import ABC, abstractmethod

class AIPlatform(ABC):

    # abstract away ai implementation with an interface
    @abstractmethod
    def chat(self, prompt: str) -> str:
        """sends a prompt to the ai agent and returns response text."""
        pass