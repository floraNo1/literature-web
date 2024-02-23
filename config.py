SECRET_KEY = "asdzxcasdzxcvbnm;lf"

# 数据库的配置信息
HOSTNAME = '106.54.36.226'
PORT = '3306'
DATABASE = 'gdz'
USERNAME = 'gdz'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "3169912749@qq.com"
MAIL_PASSWORD = "wzexvydkmhdqdhde"
MAIL_DEFAULT_SENDER = "3169912749@qq.com"