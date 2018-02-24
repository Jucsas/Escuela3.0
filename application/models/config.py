import web

db_host = 'gx97kbnhgjzh3efb.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'ijaig693dd9sx294'
db_user = 'dimtxi0vazfyfyca'
db_pw = 'pq6zlycvmv1ax4ck'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )