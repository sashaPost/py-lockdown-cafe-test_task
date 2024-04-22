class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self):
        super().__init__("Visitor is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self):
        super().__init__("Visitor's vaccine is expired.")


class NotWearingMaskError(Exception):
    def __init__(self):
        super().__init__("Visitor is not wearing a mask.")
