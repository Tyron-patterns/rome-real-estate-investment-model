import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from io import StringIO


class RealListing:
    def __init__(self, area):
        self.area = area
        self.df = pd.DataFrame(columns = ["Area", "Street", "ID_Number",  "Price", "Surface", "N. of Rooms", 
                                          "N. of Bathrooms", "External Area", "External Surface", "Floor", "Levels", 
                                          "Parking Space", "Furnished", "Conditions", "Property"])
        

    
    def characteristics(self, street, price, mq, rooms, bathrooms, exteriors, ex_surface, floor, levels, 
                        parking, furnished, conditions, construction_year, proprieta):
        # street_id = street.split()[1]
        # try:
        #     street_id = street.split()[1]
        # except IndexError:
        #     street_id = street.split()[0]

        street_id = street.split()[-1]
        area_id = self.area.split()[-1]
        
        flat_id = self.area[0:3] + "_" + street_id[0:3] + "_" + str(len(self.df)+1)

        if (self.df["Street"] == street).any():
            while True:
                print("Careful, this street name has already been added")
                keep_on = input("Do you still want to insert the record?: Y or N").lower()
    
                if keep_on == "y":
                    break
    
                elif keep_on == "n":
                    return
            
        if (self.df["ID_Number"] == flat_id).any():
            print("The apartment at this id has been already inserted!")
            return

        else:
            column = {"Area": self.area, "Street": street, "ID_Number": flat_id, "Price": price * 1000, 
                      "Surface":mq, "N. of Rooms": rooms, "N. of Bathrooms": bathrooms, "External Area": exteriors,
                      "External Surface": ex_surface, "Floor": floor, "Levels": levels, "Parking Space": parking, "Furnished": furnished, 
                      "Conditions": conditions, "Construction Year": construction_year, "Property": proprieta}
            df2 = pd.DataFrame([column])
            self.df = pd.concat([self.df, df2], axis = 0, ignore_index = True)
            return self.df

    def dataset(self):
        return self.df

    def delete_last_row(self):
        self.df = self.df.drop(self.df.index[-1])

    def delete_row(self, row_index):
        self.df = self.df.drop(row_index)
        

    def characteristics1(self):
        rows = []
        for i in range(11):
            print(f"Insert the characteristics of the apartment for apartment {i}: \n")
            area = input(f"Insert area for aparment {i}: \n")
            street = input(f"Insert street for aparment {i}: \n")
            mq = int(input(f"Insert surface for aparment {i}: \n"))
            rooms = int(input(f"Insert number of rooms for aparment {i}:\n"))
            price = int(input(f"Insert prices for aparment {i}: \n"))
            floor = int(input(f"Insert floor for aparment {i}: \n"))
            furnished = input(f"Insert furnished for aparment {i}: \n")
            row = {"Area": area, "Street": street, "Surface":mq, 
                                              "N. of Rooms": rooms, "Price": price,
                                              "Floor": floor, "Furnished": furnished}
            rows.append(row)            
        self.df = pd.DataFrame(rows)
        return self.df