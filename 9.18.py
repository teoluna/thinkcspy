def subst_chiper(msg, mapStr):
    newmsg = ""
    for char in msg:
        char = char.upper()
        newchar = mapStr.find(char + "-")
        new = mapStr[newchar + 2]
        newmsg += new
    return newmsg

mapStr = "A-B, B-C, C-D, D-E, E-F, F-G, G-H, H-I, I-J, J-K, K-L, L-M, M-N, N-O, O-P, P-Q, Q-R, R-S, S-T, T-U, U-V, V-W, W-X, X-Y, Y-Z, Z-A,  -_"
msg = "Message for encryption"

print(subst_chiper(msg, mapStr))