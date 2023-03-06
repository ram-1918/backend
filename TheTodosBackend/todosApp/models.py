from django.db import models
from datetime import datetime
# Create your models here.

# class Users(models.Model):
#     username = models.CharField(max_length= 255, unique = True)
#     email = models.CharField(max_length = 255)
#     password = models.CharField(max_length = 255)
#     phone = models.CharField(max_length=12)

#     def get_user():
#         user, created =  Users.objects.get_or_create(
#             id = 1,
#             defaults = {'username':'Ram'})
#         return user.pk

#     def __str__(self):
#         return self.username
    
#     class Meta:
#         verbose_name_plural = "Users"

class TodoLists(models.Model):
    priorities = [('None', 'No Priority'), ('1', 'Important'),('2', 'Urgent And Important')]
    name = models.CharField(max_length = 255, unique = True)
    # count = models.IntegerField(blank = True, default= 0)
    priority = models.CharField(max_length = 20, choices= priorities, default = 'None')
    deadline = models.DateField(blank = True)
    favorites = models.BooleanField(default= False)

    # @classmethod
    # def get_default_list(self):
    #     list, create = self.objects.get_or_create(
    #         name = "Default List",
    #         defaults = {'date_created': datetime.now()}
    #     )
    #     return list.pk
    
    # def save(self, *args, **kwargs):
    #     count = 0
    #     try:
    #         tasks = self.tasks.all()
    #         for task in tasks:
    #             if task.list.pk == self.id:
    #                 count += 1
    #         self.count = count
    #     except: 
    #         pass
    #     super(TodoLists, self).save(*args, **kwargs)



    # def __str__(self):
    #     return self.pk
    
    class Meta:
        verbose_name_plural = "TodoLists"

class TodoTasks(models.Model):
    priorities = [('None', 'No Priority'), ('1', 'Important'),('2', 'Urgent And Important')]
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length = 255, blank = True)
    priority = models.CharField(max_length = 20, choices= priorities, default = 'None')
    status = models.BooleanField(default= False)
    favorite = models.BooleanField(default= False)
    deadline = models.DateField(blank = True)
    list = models.ForeignKey(TodoLists, related_name = "tasks", on_delete= models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "TodoTasks"
