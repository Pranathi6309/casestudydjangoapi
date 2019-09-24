from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


class projects(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    projectName = fields.StringField(max_length=255, required=False)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()


class skills(EmbeddedDocument):
    technology = fields.StringField(max_length=10, required=True, null=False)
    experience = fields.IntField()
    level = fields.StringField(max_length=255, required=False)
    

class Employee(Document):
    employeeId = fields.StringField(max_length=10, required=True, null=False)
    employeeName = fields.StringField(max_length=100, required=True)
    workLocation = fields.StringField(max_length=100, required=True)
    skills = fields.EmbeddedDocumentListField(skills)
    projects= fields.EmbeddedDocumentListField(projects)