from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant , Contact
# Create your views here.
def home(request: HttpRequest):
    plants = Plant.objects.filter(is_edible=False)[0:3]

    context = {
        "plants" : plants
    }
    return render(request,"main/home.html" , context)


def all_plants(request: HttpRequest):

    if "categories" in request.GET:
        plants = Plant.objects.filter(category=request.GET["categories"])
    else:
        plants = Plant.objects.all

    return render(request,"main/all_plants.html" , {"plants" : plants , "category" : Plant.categories.choices})

def add(request: HttpRequest):
    if request.method =="POST":
        try:
            new_plant=Plant(
            name=request.POST["name"],
            about=request.POST["about"],
            is_edible=request.POST.get("is_edible" , False),
            used_for=request.POST["used_for"],
            category=request.POST["category"],
            image=request.FILES.get("image", Plant.image.field.default)
            )

            new_plant.save()

        except Exception as e:
            print(e)
        return redirect('main:home')
    
    return render(request,"main/add_plant.html" , {"category" : Plant.categories.choices})



def detail(request: HttpRequest ,plant_id):
    try:
        plant=Plant.objects.get(pk=plant_id)
        plants=Plant.objects.filter(is_edible=False)[0:3]
        
    except Plant.DoesNotExist:
        return redirect('main:home')
    except Exception as e:
            print(e)

    return render(request,"main/plants_detail.html" , {"plant" : plant ,"plants" : plants } )




def update(request: HttpRequest , plant_id):
    plant=Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        try:
            plant.name=request.POST["name"]
            plant.about=request.POST["about"]
            plant.is_edible=request.POST.get("is_edible" , False)
            plant.used_for=request.POST["used_for"]
            plant.category=request.POST["category"]
            plant.image=request.FILES.get("image", Plant.image.field.default)
            plant.save()
            return redirect('main:detail_page' , plant_id=plant.id)
        except Plant.DoesNotExist:
         return redirect('main:home')
        except Exception as e:
            print(e)

    return render(request,"main/update.html" , {"plant" : plant , "category" : Plant.categories.choices })



def delete(request: HttpRequest , plant_id):
    try:
        plant=Plant.objects.get(pk=plant_id)
        plant.delete()
    except Plant.DoesNotExist:
         plant=None
    except Exception as e:
            print(e)

    return redirect('main:home')


def search(request: HttpRequest):
    plants=[]
    if "search" in request.GET:
        plants=Plant.objects.filter(name__contains=request.GET["search"])
    return render(request,"main/search.html" , {"plants" : plants} )





def info(request: HttpRequest):
 if request.method ==" POST ":
        try:
            info=Contact(
            f_name=request.POST["f_name"],
            l_name=request.POST["l_name"],
            email=request.POST["email"],
            message=request.POST["message"],
            )
            info.save()
            return redirect('main:home')
        except Exception as e :
            print(e)
 return render(request,"main/contact.html")


def user_message(request: HttpRequest):
    con=Contact.objects.all()

    return render(request,"main/message.html", {"con" : con})