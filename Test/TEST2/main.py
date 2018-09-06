from UI.console import Console
from test.test import test_all
from service.ApartmentService import ApartmentService
from repo.ApartmentRepo import ApartmentRepo

test_all()


repo = ApartmentRepo("Apartamente.txt")
serv = ApartmentService(repo)
console = Console(serv)

console.run()
