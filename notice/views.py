from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from notice.models import Notice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views import generic

from notice.models import Notice

class NoticeList(ListView):
	model = Notice
	paginate_by = 2
	template_name = 'notice/index.html'

	def get_context_data(self,**kwargs):
		context = super(NoticeList,self).get_context_data(**kwargs)
		#context['now'] = 'hi'
		return context
		


def contact(request):
	return render(request,'notice/contact.html',)

def about(request):
	return render(request,'notice/about.html',)	
