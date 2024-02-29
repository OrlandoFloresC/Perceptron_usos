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

#----------------tres neuronas, una capa----------------#

inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5
outputs = [
# Neuron 1:
inputs[0]*weights1[0] +
inputs[1]*weights1[1] +
inputs[2]*weights1[2] +
inputs[3]*weights1[3] + bias1,
# Neuron 2:
inputs[0]*weights2[0] +
inputs[1]*weights2[1] +
inputs[2]*weights2[2] +
inputs[3]*weights2[3] + bias2,
# Neuron 3:
inputs[0]*weights3[0] +
inputs[1]*weights3[1] +
inputs[2]*weights3[2] +
inputs[3]*weights3[3] + bias3]
print(outputs)

#----------------tres neuronas, una capa----------------#
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
[0.5, -0.91, 0.26, -0.5],
[-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
# Output of current layer
layer_outputs = []
# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    print(f"pesos {neuron_weights}, bias {neuron_bias}")
    # Zeroed output of given neuron
    neuron_output = 0
    # For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply this input by associated weight
        # and add to the neuron’s output variable
        neuron_output += n_input*weight
    # Add bias
    neuron_output += neuron_bias
    # Put neuron’s result to the layer’s output list
    layer_outputs.append(neuron_output)
    print("Aqui termina la vuelta de los for")
print(f"salidas {layer_outputs}")