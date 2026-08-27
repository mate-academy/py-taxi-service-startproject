# Taxi service startproject

In this task, you will start project `Taxi service`.

1. Create a virtual environment, activate it, and install django via pip:
```python
pip install django
```
**Remember**: everything you will do in this project, do with activated virtual
environment.

2. Start project `taxi_service` inside the current directory (add `.` at the end
of the command):
```python
django-admin startproject taxi_service .
```

You should have such structure:
```
py-taxi-service-startproject
|-> venv
|-> manage.py
|-> README.md
|-> taxi_service
    |-> __init__.py
    |-> settings.py
    ...
```
3. Inside `py-taxi-service-startproject` start application `taxi`:
```python
python manage.py startapp taxi
```

4. Inside `taxi/models.py` create models according to this diagram:

![image](https://user-images.githubusercontent.com/80070761/159295912-d02c7080-09a7-41ec-aa86-b0ae3afdd75b.png)

**Note**: `license_number` and `Manufacturer: name` fields should be unique.

5. You have noticed that `Driver` inherits from `AbstractUser`. It means that
the standard `User` model should be replaced with the model `Driver`. Notice, that
`Driver` has an additional field compared to the standard `User`.

6. Edit `admin.py`:
    - Register all your models in the admin.
    - Make Driver's field `license_number` displayed as the other fields. 
    - Add `license_number` to the `fieldsets` as `Additional info` 
category, so you can edit this field while updating `Driver`. 
    - Add `license_number` to the `add_fieldset` as `Additional info`
category, so you can fill this field while adding a driver.
    - Make it possible to search `Car` by `model`.
    - Make it possible to filter `Car` by `manufacturer`.

7. Make migrations and migrate.
8. Use `python manage.py test` to run tests.
9. Check that each of the html-files has a blank line at the end.
10. Don't forget add `.gitignore` file before pushing. Don't push a lot of extra files(`venv`, `pycache`, `.idea`, etc.).

### Note: Attach screenshots of all created or modified pages to pull request. 

1) Attach screenshots to the comment, NOT in commit. 
2) It's important to **attach images** not links to them. See example:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.



# Початок проєкту Taxi service

У цьому завданні ви розпочнете роботу над проєктом `Taxi service`.

1. Створіть віртуальне середовище, активуйте його та встановіть Django за допомогою pip:
```python
pip install django
```
**Пам’ятайте**: усі дії в цьому проєкті слід виконувати в активованому віртуальному середовищі.

2. Створіть проєкт `taxi_service` у поточній директорії (додайте `.` у кінці команди):
```python
django-admin startproject taxi_service .
```

Ви повинні отримати таку структуру:
```
py-taxi-service-startproject
|-> venv
|-> manage.py
|-> README.md
|-> taxi_service
    |-> __init__.py
    |-> settings.py
    ...
```
3. Усередині `py-taxi-service-startproject` створіть застосунок `taxi`:
```python
python manage.py startapp taxi
```

4. У файлі `taxi/models.py` створіть моделі відповідно до цієї діаграми:

![image](https://user-images.githubusercontent.com/80070761/159295912-d02c7080-09a7-41ec-aa86-b0ae3afdd75b.png)

**Примітка**: поля `license_number` та `Manufacturer: name` мають бути унікальними.

5. Ви помітили, що модель `Driver` успадковується від `AbstractUser`. Це означає, що стандартну модель `User` слід замінити на модель `Driver`. Зверніть увагу, що `Driver` має додаткове поле порівняно зі стандартною моделлю `User`.

6. Відредагуйте `admin.py`:
    - Зареєструйте всі свої моделі в адмін-панелі.
    - Налаштуйте відображення поля `license_number` моделі `Driver` так само, як і інших полів.
    - Додайте `license_number` до `fieldsets` у категорію `Additional info`, щоб це поле можна було редагувати під час оновлення даних водія (`Driver`).
    - Додайте `license_number` до `add_fieldset` у категорію `Additional info`, щоб це поле можна було заповнити під час додавання водія. - Реалізуйте можливість пошуку `Car` за `model`.
    - Реалізуйте можливість фільтрації `Car` за `manufacturer`.

7. Створіть та застосуйте міграції.
8. Використовуйте `python manage.py test` для запуску тестів.
9. Переконайтеся, що кожен HTML-файл має порожній рядок у кінці.
10. Не забудьте додати файл `.gitignore` перед виконанням `push`. Не надсилайте зайві файли (`venv`, `pycache`, `.idea` тощо).

### Примітка: Додайте скріншоти всіх створених або змінених сторінок до pull request.

1) Додавайте скріншоти до коментаря, а НЕ до коміту.
2) Важливо **прикріплювати зображення**, а не посилання на них. Дивіться приклад:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)

### Примітка: Перевірте свій код за допомогою цього [чек-листа](checklist.md) перед відправкою рішення.