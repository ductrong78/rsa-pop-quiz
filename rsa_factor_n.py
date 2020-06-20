c = 75255211525734906277613835402288071430424711843008312747643427244949719195672234122510020964867700252670244766001468020455126734930816038170132044449149735461901965598381845578526965018707455468744133280765494836716331440441833708023757763703839321973314144967005707470020843808139177446669235792085083974008139114631575300672475637591623113579
n = 80571169762502583570860870218556349196555637633352661972486042263902899680573704768281888658061048166392559784582972746485885424878934315809515482503689061543953907590593914715357105988099387515247165428638897015082933269944745516748032673274972933745714926582716826578053099683198282736703006336437829014817026934365530607103809813016877261119
e = 65537
def find_d_byphi(phi, e):
    m = 0
    for k in range(0, phi, 1):
        d = (1 + (k * phi)) % e
        if d == 0:
            m = (1 + (k * phi)) // e
            break
    return m
a = '9162 552521 × 9280 550263 × 9590 766649 × 9715 617739 × 9842 950121 × 10294 998871 × 10831 489597 × 11090 899333 × 11430 581381 × 11441 108051 × 11643 762083 × 11939 421889 × 12024 699061 × 12067 222961 × 12331 363529 × 12602 394881 × 13133 647897 × 13621 079519 × 13943 919593 × 14479 978103 × 14908 985789 × 14951 381917 × 14999 562023 × 15050 671289 × 15125 409479 × 15233 629643 × 15486 103631 × 15682 938673 × 15772 453973 × 15858 663761 × 16528 395283 × 16638 930257 × 16960 869619 × 17168 669989'
a = a.replace(" ", "")
a = a.replace("×", " ")
a = a.split(" ")
phi = 1
for i in a:
    i = int(i)
    phi*=(i-1)
print(phi)
d = find_d_byphi(phi, e)
#
pt = hex(pow(c, d, n))
print(pt)
