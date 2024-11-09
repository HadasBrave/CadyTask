import re
from file_handling import FileHandeling

class ExtrctData:
    def __init__(self):
        self.operating_range = []
        # self.get_operating_ranges()

    def get_voltage(self):
        voltage_pattern = r'(\d+(?:\.\d+)?)(?:-|\s+)?V\s*to\s*(\d+(?:\.\d+)?)(?:-|\s+)?V'
        # search all matches in file
        matches_voltage = re.finditer(voltage_pattern, self.script)

        voltage_ranges =[]
        for voltage in matches_voltage:
            min_voltage = float(voltage.group(1))
            max_voltage = float(voltage.group(2))

            voltage_ranges.append({'min': min_voltage, 'max': max_voltage})

        if not voltage_ranges:
            return None

        if len(voltage_ranges) == 1:
            return voltage_ranges[0]

        first_range = voltage_ranges[0]
        for voltage_range in voltage_ranges[1:]:
            if voltage_range['min'] != first_range['min'] or voltage_range['max'] != first_range['max']:
                return None
        return first_range

    def get_temperature(self):
        temperature_pattern = r'([+–-]?\d+)\s*[°⁰]?\s*C\s*to\s*([+–-]?\d+)\s*[°⁰]?\s*C'
        # search all matches in file
        temperatures = re.finditer(temperature_pattern, self.script)

        temperatures_ranges =[]
        for temperature in temperatures:
            min_temperature_str = temperature.group(1)
            if min_temperature_str.startswith('–'):
                min_temperature_str = '-' + min_temperature_str[1:]
            min_temperature = float(min_temperature_str)

            max_temperature_str = temperature.group(2)
            if max_temperature_str.startswith('–'):
                max_temperature_str = '-' + max_temperature_str[1:]
            max_temperature = float(max_temperature_str)

            temperatures_ranges.append({'min': min_temperature, 'max': max_temperature})

        if not temperatures_ranges:
            return None

        if len(temperatures_ranges) == 1:
            return temperatures_ranges[0]

        first_range = temperatures_ranges[0]
        for temperature_range in temperatures_ranges[1:]:
            if temperature_range['min'] != first_range['min'] or temperature_range['max'] != first_range['max']:
                return None
        return first_range

    def get_operating_ranges(self, file_path):
        self.txt_file = FileHandeling(file_path)
        self.script = self.txt_file.script
        self.operating_range.append({'voltage': self.get_voltage(), 'temperature': self.get_temperature()})
        self.txt_file.close_file()


