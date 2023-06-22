# !! -- 필수파일 -- !!
# !! -- ./people.db -- !!

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 예제 1. 데이터베이스 연결 및 베이스 모델 생성
engine = create_engine('sqlite:///people.db')
Base = declarative_base()

# 예제 2. 테이블 정의
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 데이터베이스에 테이블 생성
Base.metadata.create_all(engine)

# 예제 3. 세션 및 CRUD 작업
Session = sessionmaker(bind=engine)
session = Session()

#자 생성 및 저장
user1 = User(name="John Doe", age=30)
session.add(user1)
session.commit()

# 사용자 조회
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

# 사용자 수정 및 삭제
user_to_update = session.query(User).filter(User.name == "John Doe").first()
user_to_update.age = 35
session.commit()

user_to_delete = session.query(User).filter(User.name == "John Doe").first()
session.delete(user_to_delete)
session.commit()

# 세션 닫기
session.close()
