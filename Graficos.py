import matplotlib.pyplot as plt
import numpy as np
import unicodedata


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")


tragetoria_bola = open("Ora_bolas-trajetoria_bola_oficial.txt", "r")
dados = tragetoria_bola.readlines()
tragetoria_bola.close()


#-------------------------------Formatação de dados da bola-------------------
dados_formatados = []
for linha in dados:
    linha = remove_control_characters(linha)
    if linha == "":
        continue
    dados_formatados.append(linha)
dados_formatados.pop(0)

#Separar os dados da bola em listas
T_bola = []
X_bola = []
Y_bola = []
for linha in dados_formatados:
    counter = 0
    tipo = 0
    dado = ""
    for char in linha:
        if(counter > 0):
            dado+=char
            if counter == 2 and tipo == 0:
                T_bola.append(float(dado))
                tipo = 1
                dado = ""
                counter = 0
            elif counter == 3 and tipo == 1:
                X_bola.append(float(dado))
                tipo = 2
                dado = ""
                counter = 0
            elif counter == 3 and tipo == 2:
                Y_bola.append(float(dado))
                tipo = 0
                dado = ""
                counter = 0
            if counter > 0:
                counter += 1
        elif (char == ","):
            dado += "."
            counter = 1
        else:
            dado += char

tragetoria_robo = open("trajetoria_robo.txt", "r")
dados = tragetoria_robo.readlines()
tragetoria_robo.close()

#-------------------------------Formatação de dados do robo-------------------
T_robo = []
X_robo = []
Y_robo = []
dados.pop(0)
for linha in dados:
  linha = linha.split(" ")
  X_robo.append(float(linha[0]))
  Y_robo.append(float(linha[1]))
  T_robo.append(float(linha[2]))

#-------------------------------Formatação de dados do contato-------------------

contador = 0
T_bola_contato = []
X_contato = []
Y_contato = []
for i in range(len(T_bola)):
  contador += 1
  if T_bola[i] > T_robo[-1]:
    break
for i in range(contador):
  X_contato.append(X_bola[i])
  Y_contato.append(Y_bola[i])
  T_bola_contato.append(T_bola[i])
  

# Plot 1

  
xbola_inicial = np.array(X_bola)
ybola_inicial = np.array(Y_bola)
xcontato = np.array(X_contato)
ycontato = np.array(Y_contato)
xrobo = np.array(X_robo)
yrobo = np.array(Y_robo)

plt.subplot(2, 2, 1)
plt.plot(xrobo, yrobo,color = 'DarkSlateGray')
plt.plot(xbola_inicial, ybola_inicial, ls = '--', color = 'Grey')
plt.plot(xcontato, ycontato,color = 'Black')

plt.title("Interceptação Robo x Bola")
plt.xlabel("Posição em X")
plt.ylabel("Posição em Y")

# Plot 2

xcontato = np.array(X_contato)
tcontato = np.array(T_bola_contato)
xrobo = np.array(X_robo)
trobo = np.array(T_robo)

plt.subplot(2, 2, 2)
plt.plot(trobo, xrobo,color = 'DarkSlateGray')
plt.plot(tcontato, xcontato,color = 'Black')

plt.title("Interceptação Robo x Bola em X")
plt.xlabel("Tempo")
plt.ylabel("Posição x")

# Plot 3

ycontato = np.array(Y_contato)
tcontato = np.array(T_bola_contato)
yrobo = np.array(Y_robo)
trobo = np.array(T_robo)

plt.subplot(2, 2, 3)
plt.plot(trobo, yrobo,color = 'DarkSlateGray')
plt.plot(tcontato,ycontato,color = 'Black')

plt.title("Interceptação Robo x Bola em Y")
plt.xlabel("Tempo")
plt.ylabel("Posição Y")






plt.tight_layout()
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.suptitle("Oras Bolas")
plt.show()