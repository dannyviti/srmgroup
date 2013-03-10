# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'loss_report.visible'
        db.add_column(u'customer_portal_loss_report', 'visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'responder_information.visible'
        db.add_column(u'customer_portal_responder_information', 'visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'loss_report.visible'
        db.delete_column(u'customer_portal_loss_report', 'visible')

        # Deleting field 'responder_information.visible'
        db.delete_column(u'customer_portal_responder_information', 'visible')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'customer_portal.files': {
            'Meta': {'object_name': 'Files'},
            'all': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'file_inc': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'customer_portal.loss_report': {
            'Meta': {'object_name': 'loss_report'},
            'adjusted_reserve': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agency_epa': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agency_epa_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agency_nrc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agency_nrc_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agency_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'agency_state_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ar_date': ('django.db.models.fields.DateField', [], {}),
            'ar_given_to': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_adjuster': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_call_back': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'c_claim_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_driver': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_driver_no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'c_freight_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_tractor_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_trailer_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'dot_reprtbl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'f_call_back': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impervious': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'initial_corrective_actions': ('django.db.models.fields.TextField', [], {}),
            'intial_reserve': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ir_date': ('django.db.models.fields.DateField', [], {}),
            'ir_given_to': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'loss_loc': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'material_dis': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'material_dis_qt': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'msds_sec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'o_call_back': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'pervious': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'police_fire_recovery': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_scope_timeline': ('django.db.models.fields.TextField', [], {}),
            'reported_by': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'responder_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customer_portal.responder_information']", 'null': 'True', 'blank': 'True'}),
            'site_cont': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site_work_completed_comments': ('django.db.models.fields.TextField', [], {}),
            'srm_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'storm_drain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'surface_water': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'customer_portal.responder_information': {
            'Meta': {'object_name': 'responder_information'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contractor_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['customer_portal']