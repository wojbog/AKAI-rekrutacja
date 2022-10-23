import json


class Importer:

    def __init__(self):
        self.data = 0

    def read_tasks(self):
         with open("taski.json","r") as f:
            data = json.load(f)
            self.data = data

    def get_tasks(self):
        return self.data