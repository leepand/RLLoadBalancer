import os


class Config(object):
    SECRET_KEY = os.urandom(64).hex()

    # NGINX_PATH = '/usr/local/webserver/nginx/sbin/nginx'
    NGINX_PATH = '/usr/local/webserver/nginx/conf'
    # CONFIG_PATH = NGINX_PATH # os.path.join(NGINX_PATH, 'conf')
    CONFIG_PATH = os.path.join(NGINX_PATH, 'conf.d')

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


class WorkingConfig(Config):
    DEBUG = False


config = {
    'dev': DevConfig,
    'default': WorkingConfig
}
