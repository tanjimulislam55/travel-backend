from typing import List
from fastapi import APIRouter, Depends, status, Response

from schemas.packages import PackageCreate, PackageOut
from models import User
from api.dependencies import get_current_user
from crud.packages import package

router = APIRouter()


@router.get("/", response_model=List[PackageOut], status_code=status.HTTP_200_OK)
async def get_multiple_packages(
    skip: int = 0,
    limit: int = 10,
):
    return await package.get_many(skip, limit)


@router.post("/", response_model=PackageOut, status_code=status.HTTP_201_CREATED)
async def add_new_package(
    package_in: PackageCreate,
    current_user: User = Depends(get_current_user),
):
    new_generated_id = await package.create(package_in)
    return {**package_in.dict(), "id": new_generated_id}


@router.delete("/{package_id}", status_code=status.HTTP_202_ACCEPTED)
async def remove_package(
    package_id: int, current_user: User = Depends(get_current_user)
):
    if not await package.get_one(package_id):
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    await package.remove(package_id)
    return {"message": "deleted successfully"}
