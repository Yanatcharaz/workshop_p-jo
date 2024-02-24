def f(x):
    return x**2-4
def df(x):
    return 2*x

x=10
f_x=f(x)
df_x=df(x)


from newton import Newton

aaa=Newton(f, df)
aaa.solve(x,1e-10,100)


