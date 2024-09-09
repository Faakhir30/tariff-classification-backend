from .searchRouter import *


@router.put("/{result_id}", response_model=SearchResultResponse)
async def update_search_result(
    result_id: UUID,
    search_result_update: SearchResultBase,
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

    # Update the search result
    search_result.hs_code = search_result_update.hs_code
    search_result.similarity_score = search_result_update.similarity_score

    await db.commit()
    await db.refresh(search_result)

    return search_result
