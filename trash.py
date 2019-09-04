# s = np.random.normal(mu, sigma, 1000)

def normal(x, mu=0.1, sigma=0.01):
    return (1/(2 * math.pi * sigma)**(1/2))*math.e ** (-1 * ((x-mu) ** 2 / (2 * sigma)))


def normal_inversa(x, mu=0.1, sigma=0.01):
    # return (math.e ** (-1 * ((x - mu) ** 2 / 2 * sigma)) / (2 * math.pi)**(1/2) * (sigma)**(1/2))
    return (math.e ** (-1 * ((x - mu) ** 2 / (2 * sigma))) / ((2 * math.pi)**(1/2) * (sigma)**(1/2)))


def func_pepega(x):
    return x ** 2


def func_pepega_inv(x):
    return x ** (1/2)


def inverse_transformation():
    # generar una variable aleatoria uniforme entre 0 y 1
    x = random.uniform(0,1)
    print(x)
    b = func_pepega(x)
    a = func_pepega_inv(b)
    print(a)
    return 0
# inverse_func, N

inverse_transformation()


def F(fi, pi):
    randoms  = numpy.random.uniform(size=pi.shape)
    
    accumulated  = numpy.random.uniform(size=pi.shape)

    for i in range(len(randoms)):
        accumulated[i] = pi[i] * fi[i](numpy.random.uniform())
    
    return numpy.sum(accumulated)

# iterations inside the function
LENGTH = 2
# function 
FUNCTION = normal

# fill an a array with numbers between 0 and 1
b = numpy.linspace(0, 1, num=LENGTH)
# make an array with the pointer of the function with thte same length
a = [normal] * LENGTH

# make sure the sum is between 0 and 1
for i in range(len(b)):
    b[i] = b[i]/LENGTH * 2

# number of iterations
k = numpy.ones((1,25))

# execute the function for the number of iterations
for l in range(len(k)):
    k[l] = F(a, b)

# print the iterations
print(k)

# plot the histogram of the iterations