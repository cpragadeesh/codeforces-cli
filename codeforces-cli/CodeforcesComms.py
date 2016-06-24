import urllib2

class CodeforcesComms(object):
    """Wraps all communication with codeforces"""
    def __init__(self):
        self.contest_id = None
        self.problem_id = None
        self.username = None
        self.password = None

    def open_problem_page(self):
        url = "http://codeforces.com/contest/"
        page = urllib2.urlopen(url + self.contest_id + '/problem/' + self.problem_id)

        return page.read()
