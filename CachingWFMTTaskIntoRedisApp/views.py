from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView,View
from django.core.cache import cache
from .models import WFMTTaskModel,Category
from django_redis import get_redis_connection
# Create your views here.
class WFMTListView(ListView):
    model=WFMTTaskModel
    template_name ="CachingWFMTTaskIntoRedisApp/wfmtlist.html"
    context_object_name ="tasks"
    
    def get_queryset(self,*args,**kwargs):
        search=self.request.GET.get("search")
        queryset= super().get_queryset(*args,**kwargs)
        if search is None:
            return queryset
        else:
            if cache.get("search"):
                print(cache.get("search"))
                print("Coming from Redis Cache")
                return cache.get("search")
            else:
                fil_val= queryset.filter(cp_number__icontains=search)
                print("coming from the DB Connection")
                cache.set("search", fil_val)
                # print(cache.get("search"))
                return fil_val
                        
    
class WFMTDetailView(DetailView):
    model =WFMTTaskModel
    template_name ="CachingWFMTTaskIntoRedisApp/wfmtdetail.html"
    context_object_name ="task"

    def get_context_data(self,*args, **kwargs):
        context=super(WFMTDetailView, self).get_context_data(*args, **kwargs)
        id=self.kwargs['pk']
        if cache.get(id):
            task=cache.get(id)
            context["data"]="Data Coming from Redis Cache on Request Hit"
            print("Data Coming from Redis Cache on Request Hit")
        else:
            task=WFMTTaskModel.objects.get(id=int(id))
            cache.set(id,task)
            context["data"]="Data Coming from the DB on request Hit"
            print("Data Coming from the DB on request Hit")
        return context

            
        
        
        
    
    
        
    
    