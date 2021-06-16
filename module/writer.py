import json


class Writer:
    def __init__(self, fp):
        self.fp = fp

    # writes Article list in json format
    def write(self, articles):
        json_string = json.dumps([ob.__dict__ for ob in articles], ensure_ascii=False, indent=4)
        self.fp.write(json_string)

