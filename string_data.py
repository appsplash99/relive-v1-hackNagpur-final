# from pprint import pprint
from data import generate_DATA

# # storing hospitals data
stored_list_data = generate_DATA()

# HTML START 
page_start_html = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>MyFlaskApp</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="static/styles/styles.css"></head><body style="margin-top: 80px;"><h1> NEARBY HOSPITALS </h1>'''

# HTML END
page_end_html = '''<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script></body></html>'''



# Equivalent data
# stored_list_data = [{'1name': ('Ruby Hall Clinic',),
#                       '2local_phone_num': ('020 2616 3391',),
#                       '3international_phone_num': ('+91 20 2616 3391',)},
#                     {'1name': ('Mukundrao Lele Hospital',),
#                       '2local_phone_num': (None,),
#                       '3international_phone_num': (None,)}]


# function to convert list data into html equivalent
# pprint(stored_list_data)
def generate_Data_to_HTML():
    # final string to be returned into html
    final_string = []

    start_string = "<div><ul><li style='text-decoration: none; '>"
    end_string = "</li></ul></div>"

    for item in stored_list_data:

        # single div block which must contain html info of each place
        each_div = []

        # add start_string at first iteration
        each_div.append(start_string)

        # print('FIRST ITEM\n\n')
        try:
            place_name      = ''.join(item['1name']).strip("'()")                           # place name
            place_local_num = ''.join(item['2local_phone_num']).strip("'(),")               # place local num
            place_inter_num = ''.join(item['3international_phone_num']).strip("'(),")       # place inter num
        # if None found convert into equivalent string
        except:
            place_local_num = 'Number Not given'
            place_inter_num = 'Number Not given'
        
        # place_name_html
        place_name_html = f'<p>{place_name}</p>'
        each_div.append(place_name_html)

        # place_local_num_html
        place_local_num_html = f"<a href='tel:{place_local_num}'><button class='button'>{place_local_num}</button></a>"
        each_div.append(place_local_num_html)

        # place_inter_num_html
        place_inter_num_html = f"<a href='tel:{place_inter_num}'><button class='button'>{place_inter_num}</button></a>"
        each_div.append(place_inter_num_html)

        # at last iteration append end_string
        each_div.append(end_string)

        # convert each_div into string and append into final_string
        final_string.append(''.join(each_div))

    ### At the end convert final string list into a list

    final_string_html = page_start_html  + ''.join(final_string) + page_end_html

    # print(final_string_html)
    ### Returning final value
    return final_string_html




