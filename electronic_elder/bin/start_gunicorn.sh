source /home/tran1l/Web_shop/env/bin/activate
exec gunicorn -c "/home/tran1l/Web_shop/electronic_elder/gunicorn_config.py" electronic_elder.wsgi 