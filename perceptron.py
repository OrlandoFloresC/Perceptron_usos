#---------------esta es solo una neurona---------------#

inputs = [1, 2, 3] #entradas a mi red neuronal
weights = [0.2, 0.8, -0.5] #pesos
bias = 2 #sesgo

output = (inputs[0]*weights[0] + #salida    #salida = entrada*peso+sesgo   (y = xm+b)
inputs[1]*weights[1] +           #para este caso como son tres entradas, por eso se hace tres vecss la operacion y al 
inputs[2]*weights[2] + bias)        #final se suma el sesgo

print(f"salida de la neurona 1, {output}") #impresion de salida

#---------------esta es solo una neurona---------------#
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0
output = (inputs[0]*weights[0] +        #salida    #salida = entrada*peso+sesgo   (y = xm+b
inputs[1]*weights[1] +                  #para este caso como son tres entradas, por eso se hace cuatro vecss la operacion y al 
inputs[2]*weights[2] +                   #final se suma el sesgo
inputs[3]*weights[3] + bias)
print(f"salida de la neurona 2, {output}") #impresion de salida

