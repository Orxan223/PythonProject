from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from font_icons.models import IconForeignKeyField
# from django.contrib.auth import get_user_model
# User= get_user_model
from django.urls import reverse
# ---------------------------------------      About     ----------------------------------
# About settles in this stock


class About(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField('Sekil', upload_to='about_image')

    def __str__(self):
        return self.title

    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name = 'About'
    #     verbose_name_plural = 'Abouts'
        # ordering = ('-created_at',)

# ---------------------------------------      Choose     ----------------------------------

# Choose settles in this stock


class Choose(models.Model):
    icon = IconForeignKeyField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=150)
    description = models.CharField(blank=True, null=True, max_length=127)

    def __str__(self):
        return self.title
    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name = 'Choose'
    #     verbose_name_plural = 'Chooses'
        # ordering = ('-created_at',)




# ---------------------------------------      Skills     ----------------------------------
    # About settles in this stock


class Skill(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    text = models.TextField(blank=True, null=True)
    category = models.ForeignKey("Category",on_delete=CASCADE)
    name = models.CharField(blank=True, null=True, max_length=150)
    image = models.ImageField('Sekil', upload_to='about_image',blank=True, null=True)
    eded = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.title

class Category(models.Model):
    percent = models.IntegerField(blank=True, null=True)


    
 


# ---------------------------------------      Blog     ----------------------------------

    # Blog settles in this stock

class Blog(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    image = models.ImageField('Sekil', upload_to='Blog_image')
    profession = models.ForeignKey('Profession', on_delete=models.CASCADE)

    # icon = IconForeignKeyField(blank=True,null=True)
    # date = models.DateField()

    def __str__(self):
        return self.title
    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


class Profession(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)
    icon = IconForeignKeyField(blank=True,null=True)

    def __str__(self):
        return self.name

    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name = 'Category'
    #     verbose_name_plural = "Categories"
        # ordering = ('name', '-created_at')

# ---------------------------------------      News     ----------------------------------

    # News settles in this stock


class News(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    short_description =  models.CharField(blank=True, null=True, max_length=150)
    slug = models.SlugField('Slug',max_length=127)
    image = models.ImageField('Sekil', upload_to='Blog_image')
    pese = models.ForeignKey('Pese', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('news_detail',args={self.slug})


class Pese(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)
    icon = IconForeignKeyField(blank=True,null=True)

    def __str__(self):
        return self.name




# ---------------------------------------      Contact     ----------------------------------

# Contact settles in this stock
class Contact(models.Model):
    full_name = models.CharField(blank=True, null=True, max_length=150)
    email = models.EmailField(blank=True, null=True, max_length=150)
    subject = models.CharField(blank=True, null=True, max_length=150)
    message = models.TextField(blank=True, null=True, help_text='Send your message', max_length=150)

    def __str__(self):
        return self.full_name

    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # published = models.BooleanField('Is published' , default=True)
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"
        # ordering = ('-created_at',)
