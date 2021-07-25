print("""python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
""")



order_list=["wings","cookies","spring rolls","salmon","steak","meat tornado","a literal garden","ice cream","cake","pie","coffee","tea","unicorn tears"]
user_order_list=[]
loop=True


while loop:
    user_input = input("""** What would you like to order? **
***********************************""").lower()


    if user_input=="quit":
        loop=False
        if user_order_list==[]:
            print("You should try our meals next time :)")
        else:
            print(f'Your final order: {len(user_order_list)} orders contain ({order_details})')


    elif user_input in order_list:
        user_order_list.append(user_input)
        order_details =''

        for i in user_order_list:
            if order_details =='':
                order_details = i
            else:
                order_details = f'{order_details} + {i}'

        print(f'{len(user_order_list)} orders contain ({order_details}) have been added to your meal')


    else:
        print(f'Your order: {user_input} doesn\'t exist, but sure we will afford it ASAP')

