from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

def hastad_gen(flag_text, e=4, bits=256):
    m = bytes_to_long(flag_text.encode('utf-8'))

    assert m.bit_length() < bits, "flag is too large."

    moduli = []
    ciphertexts = []

    for _ in range(4):
        p = getPrime(bits // 2)
        q = getPrime(bits // 2)
        n = p * q

        c = pow(m, e, n)

        moduli.append(n)
        ciphertexts.append(c)

    return moduli, ciphertexts

flag = "ctf{$mall_3_B!G_bR3acH}"
mods, ciphers = hastad_gen(flag)

print("Public Exponent (e):", 4)
for i, (n, c) in enumerate(zip(mods, ciphers), start=1):
    print(f"n{i} = {n}")
    print(f"c{i} = {c}")
