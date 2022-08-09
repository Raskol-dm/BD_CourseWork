from django.db import models

# Наша база данных
# Create your models here.


class Plants(models.Model):
	COMPL = (
            ('Master', 'master'),
            ('Middle', 'middle'),
            ('Beginner', 'beginner'),
	)
	LIGHT = (
            ('Sunny', 'sunny'),
            ('Half-shade', 'half-shade'),
            ('Dark', 'dark'),
	)
	name = models.CharField(max_length=200, db_index=True)
	kind = models.CharField(max_length=200, null=True)
	height = models.IntegerField(null=True)
	complexity = models.CharField(max_length=200, null=True, choices=COMPL)
	lighting = models.CharField(max_length=200, null=True, choices=LIGHT)
	waterfreq = models.IntegerField(null=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Цветок'
		verbose_name_plural = 'Цветы'

	def __str__(self):
		return self.name

class Room(models.Model):
	rname = models.CharField(max_length=200, db_index=True)
	status = models.BooleanField(default=False)
	user_id = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)

	class Meta:
		ordering = ('user_id',)
		verbose_name = 'Комната'
		verbose_name_plural = 'Комнаты'

	def __str__(self):
		return self.rname
