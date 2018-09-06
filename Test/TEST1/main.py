from UI.PharmacyUI import PharmacyUI
from UI.PharmacyService import PharmacyService
from Repository.MedicineRepository import MedicineRepository

MedRepo = MedicineRepository("Medicine.txt")
PharmServ = PharmacyService(MedRepo)
PharmUI = PharmacyUI(PharmServ)

PharmUI.run()