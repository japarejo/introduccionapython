import matplotlib.pyplot as plt


def draw_fibo(n):
    ratio = []
    num = []

    # Starting values
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        num.append(i)
        ratio.append(c / b)
        a = b
        b = c
    draw_graph(num, ratio)
    
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('No.')

    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive Fibonacci numbers')
    plt

draw_fibo(100)