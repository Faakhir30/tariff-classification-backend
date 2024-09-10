from .feedbackRouter import *


@router.post("/", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
async def create_feedback(
    feedback_create: FeedbackCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
    if isinstance(current_user, JSONResponse):
        return current_user

    # Check if the associated GoodsDescription exists and belongs to the current user
    description_query = select(GoodsDescription).filter(
        GoodsDescription.description_id == feedback_create.goods_description_id
    )
    result = await db.execute(description_query)
    description = result.scalars().first()

    if description is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Goods description not found"
        )

    # Create the new feedback
    new_feedback = Feedback(
        user_id=current_user.user_id,
        goods_description_id=feedback_create.goods_description_id,
        feedback_text=feedback_create.feedback_text,
        expected_values=feedback_create.expected_values,
    )

    db.add(new_feedback)
    await db.commit()
    await db.refresh(new_feedback)

    return new_feedback
