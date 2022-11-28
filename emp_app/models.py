from django.db import models

# Create your models here.
# class department(models.Model):
#     name=models.CharField(max_length=100,null=False)

#     def __str__(self):
#         return self.name

class emp(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    salary=models.IntegerField(default=0)
    # dept=models.ForeignKey(department, on_delete=models.CASCADE)
    dept=models.CharField(max_length=100,null=False)
    
    
    def __str__(self):
        return "%s %s %s " %  ( self.first_name,  self.last_name,  self.dept)


