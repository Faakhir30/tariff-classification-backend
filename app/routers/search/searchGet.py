from .searchRouter import *


@router.get("/{result_id}", response_model=SearchResultResponse)
async def read_search_result(
    result_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
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
