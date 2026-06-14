import mysql.connector

conexao = mysql.connector.connect(
    host="mysql-34bfce49-poo-pi.c.aivencloud.com",
    port="17819",
    user="avnadmin",
    password="AVNS_7mkGmMRCU5OtlEqgiMB",
    database="domino_quimico",
    ssl_disabled=False
)
cursor = conexao.cursor()
