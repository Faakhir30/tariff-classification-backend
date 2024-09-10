from typing import List

from app.models import UserRole
from .searchRouter import *


@router.get("/{result_id}", response_model=SearchResultResponse)
async def read_search_result(
    result_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
    if isinstance(current_user, JSONResponse):
        return current_user
    query = select(SearchResult).filter(SearchResult.result_id == result_id)
    result = await db.execute(query)
    search_result = result.scalars().first()

    if search_result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Search result not found"
        )

    # Check if the associated GoodsDescription belongs to the current user
    description_query = select(GoodsDescription).filter(
        GoodsDescription.description_id == search_result.description_id
    )
    result = await db.execute(description_query)
    description = result.scalars().first()

    if description.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access to this search result is forbidden",
        )

    return search_result


@router.get("/", response_model=List[SearchResultResponse])
async def get_all_search_results(
    db: AsyncSession = Depends(get_db), current_user: User = Depends(auth_dep)
):
    if isinstance(current_user, JSONResponse):
        return current_user
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Admins only",
        )

    query = select(SearchResult)
    result = await db.execute(query)
    search_results = result.scalars().all()

    return search_results
