class EmbeddedIPResolver:
    @staticmethod
    def intTryParse(value):
        try:
            int_value = int(value)

            if 0 <= int_value <= 255:
                return int_value, True

            return value, False
        except ValueError:
            return value, False

    @staticmethod
    def resolve(resolverqnamelist, qnamelist):

        # resolverqnamelist: com, example
        # qnamelist: com, example, <nonnumeric>, <numeric>, .. containing at least 4 numeric.

        if resolverqnamelist is None:
            return None

        if len(qnamelist) < len(resolverqnamelist) + 4:
            return None

        for i in range(0, len(resolverqnamelist)):
            if resolverqnamelist[i] != qnamelist[i]:
                return None

        parsed = [EmbeddedIPResolver.intTryParse(label) for label in qnamelist[len(resolverqnamelist):]]

        parts = []

        inserter = parts.insert

        for (value, success) in parsed:
            if not success:
                continue

            inserter(0, value)

        if len(parts) < 4:
            return None

        host = ".".join(repr(x) for x in parts[:4])

        return host
