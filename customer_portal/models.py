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
		verbose_name_plural = 'Files'
		permissions = (
			("can_view_uploads", "Can view uploaded files"),
		)

class responder_information(models.Model):
	contractor_name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	fax = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	visible = models.BooleanField()
	def __unicode__(self):
		return u'%s (%s, %s)' % (self.contractor_name, self.city, self.state)
	class Meta:
		verbose_name = 'Responder Information'
		verbose_name_plural = 'Responders Information'

class loss_report(models.Model):
	date = models.DateTimeField()
	srm_id = models.CharField('SRM ID', max_length=50)
	reported_by = models.CharField('Name of Person Calling', max_length=200)
	o_call_back = models.CharField('Office No.', max_length=20)
	c_call_back = models.CharField('Cell No.', max_length=20)
	f_call_back = models.CharField('Fax No.', max_length=20)
	organization = models.ForeignKey(Group, blank=True, null=True)
	loss_loc = models.CharField('Loss Location', max_length=400)
	site_cont = models.CharField('Onsite contact', max_length=100)
	material_dis = models.CharField('Material Discharge', max_length=100)
	material_dis_qt = models.CharField('Quantity', max_length=100)
	pervious = models.BooleanField()
	impervious = models.BooleanField()
	surface_water = models.BooleanField()
	storm_drain = models.BooleanField()
	msds_sec = models.BooleanField('MSDS secured')
	dot_reprtbl = models.BooleanField('DOT reportable')
	c_claim_no = models.CharField('Client Claim #', max_length=100)
	c_freight_no = models.CharField('Client Freight Bill #', max_length=100)
	c_adjuster = models.CharField('Adjuster assigned', max_length=100)
	c_tractor_no = models.CharField('Tractor #', max_length=100)
	c_trailer_no = models.CharField('Trailer #', max_length=100)
	c_driver = models.CharField('Driver Name', max_length=100)
	c_driver_no = models.CharField('Contact Number', max_length=20)
	police_fire_recovery = models.CharField('Police/Fire/Recovery onsite', max_length=200)
	agency_state = models.CharField(max_length=100)
	agency_state_no = models.CharField('Agency State #', max_length=100)
	agency_epa = models.CharField('Agency EPA', max_length=100)
	agency_epa_no = models.CharField('Agency EPA #', max_length=100)
	agency_nrc = models.CharField('Agency NRC', max_length=100)
	agency_nrc_no = models.CharField('Agency NRC #', max_length=100)
	responder_info = models.ForeignKey(responder_information, blank=True, null=True)
	initial_corrective_actions = models.TextField()
	intial_reserve = models.CharField(max_length=100)
	ir_given_to = models.CharField('Initial Given to', max_length=100)
	ir_date = models.DateField('Date')
	adjusted_reserve = models.CharField(max_length=100)
	ar_given_to = models.CharField('Adjusted Given to', max_length=100)
	ar_date = models.DateField('Date')
	project_scope_timeline = models.TextField()
	site_work_completed_comments = models.TextField()
	visible = models.BooleanField()
	class Meta:
		verbose_name = 'Loss Report'
		verbose_name_plural = 'Loss Reports'
        permissions = (
		    ("can_view_reports", "Can view Loss Reports"),
	    )

