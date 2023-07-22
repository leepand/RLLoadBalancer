# which gunicorn
sudo ~/miniconda3/bin/gunicorn -w 4 -b 0.0.0.0:8906 'wsgi:create_app()'

