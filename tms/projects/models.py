# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    id = models.IntegerField()
    projectid = models.IntegerField(db_column='ProjectId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=2500)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    departementid = models.IntegerField(db_column='DepartementId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    assigndate = models.DateTimeField(db_column='AssignDate')  # Field name made lowercase.
    realstartdate = models.DateTimeField(db_column='RealStartDate')  # Field name made lowercase.
    finishby = models.IntegerField(db_column='FinishBy')  # Field name made lowercase.
    finishdate = models.DateTimeField(db_column='FinishDate')  # Field name made lowercase.
    cancelby = models.IntegerField(db_column='CancelBy')  # Field name made lowercase.
    canceldate = models.DateTimeField(db_column='CancelDate')  # Field name made lowercase.
    closeby = models.IntegerField(db_column='CloseBy')  # Field name made lowercase.
    closedate = models.DateTimeField(db_column='CloseDate')  # Field name made lowercase.
    closereson = models.CharField(db_column='CloseReson', max_length=500)  # Field name made lowercase.
    lastedit = models.DateTimeField(db_column='LastEdit')  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'


class Project(models.Model):
    id = models.IntegerField()
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.
    start = models.DateField(db_column='Start')  # Field name made lowercase.
    end = models.DateField()
    teamname = models.CharField(db_column='TeamName', max_length=100)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=250)  # Field name made lowercase.
    creationby = models.CharField(db_column='CreationBy', max_length=20)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    departementid = models.IntegerField(db_column='DepartementId')  # Field name made lowercase.
    statusid = models.IntegerField(db_column='StatusId')  # Field name made lowercase.
    openby = models.CharField(db_column='OpenBy', max_length=20)  # Field name made lowercase.
    opendate = models.DateTimeField(db_column='OpenDate', blank=True, null=True)  # Field name made lowercase.
    closedby = models.CharField(db_column='ClosedBy', max_length=20)  # Field name made lowercase.
    closeddate = models.DateTimeField(db_column='ClosedDate', blank=True, null=True)  # Field name made lowercase.
    cancelby = models.CharField(db_column='CancelBy', max_length=20)  # Field name made lowercase.
    canceldate = models.DateTimeField(db_column='CancelDate', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class Department(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    managerid = models.CharField(db_column='ManagerId', max_length=45, blank=True, null=True)  # Field name made lowercase.
    depcode = models.IntegerField(db_column='DepCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=45, blank=True, null=True)  # Field name made lowercase.
    depcode = models.CharField(db_column='DepCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    depname = models.CharField(db_column='DepName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ismanager = models.CharField(db_column='IsManager', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ext = models.CharField(db_column='Ext', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class TaskStatus(models.Model):
    id = models.IntegerField()
    name = models.IntegerField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task_status'


class ProjectStatus(models.Model):
    id = models.IntegerField()
    name = models.IntegerField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_status'
