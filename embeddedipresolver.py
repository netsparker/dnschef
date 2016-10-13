class EmbeddedIPResolver:
    @staticmethod
    def intTryParse(value):
        try:
            int_value = int(value)

            if int_value >= 0 and int_value <= 255:
                return int_value, True

            return value, False
        except ValueError:
            return value, False

    @staticmethod
    def resolve(resolverqnamelist, qnamelist):

        # resolverqnamelist: com, example
        # qnamelist: com, example, <nonnumeric>, <numeric>, .. containing at least 4 numeric.

        if resolverqnamelist == None:
            return None

        if (len(qnamelist) < len(resolverqnamelist) + 4):
            return None

        for i in xrange(0, len(resolverqnamelist)):
            if resolverqnamelist[i] != qnamelist[i]:
                return None

        parsed = [EmbeddedIPResolver.intTryParse(label) for label in qnamelist[len(resolverqnamelist):]]

        parsedInts = []

        for (value, success) in parsed:
            if success == False:
                continue

            parsedInts.insert(0, value)

        if len(parsedInts) < 4:
            return None

        host = ".".join(str(x) for x in parsedInts[:4])

        return host
