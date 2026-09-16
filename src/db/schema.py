from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, UUID, Text

class Base(DeclarativeBase):
    pass

class ChatConversations(Base):
    __tablename__ = "chat_conversations"

    id: Mapped[str] = mapped_column(UUID(), primary_key=True)
    chat_id: Mapped[str] = mapped_column(String(length=100))
    content: Mapped[str] = mapped_column(Text())
    written_by:Mapped[str] = mapped_column(String(length=50))

class Chats(Base):
    __tablename__ = "chats"

    id: Mapped[str] = mapped_column(UUID(),primary_key=True)
    name: Mapped[str] = mapped_column(String(length=100))
    