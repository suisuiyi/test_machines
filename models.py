#encoding: utf-8

from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)


class Machine(db.Model):
    __tablename__ = 'machine'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #管理人id 与 User表关联
    custodian_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #管理人
    custodian = db.relationship('User', backref=db.backref('machines'))
    #借出人
    lender = db.Column(db.String(20), default='--')
    #0代表空闲中，1代表使用中
    status = db.Column(db.Integer, nullable=False, default=0)

    #测试机相关属性
    name = db.Column(db.String(30), nullable=False)
    #0代表苹果，1代表安卓，2代表其他
    operating_system = db.Column(db.String(20), nullable=False)
    #操作系统版本号
    operating_system_version = db.Column(db.String(20), nullable=False)
    #0代表白色，1代表黑色，2代表金色，3代表其他颜色
    color = db.Column(db.Integer, nullable=False)

    #添加机器的时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    #修改机器的时间
    update_time = db.Column(db.DateTime, default=datetime.now)