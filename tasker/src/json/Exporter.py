import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        with open("taski.json","w") as f:
            json_string = json.dumps(tasks)
            f.write(json_string)
