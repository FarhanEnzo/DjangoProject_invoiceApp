from django.db import models

class Item_entry(models.Model):

    item_name = models.CharField(max_length= 100)
    item_catagory = models.CharField(max_length= 100)
    item_price = models.IntegerField(default=0)

    def __srt__(self):

        return self.item_name + self.item_catagory 


class Item_sold(models.Model):

    item = models.ForeignKey(Item_entry, on_delete= models.CASCADE)
    item_quantity = models.IntegerField(default=0)
 
    sell_date = models.DateField()


    # rating_options = (

    #     (1, "Good"), 
    #     (2, "Bad"),
    #     (3, "Not Good"),
    #     (4, "Worst"),
    #     (5, "Excellent "),

    # )

    # rating = models.IntegerField(choices=rating_options)

    # def __str__(self):

    #     return self.restaurent + "Rating :" + str(self.rating)









