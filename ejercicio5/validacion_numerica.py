def validate_cnp(cnp):
    # Verificar la longitud del CNP
    if len(cnp) != 13:
        print("Longitud incorrecta")
        return False

    # Verificar el género
    gender_digit = int(cnp[0])
    if gender_digit not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False

    # Verificar el año de nacimiento
    year_digit = int(cnp[1:3])
    if (gender_digit in [1, 2] and not 0 <= year_digit <= 99) or \
       (gender_digit in [3, 4] and not 0 <= year_digit <= 99) or \
       (gender_digit in [5, 6] and not 0 <= year_digit <= 99) or \
       (gender_digit in [7, 8] and not 0 <= year_digit <= 99) or \
       (gender_digit == 9 and year_digit != 0):
        return False

    # Verificar el mes de nacimiento
    month_digit = int(cnp[3:5])
    if not 1 <= month_digit <= 12:
        return False

    # Verificar el día de nacimiento
    day_digit = int(cnp[5:7])
    if not 1 <= day_digit <= 31:
        return False

    # Verificar el código de área
    county_code_digit = int(cnp[7:9])
    if not 1 <= county_code_digit <= 52:
        return False

    # Verificar el número de pedido
    order_number_digit = int(cnp[9:12])
    if not 0 <= order_number_digit <= 999:
        return False

    # Calcular y verificar el dígito de control
    control_digit = int(cnp[12])
    weighted_sum = sum(int(cnp[i]) * int("279146358279"[i]) for i in range(12))
    remainder = weighted_sum % 11
    if remainder == 10:
        remainder = 1
    if remainder != control_digit:
        return False

    return True

# Ejemplos de números de identificación válidos y no válidos
valid_cnp_list = [
    "7000103172530",
    "2971010152544",
    "1991113312217",
    "1000516397063",
    "6000627077402"
]

invalid_cnp_list = [
    "3971210152544",  # Género no válido (3)
    "2431010152544",  # Año de nacimiento inválido (fuera del rango especificado)
    "2971310152544",  # Mes de nacimiento inválido (13)
    "2971013252544",  # Día de nacimiento inválido (32)
    "29710101525453"  # Código de área inválido (53)
]

# Validar los números de identificación y mostrar los resultados
print("Resultados de validación para números de identificación válidos:")
for cnp in valid_cnp_list:
    print(f"{cnp}: {validate_cnp(cnp)}")

print("\nResultados de validación para números de identificación no válidos:")
for cnp in invalid_cnp_list:
    print(f"{cnp}: {validate_cnp(cnp)}")
