from django.db import models

class temple(models.Model):
    nametemple=models.CharField(("ชื่อ"),max_length=255)
    namemunk=models.CharField(("พระเกจิ"),max_length=255)
    detail=models.CharField(("รายละเอียด"),max_length=255)
    latijud=models.CharField(("ละติจูด"),max_length=255)
    longtijud=models.CharField(("ลองติจูด"),max_length=255)

    def __str__(self):
        return self.nametemple