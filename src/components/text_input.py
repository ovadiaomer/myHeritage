from src.components.locator import Locator

class TextInput(Locator):
    def fill(self, text: str):
        self.get_locator().fill(text)
