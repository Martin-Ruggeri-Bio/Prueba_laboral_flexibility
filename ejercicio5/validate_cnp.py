from datetime import datetime

def validar_cnp(cnp):
    # Constantes
    CONTROL_STRING = "279146358279"
    AREA_CODES = set(f"{i:02d}" for i in range(1, 53)) # Códigos de área válidos del 01 al 52
    GENDER_CODES = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    # Verificar la longitud del CNP
    if len(cnp) != 13:
        return "Longitud inválida, debe tener 13 dígitos."

    # Verificar el código de género
    if cnp[0] not in GENDER_CODES:
        return "Código de género inválido."

    # Verificar el año de nacimiento
    year = cnp[1:3]
    if not year.isdigit() or int(year) > 99:
        return "Año de nacimiento inválido."
    if cnp[0] == '5' or cnp[0] == '6':
        if int(year) > datetime.now().year % 100:
            return "Año de nacimiento mayor que el actual."

    # Verificar el mes de nacimiento
    month = cnp[3:5]
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        return "Mes de nacimiento inválido."

    # Verificar el día de nacimiento
    day = cnp[5:7]
    if not day.isdigit() or int(day) < 1 or int(day) > 31:
        return "Día de nacimiento inválido."

    # Verificar el código de área
    area_code = cnp[7:9]
    if area_code not in AREA_CODES:
        return "Código de área inválido."

    # Verificar el número de orden
    order_number = cnp[9:12]
    if not order_number.isdigit():
        return "Número de orden inválido."

    # Verificar el dígito de control
    control_sum = sum(int(cnp[i]) * int(CONTROL_STRING[i]) for i in range(12))
    control_digit = control_sum % 11
    control_digit = 1 if control_digit == 10 else control_digit

    if str(control_digit) != cnp[-1]:
        return "Dígito de control inválido."

    return "CNP válido."


if __name__ == "__main__":
    valid_cnp_list = [
    "7000103172530",
    "2971010152544",
    "1991113312217",
    "1000516397063",
    "6000627077402"
    ]

    for cnp in valid_cnp_list:
        print(validar_cnp(cnp))
    
    invalid_cnp_list = [
    "3971210152544",
    "1880131560173",
    "1961301560173",
    "1960133560173",
    "5990131355213"
    ]

    for cnp in invalid_cnp_list:
        print(validar_cnp(cnp))