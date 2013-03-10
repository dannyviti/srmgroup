from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.utils.encoding import smart_str
from django.contrib.auth.decorators import permission_required
from customer_portal.models import Files, responder_information, loss_report
from django.core.servers.basehttp import FileWrapper
from django.db.models import Q
import os, mimetypes

@permission_required('customer_portal.can_view_uploads', login_url="/cp/customer/login/")
def portal_index(request):
	response = "%s welcome to The SRM Group LLC Customer Portal" % request.user.first_name
	return render_to_response('customer_portal/index.html',{
		'response': response,
		})

@permission_required('customer_portal.can_view_uploads', login_url="/cp/customer/login/")
def file_index(request):
	user_id = request.user.id
	groups = request.user.groups
	group_ids = []
	for grp in iter(request.user.groups.all()):
		group_ids.append(grp.id)
	#debug = "group ids %s\n" % group_ids
	#debug += "perm is - %s\n" % request.user.has_perm('customer_portal.can_view_uploads')
	#debug += "user id %s\n" % user_id
	file_id_list = Files.objects.filter(Q(user__exact=user_id) | Q(all__exact=1))
	#debug += "file_id_list %s\n" % file_id_list
	sql_file_ids = []
	for fperm in file_id_list:
		sql_file_ids.append(fperm.id) 
	file_id_list = Files.objects.filter(group__in=group_ids)
	for fperm in file_id_list:
		sql_file_ids.append(fperm.id)
	#debug = "sql ids %s" % sql_file_ids
	file_list = Files.objects.filter(id__in=sql_file_ids, visible__exact=1).distinct().order_by("name")
	response = request.user.first_name
	return render_to_response('customer_portal/files.html',{
		'response': response,
		#'debug': debug,
		'groups': groups,
		'file_id_list': file_id_list,
		'file_list': file_list,
		})

@permission_required('customer_portal.can_view_reports', login_url="/cp/customer/login/")
def loss_reports_index(request):
	user_id = request.user.id
	groups = request.user.groups
	group_ids = []
	for grp in iter(request.user.groups.all()):
		group_ids.append(grp.id)
	#debug = "group ids %s\n" % group_ids
	report_list = loss_report.objects.filter(organization_id__in=group_ids, visible__exact=1).distinct().order_by('srm_id', 'date')
	response = "%s here are The SRM Group Loss Reports for your account" % request.user.first_name
	return render_to_response('customer_portal/loss_reports.html',{
		'response': response,
		'user' : request.user.first_name,
		'report_list': report_list,
		#'debug': debug,
		})

@permission_required('customer_portal.can_view_reports', login_url="/cp/customer/login/")
def loss_report_single(request, report_id):
	user_id = request.user.id
	groups = request.user.groups
	group_ids = []
	for grp in iter(request.user.groups.all()):
		group_ids.append(grp.id)
	#debug = "group ids %s<br>\n" % group_ids
	#debug += "report id %s<br>\n" % report_id
	report_details = loss_report.objects.filter(srm_id__exact=report_id, organization_id__in=group_ids, visible__exact=1).distinct().order_by('srm_id', 'date').select_related('organization', 'responder_info')
	org_name = loss_report.objects.values_list('organization__name', flat=True)
	#debug += "query - %s<br>\n" % loss_report.objects.filter(srm_id__exact=report_id, organization_id__in=group_ids, visible__exact=1).query
	response = "SRM ID: %s - Loss Report Detail" % report_id
	return render_to_response('customer_portal/loss_report_single.html',{
		'response': response,
		'user' : request.user.first_name,
		'report_details': report_details,
		'report_id': report_id,
		'org_name': org_name,
		#'debug': debug,
		})

@permission_required('customer_portal.can_view_uploads', login_url="/cp/customer/login/")
def sendfile(request,filename,path):
	if filename:
		filewpath = ''.join([path,filename])
		if not os.path.exists(filewpath):
			#raise Http404
			response = HttpResponse("No Luck dude.%s" % (filewpath))
			return response
		else:
			wrapper = FileWrapper(file(filewpath))
			content_type = mimetypes.guess_type(filename)[0]
			response = HttpResponse(wrapper, mimetype='%s' % content_type) 
			response['Content-length'] = os.path.getsize(filewpath)
			response['X-Sendfile'] = filewpath
			response['Content-Disposition'] = "attachment; filename=%s" % (filename)
			return response
	else:
		#raise Http404
		response = HttpResponse("Even less luck dude.")
		return response

