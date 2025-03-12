# 15. Crie um programa dado solicite a largura e o comprimento de uma sala 
# (supondo que a sala seja quadrática), 
# solicite a largura e o tamanho do piso 
# e mostre quantos peças do preciso será necessário para revestir toda a sala.

room_width = float(input("Insira a largura da sala: "))
room_length = float(input("Insira o comprimento da sala: "))
floor_width = float(input("Insira a largura do piso: "))
floor_length = float(input("Insira o comprimento do piso: "))

room_area = room_width * room_length
floor_area = floor_width * floor_length
pieces_needed = room_area // floor_area

print(f"São necessários {pieces_needed} peças de piso para revestir toda a sala.")