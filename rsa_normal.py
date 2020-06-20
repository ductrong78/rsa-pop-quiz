import sys
def find_n(p, q):
    n = p * q
    return n


def find_q(p, n):
    q = n / p
    return (q)


def find_torient_n(p, q):
    r = (p - 1) * (q - 1)
    return (r)

def cipher_from_ne(pt, n, e):
    ct = pow(pt, e) % n
    return (ct)
def find_d_bypq(p, q, e):
    phi = find_torient_n(p, q)
    m = 0
    for k in range (0, phi, 1):
        d = (1 + (k * phi)) % e
        if d == 0:
            m = (1 + (k * phi)) // e
            break
    return m
def find_d_byphi(phi, e):
    m = 0
    for k in range(0, phi, 1):
        d = (1 + (k * phi)) % e
        if d == 0:
            m = (1 + (k * phi)) // e
            break
    return m
def plaintext_frompe(ct, p, e, n):
    q = n//p
    d = find_d_bypq(p, q, e)
    pt = pow(ct, d, n)
    return pt
def plaintext_from_d(ct, d, n):

    pt = hex(pow(ct, d, n))
    return pt
sl = sys.argv
nt = "-n : find n by p, q\n" \
     "-q : find q by p, n\n" \
     "-r : find totient(n) by p, q\n" \
     "-c : find ciphertext by plaintext, n, e\n" \
     "-d : find d by p, q, e\n" \
     "-p : find plaintext by ciphertext, p or q, e, n"
if len(sl) == 1:
    print(nt)
else:
    if sl[1] == "-n":
        print("n =",find_n(int(sl[2]), int(sl[3])))
    elif sl[1] == "-q":
        print("q =", find_q(int(sl[2]), int(sl[3])))
    elif sl[1] == "-r":
        print("totient(n) =", find_torient_n(int(sl[2]), int(sl[3])))
    elif sl[1] == "-d":
        print("d =", find_d_bypq(int(sl[2]), int(sl[3]), int(sl[4])))
    elif sl[1] == "-c":
        print("ciphertext =", cipher_from_ne(int(sl[2]), int(sl[3]), int(sl[4])))
    elif sl[1] == "-p":
        print("plaintext =", plaintext_frompe(int(sl[2]), int(sl[3]), int(sl[4]), int(sl[5])))
    else: print(nt)