* ### Для запуска проекта через docker вместе со всеми сопутствующими службами выполнить команду:
  #### - *docker-compose up -d --build*
---
* ### Для ручного запуска каждой службы и проекта отдельно: 
  #### - Заменить значение строки DATABASES -> HOST в файле [setting.py](https://github.com/DaniilMashkov/drf_test/blob/main/config/settings.py) на 127.0.0.1 
  - **Выполнить команды:**
      - docker run --name db -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=db -dp 5432:5432 -v <path_for_db>:/var/lib/postgresql/data postgres
      - docker run --name redis -dp 6379:6379 redis
      - docker run -it -v <path_to_project>:/drf_test python bash
      - cd drf_test/
      - source env/bin/activate
      - pip install -r requirements.txt 
      - python manage.py runserver
