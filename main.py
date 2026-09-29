states_ID = {
    1: "Aguascalientes",
    2: "Baja California",
    3: "Baja California Sur",
    4: "Campeche",
    5: "Coahuila",
    6: "Colima",
    7: "Chiapas",
    8: "Chihuahua",
    9: "Ciudad de México",
    10: "Durango",
    11: "Guanajuato",
    12: "Guerrero",
    13: "Hidalgo",
    14: "Jalisco",
    15: "Estado de México",
    16: "Michoacán",
    17: "Morelos",
    18: "Nayarit",
    19: "Nuevo León",
    20: "Oaxaca",
    21: "Puebla",
    22: "Querétaro",
    23: "Quintana Roo",
    24: "San Luis Potosí",
    25: "Sinaloa",
    26: "Sonora",
    27: "Tabasco",
    28: "Tamaulipas",
    29: "Tlaxcala",
    30: "Veracruz",
    31: "Yucatán",
    32: "Zacatecas"
}

states_abbr = {
    1: "AGS", 2: "BCN", 3: "BCS", 4: "CAM", 5: "COA", 6: "COL",
    7: "CHP", 8: "CHH", 9: "CDX", 10: "DUR", 11: "GTO", 12: "GRO",
    13: "HID", 14: "JAL", 15: "MEX", 16: "MIC", 17: "MOR", 18: "NAY",
    19: "NLE", 20: "OAX", 21: "PUE", 22: "QRO", 23: "ROO", 24: "SLP",
    25: "SIN", 26: "SON", 27: "TAB", 28: "TAM", 29: "TLA", 30: "VER",
    31: "YUC", 32: "ZAC"
}


branches = {
    1: 2,   # Aguascalientes
    2: 4,   # Baja California
    3: 1,   # Baja California Sur
    4: 1,   # Campeche
    5: 3,   # Coahuila
    6: 1,   # Colima
    7: 2,   # Chiapas
    8: 5,   # Chihuahua
    9: 10,  # Ciudad de México
    10: 2,  # Durango
    11: 6,  # Guanajuato
    12: 2,  # Guerrero
    13: 3,  # Hidalgo
    14: 8,  # Jalisco
    15: 7,  # Estado de México
    16: 3,  # Michoacán
    17: 2,  # Morelos
    18: 1,  # Nayarit
    19: 8,  # Nuevo León
    20: 3,  # Oaxaca
    21: 5,  # Puebla
    22: 4,  # Querétaro
    23: 3,  # Quintana Roo
    24: 3,  # San Luis Potosí
    25: 4,  # Sinaloa
    26: 4,  # Sonora
    27: 2,  # Tabasco
    28: 4,  # Tamaulipas
    29: 1,  # Tlaxcala
    30: 6,  # Veracruz
    31: 4,  # Yucatán
    32: 2  # Zacatecas
}

def split_ip(ip: str) -> list[int]:
    ip_octets_numb = []
    ip_octets_text = ip.split(".")

    if len(ip_octets_text) != 4:
        return []
    try:
        for octet in ip_octets_text:
            octet_numb = int(octet)
            if not (0 <= octet_numb <= 255):
                return []
            ip_octets_numb.append(octet_numb)
    except ValueError:
        return []
    
    return ip_octets_numb

def octets_validator(ip: list[int], branches: dict[int, int]) -> bool:
    if not ip:
        return False
    if len(ip) != 4:
        return False
    if ip[0] != 10:
        return False
    if not 1 <= ip[1] <= 32:
        return False

    branch = ip[2]
    max_branches = branches.get(ip[1])

    if max_branches is None:
        return False
    return 0 < branch <= max_branches

def state_identifier(ip: list[int], states: dict[int, str]) -> str:
    if not ip or len(ip) < 2:
        return "Error: Invalid router ID, cannot be identified." 
    
    return states.get(ip[1], "Error: State not found")

def abbr_identifier(ip: list[int], states_abbr: dict[int, str]) -> str:
    if not ip or len(ip) < 2:
        return "Error: Invalid router ID, cannot be identified."
    
    return states_abbr.get(ip[1], "Error: State not found")

def branch_identifier(ip: list[int]):
    return ip[2]


def host_identifier(ip: list[int]) -> tuple[str, str, int]:
    if not ip or len(ip) < 4:
        return "Error: Invalid router ID, cannot be identified.", "Error", 0

    host = ip[3]

    if 1 <= host <= 10:
        return "Router", "RTR", host
    elif 11 <= host <= 30:
        return "Switch L3", "SWC", host-10
    elif 31 <= host <= 60:
        return "Switch L2", "SWA", host-30
    else:
        return "Not found", "Not found", host

def identifier_main(ip: list[int], states, branches, states_abbr):
        if octets_validator(ip, branches):
            host = host_identifier(ip)
            print(f"Hostname: {abbr_identifier(ip, states_abbr)}-SUC{branch_identifier(ip):02d}-{host[1]}{host[2]:02d}")
            print(f"State: {state_identifier(ip, states)}")
            print(f"Branch: {branch_identifier(ip):02d}")
            print(f"Device: {host[0]}")
            print(f"Host Number: {host[2]:02d}")
        else:
            print("Error: Invalid router ID, cannot be identified")


def main():
    router_ID_text = "10.15.6.18"
    router_ID_numb = split_ip(router_ID_text)
    identifier_main(router_ID_numb, states_ID, branches, states_abbr)

main()   

