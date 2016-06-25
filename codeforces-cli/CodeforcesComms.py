import urllib2

class CodeforcesComms(object):
    """Wraps all communication with codeforces"""
    def __init__(self):
        self.username = None
        self.password = None

    def open_problem_page(self, contest_id, problem_id):
        url = "http://codeforces.com/contest/"
        page = urllib2.urlopen(url + contest_id + '/problem/' + problem_id)

        return page.read()
