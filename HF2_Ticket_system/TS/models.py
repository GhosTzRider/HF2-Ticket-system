from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Supporter(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'supporters'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, db_column='category_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'acticles'  # matches your table name exactly

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'services'

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        managed = False
        db_table = 'priorities'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'statuses'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, db_column='category_id')
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, db_column='service_id')
    priority = models.ForeignKey(Priority, on_delete=models.DO_NOTHING, db_column='priority_id')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, db_column='status_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    supporter = models.ForeignKey(Supporter, on_delete=models.DO_NOTHING, db_column='supporter_id', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'tickets'

    def __str__(self):
        return self.title