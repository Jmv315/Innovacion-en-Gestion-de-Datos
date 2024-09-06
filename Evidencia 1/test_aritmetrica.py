from aritmetrica import suma, resta, por, div
def test_suma():
    assert suma(2, 5)==7
    assert suma(5, 6)==11
    assert suma(9, 123)==132
def test_resta():
    assert resta(4, 7)==-3
    assert resta(56, 123)==-67
    assert resta(45, 64)==-19
def test_por():
    assert por(23, 512)==11776
    assert por(54, 67)==3618
    assert por(32, 76)==2432
def test_div():
    assert div(23, 2)==11.5
    assert div(45, 4)==11.25
    assert div(123, 5)==24.6
if __name__ == "__main__":
    test_suma()
    test_resta()
    test_por()
    test_div()
    print("Todas las pruebas pasaron correctamente.")