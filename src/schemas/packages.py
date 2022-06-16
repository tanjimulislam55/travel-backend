from typing import Union
from pydantic import BaseModel
from datetime import date


class PackageCreate(BaseModel):
    package_class: str
    description: str
    for_days: int
    is_tax_included: Union[bool, None]
    location: Union[str, None]
    place: Union[str, None]
    price_for_child_3_t_6: Union[int, None]
    price_for_child_7_t_12: Union[int, None]
    price_for_double: Union[int, None]
    price_for_infant: Union[int, None]
    price_for_single: Union[int, None]
    price_for_triple: Union[int, None]
    valid_from: date
    valid_to: date


class PackageOut(PackageCreate):
    id: int

    class Config:
        orm_mode = True
