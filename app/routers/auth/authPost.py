from app.schemas import UserLogin
from .authRouter import *


@router.post(
    "/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def signup(user_create: UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if the username or email is already taken
    query = select(User).filter(
        (User.username == user_create.username) | (User.email == user_create.email)
    )
    result = await db.execute(query)
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered",
        )

    # Hash the password
    hashed_password = hash_password(user_create.password)

    # Create new user instance
    new_user = User(
        username=user_create.username,
        email=user_create.email,
        password_hash=hashed_password,
        role=user_create.role,
    )

    # Save to the database
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


@router.post("/login")
async def login(user_create: UserLogin, db: AsyncSession = Depends(get_db)):
    query = select(User).filter(User.email == user_create.email)
    result = await db.execute(query)
    user = result.scalars().first()

    if not user or not verify_password(user_create.password, user.password_hash):
        return response(401, "Invalid email or password")

    # Generate JWT token
    token = create_access_token(data={"id": str(user.user_id), "role": user.role.value})

    return response(
        200, "Login successful", data={"access_token": token, "token_type": "bearer"}
    )
