from models import Package, Package
from .base import CRUDBase
from schemas.packages import PackageCreate


class CRUDPackage(CRUDBase[Package, PackageCreate, None]):
    pass


package = CRUDPackage(Package)
