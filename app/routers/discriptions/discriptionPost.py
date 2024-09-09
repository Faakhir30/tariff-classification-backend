from .discriptionRouter import *


@router.post(
    "/", response_model=GoodsDescriptionResponse, status_code=status.HTTP_201_CREATED
)
async def create_goods_description(
    goods_desc_create: GoodsDescriptionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
    new_description = GoodsDescription(
        user_id=current_user.user_id,
        description_text=goods_desc_create.description_text,
    )
    db.add(new_description)
    try:
        await db.commit()
        await db.refresh(new_description)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create goods description.",
        )
    return new_description
