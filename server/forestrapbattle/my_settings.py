DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'forest_1.0',
                # 로컬용
                # 'USER' : '',
                # 'PASSWORD' : '',
                # 'HOST' : '127.0.0.1',
                # 'PORT' : '3306',
                # 서버용
                'USER': '',
                'PASSWORD': '',
                'HOST' : 'k6e204.p.ssafy.io',
                'PORT' : '3306',
        }
}
SECRET_KEY = ''