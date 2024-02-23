
def F_to_C(number:int) -> int:
    return int(5 / 9 * (number - 32))

def C_to_F(number:int) -> int:
    return int(number * 9 / 5 + 32)

def covert_temperature(temp: str, tempTO: str) -> str: 
    if tempTO == '°F':
        temp = C_to_F(int(temp))
    else:
        temp = F_to_C(int(temp))     
    temp = str(temp) + tempTO 

    return temp