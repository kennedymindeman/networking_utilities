import os


class ipConfig:
    def __init__(self):
        """generates an IP config object that contains network info"""
        self.update()

    def update(self):
        """refreshes the ip configuration"""
        self.properties_table = self.generate_properties_table()
        self.ipv4 = self.properties_table.get('IPv4 Address', '')
        self.mask = self.properties_table.get('Subnet Mask', '')

    def generate_properties_table(self) -> dict:
        """gets a dictionary containing ipconfig output key val pairs"""
        def get_key_val_pair(line: str) -> tuple:
            split_line = line.split(':', 1)
            if len(split_line) != 2:
                return None, None
            key = split_line[0].strip('. ')
            val = split_line[1].strip()
            return key, val

        properties_table = {}
        lines = os.popen('ipconfig').read().split('\n')
        for line in lines:
            key, val = get_key_val_pair(line)
            if key is not None and val is not None:
                properties_table[key] = val
        return properties_table


ip_config = ipConfig()
ip_config.ipv4

# ip_format = '\d+\.\d+\.\d+'