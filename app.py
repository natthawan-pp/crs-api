from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import mysql.connector
from connection import *
from knowledge_data import *
from predict_data import *
from skill_major_data import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
host = "localhost"
user = "root"
password = "admin"
db = "crsdb"
# set FLASK_APP=app
# set FLASK_ENV=development
# flask run

######################## crs-basic-subject-master ########################


@app.route("/api/crs-basic-subject-master/getAll")
def getAllCrsBasicSubjectMaster():
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from crs_basic_subject_master")
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-basic-subject-master/getByRowId/<rowId>")
def getCrsBasicSubjectMasterByRowId(rowId):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_basic_subject_master where row_id = %s"
    val = (rowId,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-basic-subject-master/getBySubjectLevel/<subjectLevel>")
def getCrsBasicSubjectMasterBySubjectLevel(subjectLevel):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_basic_subject_master where subject_level = %s"
    val = (subjectLevel,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-basic-subject-master/getByParentRowId/<parentRowId>")
def getCrsBasicSubjectMasterByParentRowId(parentRowId):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_basic_subject_master where parent_row_id = %s"
    val = (parentRowId,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-basic-subject-master/getBySubjectNameEn/<subjectNameEn>")
def getCrsBasicSubjectMasterBySubjectNameEn(subjectNameEn):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_basic_subject_master where subject_name_en = %s"
    val = (subjectNameEn,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-basic-subject-master/getBySubjectNameTh/<subjectNameTh>")
def getCrsBasicSubjectMasterBySubjectNameTh(subjectNameTh):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_basic_subject_master where subject_name_th = %s"
    val = (subjectNameTh,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


######################## crs-skill-base-master ########################

@app.route("/api/crs-skill-base-master/getAll")
def getAllCrsSkillBaseMaster():
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from crs_skill_base_master")
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-skill-base-master/getByRowId/<rowId>")
def getCrsSkillBaseMasterByRowId(rowId):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_skill_base_master where row_id = %s"
    val = (rowId,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("//api/crs-skill-base-master/getBySkillBaseLevel/<skillBaseLevel>")
def getCrsSkillBaseMasterBySkillBaseLevel(skillBaseLevel):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_skill_base_master where subject_level = %s"
    val = (skillBaseLevel,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("//api/crs-skill-base-master/getByParentRowId/<parentRowId>")
def getCrsSkillBaseMasterByParentRowId(parentRowId):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_skill_base_master where parent_row_id = %s"
    val = (parentRowId,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("//api/crs-skill-base-master/getBySkillBaseNameEn/<skillBaseNameEn>")
def getCrsSkillBaseMasterBySkillBaseNameEn(skillBaseNameEn):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_skill_base_master where skill_base_name_en = %s"
    val = (skillBaseNameEn,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("//api/crs-skill-base-master/getBySkillBaseNameTh/<skillBaseNameTh>")
def getCrsSkillBaseMasterBySkillBaseNameTh(skillBaseNameTh):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_skill_base_master where skill_base_name_th = %s"
    val = (skillBaseNameTh,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)

######################## crs-personality-master ########################


@app.route("//api/crs-personality-master/getAll")
def getAllCrsPersonalityMaster():
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from crs_personality_master")
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("//api/crs-personality-master/getByRowId/<rowId>")
def getCrsPersonalityMasterByRowId(rowId):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_personality_master where row_id = %s"
    val = (rowId,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-personality-master/getByPersonalityGroupLevel/<personalityGroupLevel>")
def getCrsPersonalityMasterByPersonalityLevel(personalityGroupLevel):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_personality_master where personality_group_level = %s"
    val = (personalityGroupLevel,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-personality-master/getByParentRowId/<parentRowId>")
def getCrsPersonalityMasterByParentRowId(parentRowId):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_personality_master where parent_row_id = %s"
    val = (parentRowId,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-personality-master/getBypersonalityNameEn/<personalityNameEn>")
def getCrsPersonalityMasterByPersonalityNameEn(personalityNameEn):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_personality_master where personality_name_en = %s"
    val = (personalityNameEn,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)


@app.route("/api/crs-personality-master/getByPersonalityNameTh/<personalityNameTh>")
def getCrsPersonalityMasterByPersonalityNameTh(personalityNameTh):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "select * from crs_personality_master where personality_name_th = %s"
    val = (personalityNameTh,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)

######################## predict data section ########################


@app.route("/api/predict-data", methods=['POST'])
def getPredictData():
    dataSet1 = []
    dataSet2 = []
    data_json = request.get_json()
    data1 = data_json['dataSetBasicSubject']
    data2 = data_json['dataSetSkillBase']

    for i in range(len(data1)):
      dataSet1.append(data1[i])

    for j in range(len(data2)):
      dataSet2.append(data2[j])
    print(dataSet1)
    print(dataSet2)
    v = PredictData(dataSet1)
    y = SkillMajor(dataSet2)
    json_result = {
          "subject_request_data_cs": v.subject_request_data[0],
          "major_percentage_cs": v.major_percentage[0],
          "subject_request_data_it": v.subject_request_data[1],
          "major_percentage_it": v.major_percentage[1],
          "subject_request_data_ce": v.subject_request_data[2],
          "major_percentage_ce": v.major_percentage[2],
          "subject_request_data_se": v.subject_request_data[3],
          "major_percentage_se": v.major_percentage[3],
          "subject_request_data_bc": v.subject_request_data[4],
          "major_percentage_bc": v.major_percentage[4],
          "major_job_result": v.major_job_result,
          "skill_request_cs": y.skill_Request[0],
          "skill_percentage_cs": y.skill_Percentage[0],
          "skill_request_it": y.skill_Request[1],
          "skill_percentage_it": y.skill_Percentage[1],
          "skill_request_ce": y.skill_Request[2],
          "skill_percentage_ce": y.skill_Percentage[2],
          "skill_request_se": y.skill_Request[3],
          "skill_percentage_se": y.skill_Percentage[3],
          "skill_request_bc": y.skill_Request[4],
          "skill_percentage_bc": y.skill_Percentage[4],
        }
    # print(json_result)
    return make_response(jsonify(json_result), 200)
