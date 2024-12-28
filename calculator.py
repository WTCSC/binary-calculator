def binary_calculator(bin1, bin2, operator):
    def binary_to_decimal(binary):
        try:
            return int(binary, 2)
        except ValueError:
            return "Error"

    def decimal_to_binary(decimal):
        if decimal < 0 or decimal > 255:
            return "Overflow"
        return format(decimal, '08b')

    if not (set(bin1) <= {'0', '1'} and set(bin2) <= {'0', '1'}):
        return "Error"

    dec1 = binary_to_decimal(bin1)
    dec2 = binary_to_decimal(bin2)

    if dec1 == "Error" or dec2 == "Error":
        return "Error"

    try:
        if operator == '+':
            result = dec1 + dec2
        elif operator == '-':
            result = dec1 - dec2
        elif operator == '*':
            result = dec1 * dec2
        elif operator == '/':
            if dec2 == 0:
                return "NaN"
            result = dec1 // dec2
        else:
            return "Error"
    except OverflowError:
        return "Overflow"

    return decimal_to_binary(result)
