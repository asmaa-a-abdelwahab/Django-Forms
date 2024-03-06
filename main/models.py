from django.db import models

# Create your models here.

class Compound(models.Model):
    email = models.EmailField(max_length=200, null=False, blank=False)
    cpd_id = models.IntegerField(max_length=50, null=False, blank=False)
    is_synthesis_protocol_available = models.BooleanField(default=False)
    
    
