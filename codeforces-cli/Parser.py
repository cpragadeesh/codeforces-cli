from HTMLParser import HTMLParser

class HTMLParser(HTMLParser):

    def __init__(self):
        self.inside_input = 0
        self.inside_output = 0
        self.inside_pre = 0
        self.test_cases_list = []

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[1] == "input":
                self.inside_input = 1
            elif attr[1] == "output":
                self.inside_output = 1
        if tag == "pre":
            self.inside_pre = 1

    def handle_endtag(self, tag):
        if tag == "pre":
            self.inside_pre = self.inside_input = self.inside_output = 0

    def handle_data(self, data):
        if inside_pre == 1:
            if inside_input == 1:
                print data

class Parser(object):
    def __init__(self):
        self.parser = HTMLParser()

    def get_test_cases(self, page):
        self.parser.feed(page)
