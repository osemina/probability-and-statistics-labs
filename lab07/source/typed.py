"""Exactly what is typed into each yellow cell: numbers directly, no cell references and no locking."""

TYPED = {
    1: dict(zc='=NORM.S.INV(1-0.05/2)', se='=1.2/SQRT(40)', z='=(6.6-7)/(1.2/SQRT(40))', p='=2*NORM.S.DIST(-2.108,TRUE)'),
    2: dict(zc='=NORM.S.INV(0.90)', se='=10/SQRT(64)', z='=(53.1-52)/(10/SQRT(64))', p='=1-NORM.S.DIST(0.88,TRUE)'),
    3: dict(zc='=NORM.S.INV(1-0.05/2)', se='=0.8/SQRT(100)', z='=(2.82-3)/(0.8/SQRT(100))', p='=2*NORM.S.DIST(-2.25,TRUE)'),
    4: dict(df='=25-1', tc='=T.INV.2T(0.05,24)', se='=15.4/SQRT(25)', t='=(172.5-168)/(15.4/SQRT(25))', p='=T.DIST.2T(1.461,24)'),
    5: dict(p='=57/150', c1='=150*0.3', c2='=150*(1-0.3)', zc='=NORM.S.INV(0.95)', se='=SQRT(0.3*0.7/150)',
            z='=(0.38-0.3)/SQRT(0.3*0.7/150)', pv='=1-NORM.S.DIST(2.138,TRUE)'),
    6: dict(zc='=-NORM.S.INV(0.95)', se='=1800/SQRT(36)', z='=(7350-8000)/(1800/SQRT(36))', p='=NORM.S.DIST(-2.167,TRUE)'),
    7: dict(p='=21/200', c1='=200*0.08', c2='=200*(1-0.08)', zc='=NORM.S.INV(0.99)', se='=SQRT(0.08*0.92/200)',
            z='=(0.105-0.08)/SQRT(0.08*0.92/200)', pv='=1-NORM.S.DIST(1.303,TRUE)', zc10='=NORM.S.INV(0.90)'),
    8: dict(df='=25-1', tc='=T.INV.2T(0.10,24)', se='=0.9/SQRT(25)', t='=(3.4-3)/(0.9/SQRT(25))', p='=T.DIST.2T(2.222,24)'),
}
