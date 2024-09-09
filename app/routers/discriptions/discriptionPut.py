from .discriptionRouter import *


@router.put("/{description_id}", response_model=GoodsDescriptionResponse)
async def update_goods_description(
    description_id: UUID,
    goods_desc_update: GoodsDescriptionUpdate,
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

    description.description_text = goods_desc_update.description_text
    await db.commit()
    await db.refresh(description)
    return description
