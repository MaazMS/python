def total_count(total):
    if  0<= total <=100:
         page_number= 2
    else:
        if 101<= total <=200:
            page_number= 3
        else:
            if 201<= total <=300:
                page_number= 4
            else:
                if 301<= total <=400:
                    page_number= 5
                else:
                    if 401<= total <=500:
                        page_number= 6
                    else:
                        if 501 <= total <= 600:
                            page_number = 7
                        else:
                            if 601 <= total <= 700:
                                page_number = 8
                            else:
                                if 701 <= total <= 800:
                                    page_number = 9
                                else:
                                    if 801 <= total <= 900:
                                        page_number = 10
                                    else:
                                        if 901 <= total <= 1000:
                                            page_number = 11

    for number in range(1, page_number):
        print(number)
    return page_number

page = total_count(800)
print(page)