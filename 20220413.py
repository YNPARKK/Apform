import sqlite3

# DB 생성
conn = sqlite3.connect("Apform.db")
# 커서 획득
cur=conn.cursor()

def create_table():
    global conn
    try:
        conn.execute('create table TDM_CMT_REC_REG (CMT_ID integer primary key autoincrement, DOC_NO text, DOC_REV text, CMT_PAGE integer, CMT_INDEX intiger, CMT_NO integer, CMT_REC_SERIAL text, CMT_CONTENT text, CMT_CONTENT_IMG blob')