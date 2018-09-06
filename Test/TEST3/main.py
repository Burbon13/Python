from test.test import test_all
from repo.taxi_repo import TaxiRepo
from service.texi_service import TaxiService
from UI.console import ConsoleUI


repo = TaxiRepo("TaxisRepo.txt")
serv = TaxiService(repo)
console = ConsoleUI(serv)

#test_all()
console.run()