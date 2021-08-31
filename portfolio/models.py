from django.db import models


class Resume(models.Model):
    image = models.ImageField(upload_to='resume/image/')
    name = models.CharField(max_length=50, db_index=True)
    age = models.IntegerField()
    job = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=254)
    cv_file = models.FileField(upload_to='resume/files/')
    description = models.TextField()

    def __str__(self):
        return self.name


class DesignSkill(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class CodingSkill(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class LanguageSkill(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='resume/clients/')

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category , related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/porjects/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title    


class Social(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    link = models.URLField(max_length=200)
    icon = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title   


class Message(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False)
    subject = models.CharField(max_length=100, null=False)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name   