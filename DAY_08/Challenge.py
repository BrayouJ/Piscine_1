import turtle as t
for j in range(3):
    for i in range(6):
        t.fd(10*2**i)
        t.lt(120)
        t.fd(10*2**i)
        t.lt(120)
        t.fd(5*2**i)
        t.lt(120)
        t.fd(5*2**i)
        t.rt(120)
        t.fd(5*2**i)
        t.rt(120)
        t.fd(5*2**i)
        t.lt(120)
        t.fd(5*2**i)
        t.lt(120)
    t.fd(320)
    t.lt(120)

t.mainloop()