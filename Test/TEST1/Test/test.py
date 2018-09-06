from Domain.Medicine import Medicine
from Domain.Recipe import Recipe
from Repository.MedicineRepository import MedicineRepository, MedicineRepositoryException
from UI.PharmacyService import PharmacyService

def test_Medicine():
    Med = Medicine("Un medicament tare", 35.34)

    assert Med.getName() == "Un medicament tare"
    assert Med.getPrice() == 35.34
    assert str(Med) == "Un medicament tare - 35.34 lei"


def test_Recipe():
    med1 = Medicine("M1", 5.3)
    med2 = Medicine("M2", 3.4)
    med3 = Medicine("M3", 1)

    Rec = Recipe([med1,med2,med3])

    assert Rec.getTotalSum() == 9.7
    assert str(Rec) == "M1 - 5.3 lei\nM2 - 3.4 lei\nM3 - 1 lei\nCost: 9.7\n"


def test_Repo():
    repo = MedicineRepository("Medicine.txt")

    assert repo.getByName("Prenti") == Medicine("Prenti",35.2)

    try:
        repo.getByName("Dadada")
        assert False
    except MedicineRepositoryException as mre:
        assert str(mre) == "Nu exista in repo!"


def test_PharmServ():
    repo = MedicineRepository("Medicine.txt")
    pServ = PharmacyService(repo)

    assert pServ.lookup("Prenti") == Medicine("Prenti", 35.2)

    try:
        pServ.lookup("Dadada")
        assert False
    except MedicineRepositoryException as mre:
        assert str(mre) == "Nu exista in repo!"

    assert str(pServ.create_recipe(["Pronto","Prenti"])) == "Pronto - 3.4 lei\nPrenti - 35.2 lei\nCost: 38.6\n"


def runAll():
    test_Medicine()
    test_Recipe()
    test_Repo()
    test_PharmServ()


runAll()