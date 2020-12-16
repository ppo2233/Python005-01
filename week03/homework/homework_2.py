import datetime
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime

engine = create_engine("mysql+pymysql://root:root123@localhost:3306/testdb", echo=True)
metadata = MetaData(engine)


def create_user_table():
    """ 创建user表 """
    Table('user', metadata,
          Column('id', Integer, primary_key=True),
          Column('name', String(20)),
          Column('age', Integer),
          Column('birthday', DateTime),
          Column('sex', Integer, default=1),  # 1-男，2-女
          Column('education', String(20)),
          Column('created', DateTime, default=datetime.datetime.now()),
          Column('modified', DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
          )
    try:
        metadata.create_all()
    except Exception as e:
        print(f"create error {e}")


def use_user_table(sql):
    """ 插入user表 """
    db = pymysql.connect("localhost", "root", "root123", "testdb")
    try:
        # %s是占位符
        with db.cursor() as cursor:
            cursor.execute(sql)
        db.commit()

    except Exception as e:
        print(f"insert error {e}")

    finally:
        # 关闭数据库连接
        db.close()
        print(cursor.rowcount)


if __name__ == '__main__':
    # create_user_table()  # 创建用户表
    # sql = 'INSERT INTO user (id, name, age, sex) VALUES ("2", "wangshuai", "19", "1")'  # 插入数据
    sql = 'select * from user;'  # 查询数据
    use_user_table(sql)

    """
    week03>use testdb;
    Database changed
    week03>
    week03>
    week03>show tables;
    +------------------+
    | Tables_in_testdb |
    +------------------+
    | user             |
    +------------------+
    1 row in set (0.00 sec)
    
    week03>
    week03>
    week03>desc user;
    +-----------+-------------+------+-----+---------+----------------+
    | Field     | Type        | Null | Key | Default | Extra          |
    +-----------+-------------+------+-----+---------+----------------+
    | id        | int(11)     | NO   | PRI | NULL    | auto_increment |
    | name      | varchar(20) | YES  |     | NULL    |                |
    | age       | int(11)     | YES  |     | NULL    |                |
    | birthday  | datetime    | YES  |     | NULL    |                |
    | sex       | int(11)     | YES  |     | NULL    |                |
    | education | varchar(20) | YES  |     | NULL    |                |
    | created   | datetime    | YES  |     | NULL    |                |
    | modified  | datetime    | YES  |     | NULL    |                |
    +-----------+-------------+------+-----+---------+----------------+
    8 rows in set (0.00 sec)
    
    week03>select * from user;
    +----+-----------+------+----------+------+-----------+---------+----------+
    | id | name      | age  | birthday | sex  | education | created | modified |
    +----+-----------+------+----------+------+-----------+---------+----------+
    |  1 | lili      |   12 | NULL     |    2 | NULL      | NULL    | NULL     |
    |  2 | wangshuai |   19 | NULL     |    1 | NULL      | NULL    | NULL     |
    +----+-----------+------+----------+------+-----------+---------+----------+
    2 rows in set (0.00 sec)
    
    week03>
    
    """
