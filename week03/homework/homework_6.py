import datetime
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime, ForeignKey

engine = create_engine("mysql+pymysql://root:root123@localhost:3306/testdb", echo=True)
metadata = MetaData(engine)


def create_tables():
    """ 创建数据库表 """
    Table('transfer_user', metadata,  # 转账用户表
          Column('id', Integer, primary_key=True),
          Column('name', String(20))
          )

    Table('transfer_assert', metadata,  # 转账资产表
          Column('id', Integer, primary_key=True),
          Column('user', None, ForeignKey('transfer_user.id')),
          Column('assert', Integer)
          )

    Table('transfer_audit', metadata,  # 转账审计表
          Column('id', Integer, primary_key=True),
          Column('user_provide', Integer),  # 转出者
          Column('user_accept', Integer),  # 传入者
          Column('created', DateTime, default=datetime.datetime.now())  # 审计创建时间
          )
    try:
        metadata.create_all()
    except Exception as e:
        print(f"create error {e}")


def init_user_assert_data(sql):
    """ 初始化用户资产数据 """
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


def perform():
    """ 开始转账 """
    db = pymysql.connect("localhost", "root", "root123", "testdb")
    try:
        with db.cursor() as cursor:
            sql1 = 'update transfer_assert set assert=assert-100 where id=1;'
            sql2 = 'update transfer_assert set assert=assert+100 where id=2;'
            sql3 = f'INSERT INTO transfer_audit VALUES(1, 1, 2, "{datetime.datetime.now()}")'
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
        db.commit()

    except Exception as e:
        print(f"insert error {e}")

    finally:
        # 关闭数据库连接
        db.close()
        print(cursor.rowcount)


if __name__ == '__main__':
    # create_tables()  # 创建数据库表
    sqls = [
        'INSERT INTO transfer_user VALUES(1, "zhangsan");',
        'INSERT INTO transfer_user VALUES(2, "lisi");',
        'INSERT INTO transfer_assert VALUES(1, 1, 230);',
        'INSERT INTO transfer_assert VALUES(2, 2, 130);',
    ]
    # for sql in sqls:
    #     init_user_assert_data(sql)  # 初始化用户资产数据sql
    perform()  # 开始转账
