from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=144, null=False, blank=False, db_column='NAME')
    desc = models.TextField(null=False, blank=False, db_column='DESCRIPTION')
    is_active = models.BooleanField(db_default=True, db_column='IS_ACTIVE')
    is_deleted = models.BooleanField(db_default=False, db_column='IS_DELETED')
    
    class Meta:
        pass
    
    def __str__(self):
        return f"{self.name} : {self.desc}"