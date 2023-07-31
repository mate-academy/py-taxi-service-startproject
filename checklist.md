# Сheck Your Code Against the Following Points

## Don't forget to add `.gitignore` file BEFORE pushing
Make sure you don't push db files (files with `.sqlite`, `.db3`, etc. extension).

## Don't Forget to Add Migrations to your PR
This is a required for the tests to pass.

## Code Style
1. Implement `Meta` class only after you defined all attributes.

Good example:
```python
class Order(models.Model):
    created_at = ...
    user = ...

    class Meta:
        pass
```

Bad example:
```python
class Order(models.Model):
    created_at = ...

    class Meta:
        pass    

    user = ...
```

2. Use `AUTH_USER_MODEL` instead of `User`, it is the best practice.

Good example:
```python
from django.conf import settings


class Order(models.Model):
    customer = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

Bad example:
```python
class Order(models.Model):
    customer = models.ManyToManyField(User)
```

3. Don't overuse f-string.

Good example:
```python
class Player(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name
```

Bad example:
```python
class Player(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.name}"
```

Bad example:
```python
class Player(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return str(self.name)
```

4. Use the correct `related_name`. In the majority of cases, the name of the model in plural will be just right.

Good example:
```python
class Team(models.Model):
    pass

class Player(models.Model):
    name = models.CharField(max_length=63)
    team = models.ForeignKey(Team, related_name="players")
```

Bad example:
```python
class Team(models.Model):
    pass

class Player(models.Model):
    name = models.CharField(max_length=63)
    team = models.ForeignKey(Team, related_name="teams")
```

5. `verbose_name` and `verbose_name_plural` should be in lowercase.

Good example:
```python
class Meta:
    verbose_name = "user"
    verbose_name_plural = "users"
```

Bad example:
```python
class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"
```

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
