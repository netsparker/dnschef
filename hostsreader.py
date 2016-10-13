class HostsReader:
    @staticmethod
    def read_all(path):
        try:
            result = {}

            with open(path, 'r') as file:
                lines = [line for line in file]
                for line in lines:
                    line = line.strip()

                    if len(line) == 0:
                        continue

                    if line[0] == "\r":
                        continue

                    if line[0] == "\n":
                        continue

                    if line[0] == "#":
                        continue

                    parts = line.split()

                    result[parts[1]] = parts[0]

            return result
        except IOError:
            return {}
