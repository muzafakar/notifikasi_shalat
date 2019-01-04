# File ini isinya cuma message

class CustomMessage:
    @staticmethod
    def salam():
        return "Assalamualaikum"

    @staticmethod
    def breakfast():
        return "Jangan lupa sarapan ya"

    @staticmethod
    def ask_shalat(self):
        return f"Kak, udah shalat {self} belum?"

    @staticmethod
    def ask_to_sleep(self):
        return f"Udah jam {self}, ayo istirahat dulu kak"
