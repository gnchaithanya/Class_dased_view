from django.shortcuts import render

# Create your views here.
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from app.forms import *

#  Http response by using Fuctionbased Views
def Fbv_view(request):
     return HttpResponse('This is functional based view')

# Http response by using Classbased Views
class Cbv_view(View):
     def get(self,request):
          return HttpResponse('This is class Based View')
     
# Rendering by using functional based view
def fbv_render(request):
     return render(request,'fbv_render.html')


# Rendering by using class based view
class cbv_render(View):
     def get(self,request):
          return render(request,'cbv_render.html')
     
#  insert by using fbv_temp
def insert_fbv(request):
     SFO=StudentFrom()
     d={'SFO':SFO}
     if request.method=='POST':
          SFDO=StudentFrom(request.POST)
          if SFDO.is_valid():
               SFDO.save()
               return HttpResponse('Data is Inserted Successfully!!!!')
     return render(request,'insert_fbv.html',d)


# insert by using cbv_temp
class insert_cbv(View):
    def get(self,request):
         SFO=StudentFrom()
         d={'SFO':SFO}
         
         return render(request,'insert_cbv.html',d)
    def post(self,request):
             
             SFDO=StudentFrom(request.POST)
             if SFDO.is_valid():
                  SFDO.save()
                  return HttpResponse('Data Inserted Successfulle!!!')
        
#  insert by unsing (cbv_temp)    Tempalte View
class cbv_temp(TemplateView):
     template_name='cbv_temp.html'
     