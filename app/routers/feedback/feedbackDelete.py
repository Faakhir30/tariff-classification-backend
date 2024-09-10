from .feedbackRouter import *


@router.delete("/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_feedback(
    feedback_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(auth_dep),
):
    if isinstance(current_user, JSONResponse):
        return current_user
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

    await db.delete(feedback)
    await db.commit()

    return
