from .feedbackRouter import *


@router.get("/{feedback_id}", response_model=FeedbackResponse)
async def read_feedback(
    feedback_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
    query = select(Feedback).filter(Feedback.feedback_id == feedback_id)
    result = await db.execute(query)
    feedback = result.scalars().first()

    if feedback is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feedback not found"
        )

    # Ensure the feedback is associated with the current user
    if feedback.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access to this feedback is forbidden",
        )

    return feedback


@router.get("/", response_model=List[FeedbackResponse])
async def get_all_feedback(
    db: AsyncSession = Depends(get_db), current_user: User = Depends(auth_dep)
):
    # Check if the current user is an admin
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Admins only",
        )

    query = select(Feedback)
    result = await db.execute(query)
    feedbacks = result.scalars().all()

    return feedbacks
