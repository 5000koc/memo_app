class Config :
    # DB 관련 정보
    HOST = 'yhstudydb.cxqwomk3krwg.ap-northeast-2.rds.amazonaws.com'
    DATABASE = 'memo_db'
    DB_USER = 'memo_db_user'
    DB_PASSWORD= '1234'
    
    # 비밀번호 암호화
    SALT = '0619#hiyo'

    # JWT 환경 변수 셋팅
    JWT_SECRET_KEY = 'hot6@yo'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True