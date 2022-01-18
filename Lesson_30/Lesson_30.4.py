from Lesson_30_3_5 import *
all_store = Shop(n,m,k,q,w)
all_store.describe_shop(n,m)
all_store.number_of_units(k)
all_store.set_number_of_units(q)
all_store.increment_number_of_units(w)
all_store = Discount(n,m,k,q,w,z)
all_store.get_discounts_products(z)