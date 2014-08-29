class test:
    start_urls = []
    def __init__(self):
        self.start_urls = self.create_start_url()

    def create_start_url(self):
        urls = []
        base_url = "http://www.clinicaltrials.gov/ct2/results?"
        options = self.parse_conf("query.conf")
        # print options
        if "term" in options:
            base_url += "term=" + options["term"]
        else:
            base_url += "term="

        if "recr" not in options or options["recr"].lower()=="all":
            options["recr"] = ""
        if "state1" not in options or options["state1"].lower()=="all":
            options["state1"] = ""
        base_url += "&recr=" + options["recr"] + "&state1=" + options["state1"]
        urls.append(base_url)
        return urls

    def parse_conf(self,filename):
        options = {}
        f = open(filename)
        for line in f:
            line = line.strip()
            if '#' in line:
                (line,comment) = line.split('#',1)
            if not line:
                continue
            if '=' in line:
                option,value = line.split('=',1)
                option = option.strip()
                value = value.strip()
                options[option] = value
        f.close()
        return options

test1 = test()
# options = test1.parse_conf("query.conf")
# print options
print test1.start_urls
