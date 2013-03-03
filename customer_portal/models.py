from django.db import models
from django.contrib.auth.models import User, Group

class Files(models.Model):
	name = models.CharField(max_length=200)
	file_inc = models.TextField()
	user = models.ForeignKey(User, blank=True, null=True, default=1)
	group = models.ForeignKey(Group, blank=True, null=True)
	all = models.BooleanField()
	visible = models.BooleanField()
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Files"
		permissions = (
			("can_view_uploads", "Can view uploaded files"),
		)

