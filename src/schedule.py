import requests
import json


class Schedule:
    node = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Sunset", "Maghrib", "Isha", "SepertigaMalam", "TengahMalam",
            "DuapertigaMalam", "method"]

    def refresh_schedule(self):
        response = requests.get("https://time.siswadi.com/pray/Yogyakarta").text
        parsed = json.loads(response)
        data = parsed["data"]

        file = open("res/schedule.txt", "w+")
        # file.write(f"{data}")
        for i in self.node:
            file.write(f"{data[i]}\n")
        file.close()

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

    @staticmethod
    def fajr():
        with open("res/schedule.txt", "r") as fp:
            for i, line in enumerate(fp):
                if i is 0:
                    return line

