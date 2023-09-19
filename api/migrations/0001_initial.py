from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = CustomUser(name="Anushri", 
                          email="anu09@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="8109761205",
                          gender ="female"
                          )
        user.set_password('anushri')
        user.save()

    dependencies=[]

    operations =[
            migrations.RunPython(seed_data),
        ]