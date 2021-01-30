from django.shortcuts import render
from invoice_app.models import Item_entry, Item_sold
from django.shortcuts import redirect 
from invoice_app import forms  # (to connect with from.py classes)




def base(request):
    diction= {}

    return render(request, 'invoice_app/base.html', context=diction )


def home(request):

    diction = {"home_text" : "Welcome to Food'oice"}

    return render(request, 'invoice_app/home.html', context=diction )



def index(request):

    food_list = Item_entry.objects.order_by("item_name")

    diction = {"text1": "List of food items", "food_list": food_list}
    return render(request, 'invoice_app/index.html', context=diction)



def form(request):

    new_form = forms.EntryForm()  # creating a ItemEnrty_Form object 

    if request.method == 'POST':   #  to cheack wheather the has submitted or not 

        # if condition supports,the submitted form will override in new_form   
        new_form = forms.EntryForm(request.POST) 

        if new_form.is_valid():   #cheaking validations
            new_form.save(commit="True")   # to save information in models

            return redirect('/index/') # to view the update in index page
    else:

        diction= {"item_form": new_form, "heading_1" : "Add new items"}
        return render(request, 'invoice_app/form.html', context=diction)




def orderForm(request):

    form = forms.OrderForm()

    if request.method == "POST":

        form = forms.OrderForm(request.POST)

        if form.is_valid():
            form.save(commit="True")

            return index(request)

    diction = {"title": "place an order", "order_form": form}

    return render(request, 'invoice_app/orderForm.html', context=diction)



def sold_list(request, item_id):

    food_info = Item_entry.objects.get(pk = item_id)  # query- to get data from database using pk
    sold_info = Item_sold.objects.filter(item = item_id )

    diction= {'title': 'order list', 'food_info': food_info, 'sold_info': sold_info}

    return render(request, 'invoice_app/sold_list.html', context= diction)



def edit_info(request, food_id): # same as form class 

    food_info = Item_entry.objects.get(pk = food_id)
    new_form = forms.EntryForm(instance= food_info)
    diction={}

    if request.method == 'POST':  # for editing info 

        new_form = forms.EntryForm(request.POST, instance= food_info)

        if new_form.is_valid():   #cheaking validations

            new_form.save(commit="True")
            diction.update({'update_text':'Successfully Updated!'})
            # return index(request) # updated info ta je url/page e show korte chai

 

    diction.update({'edit_form' : new_form, 'food_info': food_info})

    return render(request, 'invoice_app/edit_info.html', context= diction)


def delete_info(request):

    diction = {}

    return render(request, 'invoice_app/delete_info.html', context=diction)
