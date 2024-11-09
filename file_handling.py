import re

class FileHandeling:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = self.open_file()
        self.script = self.read_file_contents()

    def open_file(self):
        try:
            return open(self.file_path, 'r')
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return None
        except Exception as e:
            print(f"Error opening file: {e}")
            return None

    def close_file(self):
        if self.file:
            self.file.close()

    def read_file_contents(self):
        if self.file:
            return self.file.read().strip()
        else:
            return None

    # def get_voltage(self, read_file_contents):
    #     voltage_pattern = r'(\d+(?:\.\d+)?)(?:-|\s+)?V\s*to\s*(\d+(?:\.\d+)?)(?:-|\s+)?V'
    #     # search all matches in file
    #     matches_voltage = re.finditer(voltage_pattern, read_file_contents)
    #
    #     voltage_ranges =[]
    #     for voltage in matches_voltage:
    #         min_voltage = float(voltage.group(1))
    #         max_voltage = float(voltage.group(2))
    #
    #         voltage_ranges.append({'min': min_voltage, 'max': max_voltage})
    #
    #     if not voltage_ranges:
    #         return None
    #
    #     if len(voltage_ranges) == 1:
    #         return voltage_ranges[0]
    #
    #     first_range = voltage_ranges[0]
    #     for voltage_range in voltage_ranges[1:]:
    #         if voltage_range['min'] != first_range['min'] or voltage_range['max'] != first_range['max']:
    #             return None
    #     return first_range
    #
    # def get_temperature(self, read_file_contents):
    #     temperature_pattern = r'([+–-]?\d+)\s*[°⁰]?\s*C\s*to\s*([+–-]?\d+)\s*[°⁰]?\s*C'
    #     # search all matches in file
    #     temperatures = re.finditer(temperature_pattern, read_file_contents)
    #
    #     temperatures_ranges =[]
    #     for temperature in temperatures:
    #         min_temperature_str = temperature.group(1)
    #         if min_temperature_str.startswith('–'):
    #             min_temperature_str = '-' + min_temperature_str[1:]
    #         min_temperature = float(min_temperature_str)
    #
    #         max_temperature_str = temperature.group(2)
    #         if max_temperature_str.startswith('–'):
    #             max_temperature_str = '-' + max_temperature_str[1:]
    #         max_temperature = float(max_temperature_str)
    #
    #         temperatures_ranges.append({'min': min_temperature, 'max': max_temperature})
    #
    #     if not temperatures_ranges:
    #         return None
    #
    #     if len(temperatures_ranges) == 1:
    #         return temperatures_ranges[0]
    #
    #     first_range = temperatures_ranges[0]
    #     for temperature_range in temperatures_ranges[1:]:
    #         if temperature_range['min'] != first_range['min'] or temperature_range['max'] != first_range['max']:
    #             return None
    #     return first_range


# v = FileHandeling('AD7791._2115.txt')
# s = v.read_file_contents()
# print(v.get_voltage(s))
# print(v.get_temperature(s))
# v.close_file()
