from django.contrib import admin

from adminfiles.admin import FilePickerAdmin

from srmgroup.customer_portal.models import *

class FilesAdmin(FilePickerAdmin):
    adminfiles_fields = ['file_inc',]

class responder_informationAdmin(admin.ModelAdmin):
    list_diplay = ('contractor_name','city','state')

class loss_reportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,           {'fields': ['date','srm_id','reported_by','o_call_back','c_call_back','f_call_back','organization']}),
        (None,           {'fields': ['loss_loc','site_cont','material_dis','material_dis_qt']}),
        ('Released to:', {'fields': ['pervious','impervious','surface_water','storm_drain']}),
        (None,           {'fields': ['msds_sec','dot_reprtbl']}),
        ('Client Reference Number (Obtain one of the follwing)', {'fields': ['c_claim_no','c_freight_no','c_adjuster','c_tractor_no','c_trailer_no','c_driver','c_driver_no']}),
        (None,           {'fields': ['police_fire_recovery']}),
        ('Agency Notification',           {'fields': ['agency_state','agency_state_no','agency_epa','agency_epa_no','agency_nrc','agency_nrc_no']}),
        (None,           {'fields': ['responder_info']}),
        (None,           {'fields': ['initial_corrective_actions','intial_reserve','ir_given_to','ir_date','adjusted_reserve','ar_given_to','ar_date','project_scope_timeline','site_work_completed_comments']}),
        (None,           {'fields': ['visible']}),
    ]
    list_display = ('srm_id','organization','date')

admin.site.register(Files, FilesAdmin)
admin.site.register(responder_information, responder_informationAdmin)
admin.site.register(loss_report, loss_reportAdmin)

