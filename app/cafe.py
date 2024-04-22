from .errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)

import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor):
        if "vaccine" not in visitor:
            raise NotVaccinatedError()

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError()

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError()

        return (
            f"Welcome to {self.name}"
        )
