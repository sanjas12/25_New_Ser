from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Создаем соединение с базой данных (в данном случае SQLite)
engine = create_engine('sqlite:///database/mydatabase.db', echo=True)

# Создаем базовый класс для объявления моделей
Base = declarative_base()


class Title(Base):
    __tablename__ = 'news'
    # __table_args__ = {'mysql_engine':'InnoDB'}

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    title = Column(String(100), unique=True)
    content = Column(String(100), unique=False)
    timestamp = Column(String(100), unique=True)

# Создаем таблицу в базе данных
Base.metadata.create_all(engine)

class DbSession:
    def __init__(self):
        pass
    
    def __enter__(self)-> None:
        self.connection = engine.connect()
        self.session = scoped_session(sessionmaker(
                                        autocommit=False,
                                        autoflush=False,
                                        bind=engine)
                                        )
        return self.session

    def __exit__(self, exc_type, value, traceback):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.connection.close()

    def __repr__(self):
            return f"<News(id={self.id}, title={self.title}, content={self.content})>"

if __name__ == "__main__":
    with DbSession() as db_session:
        # Perform database operations using db_session
        news_entry = Title(title='Биржа поддержала миноритариев в споре из-за незаконной приватизации',
                           content='Example Content',
                           timestamp='Mon Dec  0 15:45:39 2023') 
        
        news_entry_2 = Title(title='поддержала миноритариев в споре из-за незаконной приватизации',
                           content='Content',
                           timestamp='Mon Dec  10 12:45:59 2023')
        
        db_session.add(news_entry)
        db_session.add(news_entry_2)