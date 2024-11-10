import re


class ExtrctData:
    def __init__(self):
        self.operating_range = []

    def get_voltage(self):
        try:
            voltage_pattern = r'(\d+(?:\.\d+)?)(?:-|\s+)?V\s*to\s*(\d+(?:\.\d+)?)(?:-|\s+)?V'
            # Search -all- matches for the pattern in file
            matches_voltage = re.finditer(voltage_pattern, self.script)
            voltage_ranges = []
            for voltage in matches_voltage:
                min_voltage = float(voltage.group(1))
                max_voltage = float(voltage.group(2))
                # Save the min and the max data into voltage_ranges array
                voltage_ranges.append({'min': min_voltage, 'max': max_voltage})

            # If there is only one answer
            if len(voltage_ranges) == 1:
                return voltage_ranges[0]

            # If there are few answers check if they are identical if not - return None
            first_range = voltage_ranges[0]
            for voltage_range in voltage_ranges[1:]:
                if voltage_range['min'] != first_range['min'] or voltage_range['max'] != first_range['max']:
                    return None
            return first_range
        except Exception as e:
            print(f"Error processing: {str(e)}")

    def get_temperature(self):
        try:
            temperature_pattern = r'([+–-]?\d+)\s*[°⁰]?\s*C\s*to\s*([+–-]?\d+)\s*[°⁰]?\s*C'
            # Search -all- matches for the pattern in file
            temperatures = re.finditer(temperature_pattern, self.script)
            temperatures_ranges = []
            for temperature in temperatures:
                min_temperature_str = temperature.group(1)
                # Checking if the minus is written correctly
                if min_temperature_str.startswith('–'):
                    min_temperature_str = '-' + min_temperature_str[1:]
                min_temperature = float(min_temperature_str)

                max_temperature_str = temperature.group(2)
                # Checking if the minus is written correctly
                if max_temperature_str.startswith('–'):
                    max_temperature_str = '-' + max_temperature_str[1:]
                max_temperature = float(max_temperature_str)

                # Save the min and the max data into voltage_ranges array
                temperatures_ranges.append({'min': min_temperature, 'max': max_temperature})

            # If there is only one answer
            if len(temperatures_ranges) == 1:
                return temperatures_ranges[0]

            # If there are few answers check if they are identical if not - return None
            first_range = temperatures_ranges[0]
            for temperature_range in temperatures_ranges[1:]:
                if temperature_range['min'] != first_range['min'] or temperature_range['max'] != first_range['max']:
                    return None
            return first_range
        except Exception as e:
            print(f"Error processing: {str(e)}")

    def get_operating_ranges(self, file_path):
        try:
            # Open and read the file content
            self.txt_file = open(file_path, 'r')
            self.script = self.txt_file.read().strip()
            # Reading of the voltage and temperatures and storage in the operating_range array
            self.operating_range.append({'voltage': self.get_voltage(), 'temperature': self.get_temperature()})
            self.txt_file.close()
        except Exception as e:
            print(f"Error: {e}")


