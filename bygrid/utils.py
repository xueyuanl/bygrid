def get_decimal_precision(x):
    xstr = str(x)
    decimal = xstr[xstr.find('.') + 1:]
    res = 1
    for i in decimal:
        if i == '0':
            res += 1
        else:
            break
    return res


def format_decimal(decimal, precision):
    s = "{:.{}f}".format(decimal, precision)
    return float(s)
