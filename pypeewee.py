from peewee import *

db = SqliteDatabase('people.db')  # SQLite 데이터베이스 생성

class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db  # 테이블과 데이터베이스 연결

db.connect()
db.create_tables([Person])  # 테이블 생성하기

alice = Person(name='Alice', age=30)
alice.save()  # 데이터를 데이터베이스에 저장

persons = [Person(name='Bob', age=25), Person(name='Charlie', age=35)]
Person.bulk_create(persons)  # 여러 데이터를 한번에 데이터베이스에 저장

result = Person.select().where(Person.age >= 30)
for person in result:
    print(person.name, person.age)

person_to_update = (Person
                    .select()
                    .where(Person.name == 'Alice')
                    .get())  # get() 메소드는 한 개의 데이터를 가져옵니다

person_to_update.age = 32
person_to_update.save()  # 데이터베이스에 값 업데이트

person_to_delete = (Person
                    .select()
 .where(Person.name == 'Charlie')
                    .get())  # 삭제할 데이터 선택

person_to_delete.delete_instance()  # 데이터 삭제

db.close()