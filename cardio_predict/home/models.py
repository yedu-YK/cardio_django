from django.db import models

# Create your models here.
class CardioModel(models.Model):

    gender_choices = ((1,'Female'),(2,'male'))
    chol_choices = ((1,'Normal'),(2,'Above Normal'),(3,'Well Above Normal'))
    gluc_choices = ((1,'Normal'),(2,'Above Normal'),(3,'Well Above Normal'))
    smoker_choices = ((0,'Smoker'),(1,'Non Smoker'))
    alco_choices = ((0,'Drinks'),(1,'Non Drinker'))
    active_choices = ((0,'Active Person'),(1,'Non Active Person'))

    date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    gender = models.IntegerField( choices=gender_choices)
    cholesterol = models.IntegerField( choices=chol_choices)
    height = models.IntegerField()
    weight = models.IntegerField()
    
    sbp = models.IntegerField()
    dbp = models.IntegerField()
    
    gluc = models.IntegerField(choices=gluc_choices)
    smoke = models.IntegerField(choices=smoker_choices)
    alco = models.IntegerField(choices=alco_choices)
    active = models.IntegerField( choices=active_choices)
    
    bmi = models.IntegerField(null=True)
    bpc = models.IntegerField( null=True)
    
    cardio = models.IntegerField( null=True)