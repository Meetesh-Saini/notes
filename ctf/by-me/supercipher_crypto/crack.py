import string

class Crack:
    def __init__(self):
        self.k_len = 4
        self.k_spc = "0123456789"

    def dec(self, ct, k):
        pt = ""
        for i, c in enumerate(ct):
            k_c = k[i % len(k)]
            pt += chr(ord(c) ^ ord(k_c))
        return pt

    def crack(self, ct):
        ct = ct.strip()
        psbl_pts = []
        for k_cand in range(10000):
            k = str(k_cand).zfill(self.k_len)
            pt = self.dec(ct, k)
            if all(c.isprintable() for c in pt):
                psbl_pts.append(pt)
        return psbl_pts


if __name__ == "__main__":
    with open("./out/output.txt", "rb") as f:
        ct = f.read().decode()
    crkr = Crack()
    res = crkr.crack(ct)

    print("Possible flags:")
    for r in res:
        if not r.startswith("ctf{"): continue
        print(r)
