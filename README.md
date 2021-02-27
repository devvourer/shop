# download zip file from https://github.com/devvourer/shop/
 - extract file 
 - create virtual enivroment
 - activate virtual enivroment
 - download all packages from requirements
 - create database in postgresql
     * directory 'store' have file 'settings.py'
     * from 86 line starts code for connect database
     * you should replace 'shop_db' on your database name
     * replace key values "PASSWORD" and "USERNAME" with the database creator
 - make migrations with database

 - with command 'python manage.py createsuperuser' , create super user
 - after creating user, you should go to shell(python manage.py shell)
     * write this code :
     * from accounts.models import User
     * user = User.objects.get(id=1)
     * user.is_active = True
     * user.save()
     * close shell
 - run server
 - now you can go to admin panel

     
