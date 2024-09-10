from .searchRouter import *


@router.delete("/{result_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_search_result(
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

    await db.delete(search_result)
    await db.commit()

    return
