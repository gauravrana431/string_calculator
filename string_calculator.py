import re

class StringCalculator:
    def __init__(self):
        self.call_count = 0
        self.add_occurred = [] 

    def add(self, numbers: str) -> int:
        self.call_count += 1

        if not numbers:          
            return 0

        delimiters = [',', '\n']
        if numbers.startswith('//'):
            header, numbers = numbers.split('\n', 1)
            custom_part = header[2:]
            if custom_part.startswith('['):               
                delimiters += re.findall(r'\[([^\]]+)\]', custom_part)
            else:
                delimiters.append(custom_part)

        delimiter_pattern = '|'.join(map(re.escape, delimiters))
        num_str = re.split(delimiter_pattern, numbers)

        total = 0
        negativeNumbers = []

        for num in num_str:
            if not num:
                continue
            value = int(num)
            if value < 0:
                negativeNumbers.append(value)
            elif value <= 1000: 
                total += value

        if negativeNumbers:
            raise ValueError(f"negative numbers {', '.join(map(str, negativeNumbers))}")


        return total

    def get_called_count(self) -> int:
        return self.call_count



