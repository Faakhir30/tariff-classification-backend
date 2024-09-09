from .discriptionRouter import *


@router.delete("/{description_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_goods_description(
    description_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
    query = select(GoodsDescription).filter(
        GoodsDescription.description_id == description_id,
        GoodsDescription.user_id == current_user.user_id,
    )
    result = await db.execute(query)
    description = result.scalars().first()

    if not description:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Goods description not found."
        )

    await db.delete(description)
    await db.commit()
