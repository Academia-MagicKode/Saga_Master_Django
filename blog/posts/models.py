from django.db import models
from django.contrib.auth import get_user_model
from datetime import date,timedelta

# Create your models here.

"""
Fileds:
    Relacionados con los campos admitidos por bases de datos SQL.
    (Aunque podriamos generar nuestros propios Fields)
    
Argumentos:

null - indica si un campo puede ser null, asociado a la BDD
blank - indica si un campo puede estar vacio, asociado a la validacion del lado Django.
default - El valor default sera usado si no se ingresa este campo
choices- Limita las opciones de un Field. (bdd- display form)
help_text- extra data para ser mostrada en un formulario.
primary_key- Generada automaticamente (id) si no creamos ninguna
unique- Campo de valor unico.

verbose_name- display del field, arg opcional que django puede generar automaticamente.
    para Foreingkey OntetoOne y ManytoMany puede ir solo como keyword arg.
auto_now- Mapeo automático del datetime actual
related_name -Diferenciamos campos enlazados a un mismo model

ManytoMany metodos:
    add => agregar objetos
    remove => borrar objetos
    all => consultar todos lso objetos
    clear => borrar todos los objetos
    count => numero de elementos almacenados

"""

class Post(models.Model):

    POST_TYPES=[
        ("N","Noticias"),
        ("A","Articulos"),
        ("C","Curiosidades"),
        ("F","Farandula")
    ]

    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             verbose_name="Autor")
    title=models.CharField("Titulo",max_length=50)
    content=models.TextField("Contenido")
    post_type=models.CharField("Tipo",max_length=1,choices=POST_TYPES)
    image=models.ImageField("Imagen",blank=True,null=True)
    created_at=models.DateTimeField("Hora y fecha de creacion",auto_now=True)
    stars=models.IntegerField(default=0)
    users_voted=models.ManyToManyField(get_user_model(), related_name="users_voted",
                                       verbose_name="Usuarios que votaron")


    class Meta():
        ordering=["-created_at"]
        verbose_name="Post"
        verbose_name_plural="Posteos"

    def __str__(self):
        return self.title


    def vote(self,user,stars):
        """
        Vote for post
        :param user (user objct)
        :param stars: (int [1-5])
        """
        if user in self.users_voted.all():
            return False
        self.stars+=stars
        self.users_voted.add(user)
        self.save()
        return True

    def save(self, *args,**kwargs):
        if self.author.is_banned:
            print("-------------Este Usuario esta baneado! no puede Postear!")
            return
        else:
            super().save(*args,*kwargs)
            self.author.post_number += 1
            self.author.save()
            return

#-------PROXY  MODELS--------------------------------------------------------

class PostOrderingStars(Post):

    @property
    def get_average_stars(self):
        number_users=self.users_voted.count()

        if number_users == 0:
            return 0
        else:
            return round(
                float(self.stars/number_users) ,1
            )

    @classmethod
    def best_voted_weekly(cls, avg=4):
        """return the best voted last week"""
        qs=PostOrderingStars.objects.filter(created_at__gte=date.today()-timedelta(days=7))
        best_voted= [post for post in qs if post.get_average_stars >= avg ]
        return best_voted


    class Meta:
        ordering = ["-stars"]
        proxy=True


class UsersFollows(models.Model):
    user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    users_followed=models.ManyToManyField(get_user_model(), related_name="users_followed",
                                          verbose_name="Usuarios Seguidos")

    class Meta():
        verbose_name = "Usuarios Seguidos"
        verbose_name_plural = "Usuarios Seguidos"

    def __str__(self):
        return self.user.email

""""

# EJEMPLO CLASES MODELOS ABSTRACTOS-----------------------------
class GeneralInfo(models.Model):
    name=models.CharField(max_length=100)
    birthday=models.DateField()

    class Meta:
        ordering=["name",]
        abstract=True


class Student(GeneralInfo):
    
    
    class Meta(GeneralInfo.Meta):
        verbose_name="Estudiante"

"""