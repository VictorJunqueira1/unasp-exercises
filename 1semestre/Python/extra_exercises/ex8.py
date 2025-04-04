# 8. Validar um número de IP 
# (deve conter 12 dígitos, 
# seguir o padrão: xxx.xxx.xxx.xxx, 
# e ter somente números)
# 192.168.000.001
ip_address = input("Digite um IP válido: ")

# Verificar o comprimento do IP
if len(ip_address) != 15:
    print("IP Inválido. O IP deve conter 15 caracteres.")
else:
    # Separar o IP nos octetos
    octetos = ip_address.split(".")
    
    # Verificar se o IP tem 4 octetos
    if len(octetos) != 4:
        print("IP Inválido. O formato correto é xxx.xxx.xxx.xxx")
    else:
        valid = True

        # Verificar se cada octeto é numérico e está no intervalo de 0 a 255
        for i in range(4):
            # Verificar se o octeto é numérico
            if not octetos[i].isdigit():
                print(f"Octeto {i+1} inválido. Deve ser um número.")
                valid = False
                break
            
            # Verificar se o valor do octeto está entre 0 e 255
            if not (0 <= int(octetos[i]) <= 255):
                print(f"Octeto {i+1} inválido. O valor deve estar entre 0 e 255.")
                valid = False
                break
        
        # Se todos os octetos forem válidos, o IP é válido
        if valid:
            print("IP válido.")