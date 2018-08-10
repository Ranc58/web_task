DRF tasks
=====================

DRF api with celery support for background tasks. Maximum number of tasks to be processed at the same time - 2. 

# How to install

1) With docker:
    - If it need - setup postgres and redis in `env/.env` file. By default, this file is configured for use with Docker.
    - `docker-compose up --build`.
    - Run tests `docker-compose exec app python3 manage.py test`.
    Postgres data will be saved in `postgres/pgdata`
    
2) Without docker:
    - `cp env/.env src/;  cd src/`.
    - Setup postgres and redis in `.env` file.
    - Run django and celery `./run_server.sh`.
    - Run tests (from `src`) `python3 manage.py test`.
    
# How to use

1) Make `POST` request to `http://127.0.0.1:8000/a/v1/tasks/`. It will return something like `{"id":1}` and create background task.
2) Make `GET` request to `http://127.0.0.1:8000/a/v1/tasks/<TASK_ID>` for get info about task. It will return something like
`{"status":"in queue","create_time":"2018-08-10T18:52:23","start_time":null,"time_to_execute":null}`. \
    - `status`: May have values `in queue` (processing not started yet), `run` (processing has begun), `completed`(processing complete)
    - `create_time`: Time when task processing has been created.
    - `start_time`: Time when task processing has started.
    - `time_to_execute`: Time when task processing has finished.


 