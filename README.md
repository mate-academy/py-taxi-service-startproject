# Taxi service startproject

In this task, you will start project `Taxi service`.

1. Create a virtual environment, activate it, and install django via pip. 
Remember, everything you will do in this project, do with activated virtual
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
3. Inside `py-taxi-service` start application `taxi`.
4. Inside `taxi/models.py` create models according to this diagram:

![image](https://user-images.githubusercontent.com/80070761/159295912-d02c7080-09a7-41ec-aa86-b0ae3afdd75b.png)

Note: `licence_number` and `Manufacturer: name` fields should be unique.

5. You have noticed that `Driver` inherits from `AbstractUser`. It means that
the standard `User` model should be replaced with the model `Driver`. Notice, that
`Driver` has an additional field compared to the standard `User`. To make correct model name display in the admin, 
add `verbose_name` and `verbose_name_plural` inside `Driver` model.

6. Edit `admin.py`:
    - Register all your models in the admin. 
    - Make Driver's field `licence_number` be 
displayed as the other field. 
    - Add `licence_number` to the `fieldsets`, so you
can edit this field while updating `Driver`. 
    - Add `licence_number` to the 
`add_fieldset` so you can fill this field while adding a driver.
    - Make it possible to search `Car` by `model`.
    - Make it possible to filter `Car` by `manufacturer`.

7. Make migrations and migrate.

NOTE: Attach screenshots of all created pages on admin panel to pull request. It's important to attach images not links to them. See example:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)
