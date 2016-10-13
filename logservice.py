import requests
import traceback


class LogService:
    def __init__(self, endpoint):
        if endpoint.endswith("/"):
            self.endpoint = endpoint[:-1]
        else:
            self.endpoint = endpoint

        self.prefix = "%s/d/" % self.endpoint

        print "LogService prefix: %s" % self.prefix

    def record_hit(self, identity, concatenated_subdomains, comment=None):

        if comment is None:
            comment = ""

        url = self.prefix + comment + "?id=" + identity

        if len(concatenated_subdomains) > 0:
            url += "&subs=" + concatenated_subdomains

        try:

            requests.get(url)
        except Exception as e:
            # Log and ignore the exception.
            print traceback.print_exc()
