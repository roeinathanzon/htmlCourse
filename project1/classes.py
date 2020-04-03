import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__="courses"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False, unique=True)
    password=db.Column(db.String, nullable=False)
    students = db.relationship("Student", backref='course', lazy=True)

    def add_student(self,name,username,password):
        s = Student(name=name,username=username,password=password,course_id=self.id)
        db.session.add(s)
        db.session.commit()
                               
class Student(db.Model):
    __tablename__ = "students"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    username=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)

class State:
    def __init__(self,name,isAccept):
        self.name=name
        self.isAccept=isAccept
        self.links={}

class Dfa:
    def __init__(self,data):
        self.nodes=[]
        if(data.get('nodes')):
            for node in data.get('nodes'):
                self.nodes.append(State(node['text'],node['isAcceptState']))
        if(data.get('links')):
            for link in data.get('links'):
                if(link['type']=='Link'):
                    for var in link['text'].split(','):
                        self.nodes[link['nodeA']].links[var]=self.nodes[link['nodeB']]
                elif(link['type']=='SelfLink'):
                    for var in link['text'].split(','):
                        self.nodes[link['node']].links[var]=self.nodes[link['node']]
                    
    def run(self,word):
        currNode=self.nodes[0]
        for st in word:
            if(not currNode.links.get(st)):
                return False
            currNode=currNode.links.get(st)
        return currNode.isAccept




            












                
        
