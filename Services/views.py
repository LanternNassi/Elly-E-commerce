from django.shortcuts import render,redirect
from django.http import HttpResponse
from Services.forms import service_installer,login_view_form,service_editer
from django import forms
from Services.models import Plumbing_Services,Tiling_Services,images_plumbing,images_tiling

# Create your views here.

def recorder (request):
    msg = None
    form = service_installer()
    if request.method == "POST":
        form = service_installer(request.POST,request.FILES )
        if form.is_valid():
            Name = form.cleaned_data.get("Name")
            Contact = form.cleaned_data.get("Contact")
            Email = form.cleaned_data.get("Email")
            Password = form.cleaned_data.get("Password")
            profile_pic = form.cleaned_data.get("profile_pic")
            p=Plumbing_Services.objects.create(Name=Name,Contact=Contact,EMail=Email,Password=Password,Status=False,profile_pic=profile_pic)
            p.save()
            images_plumbing.objects.create(Name=p,image=profile_pic)
            return render(request,'elly/plumber_account.html',{'plumber':Plumbing_Services.objects.get(Password=Password),'Plumber_gallery':images_plumbing.objects.filter(Name__Password=Password)})

            #return redirect("/")
            # return render(re)
            #base = Plumbing_Services.objects.all()
            #for plumber in base :
            #    if plumber.Name == p.Name :
             #       msg = 'User already exists pick another name'
              #      form = service_installer()

               # else :
                #    return redirect("/") 
        else :
            msg=form.errors
            form=service_installer()  
    else:
        form=service_installer()                
                      
                
            

    return render(request,'elly/service_form.html',{'form':form,'msg':form.errors})



def login_view (request):
    form = login_view_form(request.POST)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("Name")
            Password = form.cleaned_data.get("Password")
            base = Plumbing_Services.objects.all()
            for plumber in base :
                if plumber.Password == Password:
                    if plumber.Name == username :
                        #return redirect("/Catalogue/")
                        return render(request,'elly/plumber_account.html',{'plumber':Plumbing_Services.objects.get(Name=username),'Plumber_gallery':images_plumbing.objects.filter(Name__Name=username)})
                        #return render(request,'elly/portfolio-details.html',{'plumber':plumber}) 
                    else :
                        msg='Please check your name'
                else :
                    msg = 'Error validating account.Please check whether your account is present' 

        else :

            form = login_view()
    return render(request,'elly/login.html',{'form':form,})                



""" Start of the tilers section """


def recorder_tiler (request):
    msg = None
    form = service_installer()
    if request.method == "POST":
        form = service_installer(request.POST,request.FILES )
        if form.is_valid():
            Name = form.cleaned_data.get("Name")
            Contact = form.cleaned_data.get("Contact")
            Email = form.cleaned_data.get("Email")
            Password = form.cleaned_data.get("Password")
            profile_pic = form.cleaned_data.get("profile_pic")
            p=Tiling_Services.objects.create(Name=Name,Contact=Contact,Email=Email,Password=Password,Status=False,profile_pic=profile_pic)
            p.save()
            images_tiling.objects.create(Name=p,image=profile_pic)
            return render(request,'elly/Tiler_account.html',{'tiler':Tiling_Services.objects.get(Name=Name),'Tiler_gallery':images_tiling.objects.filter(Name__Name=Name)})
            #return redirect("/")
            #base = Plumbing_Services.objects.all()
            #for plumber in base :
            #    if plumber.Name == p.Name :
             #       msg = 'User already exists pick another name'
              #      form = service_installer()

               # else :
                #    return redirect("/") 
                    
                      
                
            

    return render(request,'elly/tiler_signup.html',{'form':form})



def login_view_tiler (request):
    form = login_view_form(request.POST)
    
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("Name")
            Password = form.cleaned_data.get("Password")
            base = Tiling_Services.objects.all()
            for Tiler in base :
                if Tiler.Password == Password:
                    if Tiler.Name == username :
                        #return redirect("/Catalogue/")
                        return render(request,'elly/Tiler_account.html',{'tiler':Tiling_Services.objects.get(Name=username),'Tiler_gallery':images_tiling.objects.filter(Name__Name=username)}) 
                    else :
                        msg='Please check your name'
                else :
                    msg = 'Error validating account.Please check whether your account is present' 

        else :

            form = login_view()
    return render(request,'elly/login_tiler.html',{'form':form})     




def services_renderer (request):
    plumbers = Plumbing_Services.objects.all()
    tilers = Tiling_Services.objects.all()
    tile_pic = images_tiling.objects.all()
    return render(request,'elly/services.html',{'plumbers':plumbers,'tilers':tilers})  



def profile_renderer (request,id):
    tiles_info = Tiling_Services.objects.get(id = id)
    tiles_gallery = images_tiling.objects.filter(Name__Name = tiles_info.Name)
    
    return render(request,'elly/profile.html',{'tiles_info':tiles_info,'tiles_gallery':tiles_gallery})  

def profile_renderer_plumbing (request,id):
    
    plumber_info = Plumbing_Services.objects.get(id = id)
    plumber_gallery = images_plumbing.objects.filter(Name__Name = plumber_info.Name)
    
    return render(request,'elly/profile_plumber.html',{'plumber_info':plumber_info,'plumber_gallery':plumber_gallery})               










# start of account editting\

def tiler_editer(request,id):
    information = Tiling_Services.objects.get(id = id)
    info = {'Name':information.Name , 'Contact':information.Contact , 'Email': information.Email , 'Password':information.Password }  
    if request.method == "POST" :
        form = service_editer(request.POST)
        if form.is_valid():
            Tiling_Services.objects.filter(id = id).update(Name=form.cleaned_data.get("Name"),Contact=form.cleaned_data.get("Contact"),Email=form.cleaned_data.get("Email"),Password=form.cleaned_data.get("Password"))
            username = form.cleaned_data.get("Name")
            Password = form.cleaned_data.get("Password")
        return render(request,'elly/Tiler_account.html',{'tiler':Tiling_Services.objects.get(Name= username),'Tiler_gallery':images_tiling.objects.filter(Name__Name=username)}) 
            #return redirect("/")

    else :  
        form = service_editer(info)    
    return render(request,'elly/Tilers_editer.html',{'form':form})



def plumber_editer(request,id):
    information = Plumbing_Services.objects.get(id = id)
    info = {'Name':information.Name , 'Contact':information.Contact , 'Email': information.EMail , 'Password':information.Password }  
    if request.method == "POST" :
        form = service_editer(request.POST)
        if form.is_valid():
            Plumbing_Services.objects.filter(id = id).update(Name=form.cleaned_data.get("Name"),Contact=form.cleaned_data.get("Contact"),EMail=form.cleaned_data.get("Email"),Password=form.cleaned_data.get("Password"))
            username = form.cleaned_data.get("Name")
            Password = form.cleaned_data.get("Password")
        return render(request,'elly/Tiler_account.html',{'tiler':Plumbing_Services.objects.get(Name=username),'Tiler_gallery':images_tiling.objects.filter(Name__Name=username)}) 
            #return redirect("/")

    else :  
        form = service_editer(info)    
    return render(request,'elly/Tilers_editer.html',{'form':form})




            





              

