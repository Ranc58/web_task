DRF tasks
=====================

DRF api with celery support for background tasks. Maximum number of tasks to be processed at the same time - 2. 

# How to install

1) With docker:
    - If it need - setup postgres and redis in `env/.env` file. By default, this file is configured for use with Docker.
    - `docker-compose up --build`.
    - For run tests `docker-compose exec app python3 manage.py test`. \
    Postgres data will be saved in `postgres/pgdata`
    
2) Without docker:
    - Recomended use venv or virtualenv for better isolation.\
      Venv setup example: \
      `python3 -m venv myenv`\
      `source myenv/bin/activate`
    - `cp env/.env src/;  cd src/`.
    - Setup postgres and redis in `.env` file.
    - `pip3 install -r requirements.txt`
    - Run django and celery `./run_server.sh`.
    - For run tests (from `src`) `python3 manage.py test`.
    
# How to use

1) Make `POST` request to `http://127.0.0.1:8000/a/v1/tasks/`. It will return something like `{"id":1}` and create background task.
2) Make `GET` request to `http://127.0.0.1:8000/a/v1/tasks/<TASK_ID>/` for get info about task. It will return something like
```{"status":"in queue","create_time":"18:52:23","start_time":null,"time_to_execute":null}```. 
    - `status`: May have values `in queue` (processing not started yet), `run` (processing has begun), `completed`(processing complete)
    - `create_time`: Time when task processing has been created.
    - `start_time`: Time when task processing has started.
    - `time_to_execute`: Time when task processing has finished.


 
