from domain.taxi import Taxi
from repo.taxi_repo import TaxiRepoException, TaxiRepo
from service.texi_service import TaxiService


def test_taxi():
    tx = Taxi(1,"Mihail Balanceanu",4,5)

    assert tx.getId() == 1
    assert tx.getX() == 4
    assert tx.getY() == 5

    assert str(tx) == '1 - Mihail Balanceanu - 4 - 5'


def test_repo():
    repo = TaxiRepo("TextRepo.txt")

    assert repo.getAll() == [Taxi(8,"",3,3),Taxi(13,"",2,2)]

    repo.modify(13, "Pula Mea ", 69, 69)

    try:
        repo.modify(11, "Pula Mea ", 69, 69)
        assert False
    except TaxiRepoException as tre:
        assert str(tre) == "Taxiul nu exista in repo!"


def test_service():
    repo = TaxiRepo("TextRepo.txt")
    serv = TaxiService(repo)

    serv.modifyTaxi(13,"DADA",2,2)

    try:
        serv.modifyTaxi(11, "Pula Mea ", 69, 69)
        assert False
    except TaxiRepoException as tre:
        assert str(tre) == "Taxiul nu exista in repo!"

    repo2 = TaxiRepo("TestRepo2.txt")
    serv = TaxiService(repo2)

    assert serv.getFromAdress("abc") == [Taxi(33,"",0,0),Taxi(13,"",0,0),Taxi(3,"",0,0)]

    assert serv.orderByDistance(4,4) == [Taxi(2,"",0,0),Taxi(5,"",0,0),Taxi(33,"",0,0),Taxi(3,"",0,0),Taxi(13,"",0,0),Taxi(8,"",0,0)]


def test_all():
    test_taxi()
    test_repo()
    test_service()