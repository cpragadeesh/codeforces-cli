from HTMLParser import HTMLParser

class Parser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.inside_input = 0
        self.inside_output = 0
        self.inside_pre = 0
        self.test_cases_list = []
        self.current_input = ""
        self.current_output = ""
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[1] == "input":
                self.inside_input = 1
            elif attr[1] == "output":
                self.inside_output = 1
        if tag == "pre":
            self.inside_pre = 1
        if tag == "br" and self.inside_pre == 1:
            if self.inside_input == 1:
                self.current_input += '\n'
            elif self.inside_output == 1:
                self.current_output += '\n'

    def handle_endtag(self, tag):
        #if its a closing pre tag and both current_input and current_output is filled
        if tag == "pre" and len(self.current_output) > 0:
            self.test_cases_list.append([self.current_input, self.current_output])
            self.current_input = self.current_output = ""
            self.inside_pre = self.inside_input = self.inside_output = 0
        #if its a closing pre tag and only current_input exists
        elif tag == "pre":
            self.inside_pre = self.inside_input = 0

    def handle_data(self, data):
        if self.inside_pre == 1:
            if self.inside_input == 1:
                self.current_input = self.current_input + data
            if self.inside_output == 1:
                self.current_output = self.current_output + data

    def get_test_cases(self, page):
        self.feed(page)
        return self.test_cases_list
