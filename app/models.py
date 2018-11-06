from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import User


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Client(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    user = models.OneToOneField(User)

    name = models.CharField(
        verbose_name='nombre',
        max_length=128,
    )

    email = models.EmailField(
        verbose_name='correo electrónico',
        unique=True,
        blank=False,
    )

    is_driver = models.BooleanField(
        default=False,
        help_text='Indica si el usuario es conductor',
    )

    def __str__(self):
        if self.is_driver:
            return f'conductor - {self.name}'
        return f'pasajero - {self.name}'


    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ('-id',)


class Trip(models.Model):
    CITY_CHOICES = (
        (1, 'Armenia'),
        (3, 'Barranquilla'),
        (2, 'Barrancabermeja'),
        (4, 'Bogotá'),
        (5, 'Bucaramanga'),
        (6, 'Caldas (Antioquia)'),
        (7, 'Cali'),
        (8, 'Cartagena'),
        (9, 'Cúcuta'),
        (10, 'Florencia - Caqueta'),
        (11, 'Manizales'),
        (12, 'Medellín'),
        (13, 'Montería'),
        (15, 'Pamplona'),
        (16, 'Pasto'),
        (17, 'Pereira'),
        (18, 'Popayán'),
        (19, 'Soacha'),
        (20, 'Sogamoso'),
        (21, 'Tunja'),
        (14, 'Otra'),
        (22, 'Fuera del país'),
    )

    travel_date = models.DateTimeField(
        verbose_name='fecha de viaje',
    )

    quotas = models.PositiveSmallIntegerField(
        verbose_name='cupos'
    )

    driver = models.ForeignKey(
        'app.Client',
        verbose_name='conductor'
    )

    city_from = models.PositiveSmallIntegerField(
        choices=CITY_CHOICES,
        verbose_name='ciudad de origen',
    )

    city_to = models.PositiveSmallIntegerField(
        choices=CITY_CHOICES,
        verbose_name='ciudad de destino',
    )

    def __str__(self):
        return 'Viaje {} - {}'.format(
            self.get_city_from_display(),
            self.get_city_to_display()
        )

    class Meta:
        verbose_name = 'viaje'
        verbose_name_plural = 'viajes'
        ordering = ('-id',)


class Reservation(models.Model):
    trip = models.ForeignKey(
        'app.Trip',
        verbose_name='viaje',
    )

    user = models.ForeignKey(
        'app.Client',
        verbose_name='usuario',
    )

    requested_quotas = models.PositiveSmallIntegerField(
        help_text='cupos solicitados',
    )

    def __str__(self):
        return f'Reservacion No {self.id}, cupos: {self.requested_quotas}'

    class Meta:
        verbose_name = 'reservacion'
        verbose_name_plural = 'reservaciones'
        ordering = ('-id',)
