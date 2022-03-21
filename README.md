# Taxi service startproject

In this task you will start project `Taxi service`.

1. Create virtual environment, activate it and install django via pip. 
Remember: everything you will do in this project, do with activated virtual
environment.
2. Start project `taxi_service` inside the current directory (add `.` at the end
of the command). You should have such structure:
```
py-taxi-service
|-> venv
|-> manage.py
|-> taxi_service
    |-> __init__.py
    |-> settings.py
    ...
```
3. Inside `py-taxi-service` start application `taxi`. Don't forget to register
this app in settings.
4. Inside `taxi/models.py` create models according to this diagram:

![image](https://user-images.githubusercontent.com/80070761/159295912-d02c7080-09a7-41ec-aa86-b0ae3afdd75b.png)
5. You have noticed that `Driver` inherits from `AbstractUser`. It means that
standard `User` model should be replaced with the model `Driver`. Don't forget
to register it in settings.
6. Make migrations and migrate.
