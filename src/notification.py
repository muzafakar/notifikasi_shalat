import os
class Notification:
    @staticmethod
    def send_notification(message, icon, content=None):
        if content is None:
            os.system(f"notify-send {message} -i {icon}")
        else:
            os.system(f"notify-send {message} -i {icon} {content}")

