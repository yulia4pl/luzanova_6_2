
def m_to_ft(number:int) -> int:
    return int(number / 0.3048)

def ft_to_m(number:int) -> int:
    return int(number * 0.3048)

def covert_distance(dist: str, distTO: str) -> str: 
    if distTO == 'm':
        dist = ft_to_m(int(dist))
    else:
        dist = m_to_ft(int(dist))     
    dist = str(dist) + distTO 

    return dist