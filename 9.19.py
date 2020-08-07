def decrypt(msg, alphabet):
    newmsg = ""
    for char in msg:
        newchar = mapStr.find(char + ",")
        new = mapStr[newchar - 2]
        newmsg += new
    return newmsg

mapStr = "A-B, B-C, C-D, D-E, E-F, F-G, G-H, H-I, I-J, J-K, K-L, L-M, M-N, N-O, O-P, P-Q, Q-R, R-S, S-T, T-U, U-V, V-W, W-X, X-Y, Y-Z, Z-A,  -_"
msg = "NFTTBHF_GPS_FODSZQUJPO"

print(decrypt(msg, mapStr))