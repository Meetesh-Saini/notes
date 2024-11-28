from sage.all import *
from Crypto.Util.number import long_to_bytes

n1 = 46079495604701097210605130474390742533625805658199515036409084114927754901373
c1 = 29895280587904224069299890044241091165244333244698360373130490320631344557677
n2 = 79227851709501877413610746064341727161909381331106309326774361440475382741143
c2 = 37682204634415676729107642500962731266440907990452778604043102625152670962626
n3 = 99145052382328217620437811908591180726312054787792531654079722998960667632413
c3 = 57178307266842910823994203827063677936264723209345836946065110596376286679351
n4 = 74274755080319699155516061185733624649668162004325050605245587972678816803329
c4 = 25551489060702899444611595891810259109866273402096710296490025062450696792476

e = 4

moduli = [n1, n2, n3, n4]
cts = [c1, c2, c3, c4]

N = prod(moduli)
Ns = [N // n for n in moduli]
inverse_Ns = [inverse_mod(Ns[i], moduli[i]) for i in range(len(moduli))]

combined_ct = sum(cts[i] * Ns[i] * inverse_Ns[i] for i in range(len(moduli))) % N

m_root = combined_ct.nth_root(e)

if m_root**e == combined_ct:
    plaintext = long_to_bytes(m_root).decode('utf-8')
    print("Plaintext:", plaintext)
else:
    print("Not found.")
