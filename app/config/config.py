class Config:

    SECRET_KEY = "clave_super_secreta"

    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    SESSION_FILE_DIR = "./.flask_session"