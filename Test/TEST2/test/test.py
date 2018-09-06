from domain.apartment import Apartment
from domain.Bill import Bill
from repo.ApartmentRepo import ApartmentRepoException, ApartmentRepo
from service.ApartmentService import ApartmentService

def test_Apartment():
    ap = Apartment(13,"Roatis",3)

    assert ap.getNrAp() == 13
    assert ap.getNrLoc() == 3
    assert ap.getNumeFam() == "Roatis"

def test_Bill():
    bil = Bill(Apartment(13,"Roatis",3),3,7,100)

    assert bil.getApartment() == Apartment(13,"Roatis",3)
    assert bil.getGas() == 7
    assert bil.getWater() == 3
    assert bil.getIntret() == 100
    assert bil.getSumTotal() == 185

def test_repo():
    repo = ApartmentRepo("Apartamente2.txt")

    assert repo.findByNr(8) == Apartment(8,"Bodean",3)

    try:
        ah = repo.findByNr(3)
        assert False
    except ApartmentRepoException as are:
        assert str(are) == "Apartamentul nu exista in repo!"

    assert repo.getAll() == [Apartment(13,"Poescu",3),Apartment(2,"Roatis",2),Apartment(8,"Bodean",3)]

def test_service():
    repo = ApartmentRepo("Apartamente2.txt")
    svc = ApartmentService(repo)

    assert svc.sortByFamilyName() == [Apartment(8,"",2),Apartment(13,"",2),Apartment(2,"",2)]

    assert str(svc.plata(8,5,7,100)) == "Cost: 195"


def test_all():
    test_Apartment()
    test_Bill()
    test_repo()
    test_service()