from operator import truediv


a = ("дед","слово","вода", "потоп", "река","топот")
def polind(x):
    revers = "".join(reversed(x))
    if revers == x:
        return True
    else:
        return False   
#print(polind("дед"))
filt = tuple(filter(polind,a))
print(filt)
    



