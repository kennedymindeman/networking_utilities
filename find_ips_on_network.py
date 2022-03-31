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

    def get_length_of_bitmask(self) -> int:
        """gets the length of the string of 1s in the subnet mask"""
        bits = ''.join([f'{int(octet):b}' for octet in self.mask.split('.')])
        ones, zeroes = bits.split('0', 1)
        if int(zeroes) != 0:
            raise ValueError("unhandled subnet mask format")
        return len(ones)

    def scan_subnet(self) -> list:
        """runs nmap on the subnet"""
        nmap_out = os.popen(f'nmap {self.ipv4}/{self.get_length_of_bitmask()}')
        ret = []
        # for line in nmap_out.read().split('\n'):
        #     lst +=
        return ret

ip_config = ipConfig()
ip_config.ipv4

# ip_format = '\d+\.\d+\.\d+'
