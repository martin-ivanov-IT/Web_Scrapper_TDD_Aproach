import json


class Writer:
    def __init__(self, fp):
        self.fp = fp

    def writeRowToFile(self, articles):
        json_string = json.dumps([ob.__dict__ for ob in articles], ensure_ascii=False, indent=4)
        # print(json_string)
        self.fp.write(json_string)

