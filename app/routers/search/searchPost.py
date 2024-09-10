from .searchRouter import *


@router.post(
    "/", response_model=SearchResultResponse, status_code=status.HTTP_201_CREATED
)
async def create_search_result(
    search_result_create: SearchRequestBase,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
    # Check if the associated GoodsDescription exists and belongs to the current user
    if isinstance(current_user, JSONResponse):
        return current_user
    description_query = select(GoodsDescription).filter(
        GoodsDescription.description_id == search_result_create.description
    )
    result = await db.execute(description_query)
    description = result.scalars().first()

    if description is None or description.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Goods description not found or not owned by you",
        )

    # Create the new search result
    new_search_result = SearchResult(
        description_id=search_result_create.description_id,
        hs_code=search_result_create.hs_code,
        similarity_score=search_result_create.similarity_score,
    )

    db.add(new_search_result)
    await db.commit()
    await db.refresh(new_search_result)

    return new_search_result
