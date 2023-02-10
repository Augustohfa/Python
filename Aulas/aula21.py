"""
Constante = "Váriaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <-- contavem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

carro_passou_velocidade = velocidade >= RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and carro_passou_velocidade

if carro_passou_velocidade:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou do radar 1')

if carro_multado_radar_1:
    print('Carro multado no radar 1')
