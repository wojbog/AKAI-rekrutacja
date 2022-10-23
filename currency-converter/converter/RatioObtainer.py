import json
import datetime
import urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        try:
            f=open("ratios.json", "r")
            f = open('ratios.json',"r")
            data = json.load(f)
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d")
            f.close()
            for licznik in data:
                if licznik['base_currency'] == self.base and licznik['target_currency'] == self.target and licznik['date_fetched'] == str(now):
                    return True
            return False
        except IOError:
            return False

    def fetch_ratio(self):
        url = 'https://api.exchangerate.host/convert?from='+self.base+'&to='+self.target
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        self.save_ratio(data['result'])

    def save_ratio(self, ratio):
        czy = False

        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d")

        f = open('ratios.json',"r")
        data = json.load(f)
        
        f.close()
        tab = []
        for licznik in data:
            if licznik['base_currency'] == self.base and licznik['target_currency'] == self.target:
                licznik["ratio"] = ratio
                licznik["date_fetched"] = str(now)
                czy = True
            tab.append(licznik)

        if not czy:
            obj = {
                "base_currency": self.base,
                "target_currency": self.target,
                "date_fetched": now,
                "ratio": ratio
            }
            tab.append(obj)

        json_string = json.dumps(tab)
        f = open('ratios.json',"w")
        f.write(json_string)
        f.close()

    def get_matched_ratio_value(self):
        f=open("ratios.json", "r")
        f = open('ratios.json',"r")
        data = json.load(f)
        f.close()
        for licznik in data:
            if licznik['base_currency'] == self.base and licznik['target_currency'] == self.target:
                return licznik['ratio']

