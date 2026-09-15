import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from io import StringIO


class OmiScraper:
    #creates the attribute cemplete_dt, which contains the individual dataframes for each area (from previous dtaframes or new ones)
    def __init__(self, initial_data = None):
        if initial_data is None:
            self.complete_dt = {}
        else:
            self.complete_dt = initial_data

        self.df = pd.DataFrame()

        if self.complete_dt:
            self.flatten_all()

    
    #Shows in one output every individual dataframes for each area
    def show_dts(self):
        self.dt_list = []
        for key in self.complete_dt:
            self.dt_list.append(key)
            self.dt = self.complete_dt[key]
            print("\n ------------------------------------------------------ \n")
            print(f"This is the dataframe for {key}\n")
            display(self.dt)
        print(self.dt_list)

        
    #Shows a dataframe for the areas/dataframes uploaded so far
    def show_dt_list(self):
        self.area_dataframe = pd.DataFrame(self.complete_dt.keys())
        print(f"The list of the available areas is: \n")
        return list(self.complete_dt.keys())

        
    #Concatenates every dataframe into a bigger database
    def current_dt(self):
        return self.df


    def flatten_columns(self, df):
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [
                col[0] if col[0] == col[1] or col[1] == ""
                else f"{col[0]} - {col[1]}"
                for col in df.columns
            ]
        return df
    
    
    def flatten_all(self):
        # flatten stored dataframes
        for key in self.complete_dt:
            self.complete_dt[key] = self.flatten_columns(self.complete_dt[key])
    
        # rebuild df
        if self.complete_dt:
            self.df = pd.concat(self.complete_dt.values(), ignore_index=True)
        else:
            self.df = pd.DataFrame()

    
    #Adds the name of the area, uploads the original table and adds the additional necessary info for the given dataframe
    def add_dt_col(self, area_name, html_table, zona, codice_zona, microzona_catastale, tipologia_prevalente):
        #Checks if the inserted parameters are already present

        if area_name in self.complete_dt:
            return f"The value {area_name} is already present"

        prices_area = pd.read_html(StringIO(html_table))[0]
        prices_area = self.flatten_columns(prices_area)

        #Checks if the html_code introduced produces the same dataframe
        for areas in self.complete_dt.values():
            if prices_area.equals(areas[prices_area.columns]):
                return "This html code was already used!"
                    
        for key, df in self.complete_dt.items():
            if zona == df["Fascia/Zona"].iloc[0]:
                return f"The value {zona} is already present in  {key}"
                
            if codice_zona == df["Codice Zona"].iloc[0]:
                return f"The value {codice_zona} is already present in  {key}"
                
            # if microzona_catastale == df["Microzona Catastale"].iloc[0]:
            #     return f"The value {microzona_catastale} is already present in {key}"

        column_values = {
        'Area': area_name,            
        'Province': 'Rome',
        'Municipality': 'Fiumicino',
        'Fascia/Zona': zona,
        'Codice Zona': codice_zona,
        'Microzona Catastale': microzona_catastale,
        'Tipologia prevalente': tipologia_prevalente,
        'Destinazione': 'Residenziale',
        }
        prices_area = prices_area.assign(**column_values)
        self.complete_dt[area_name] = prices_area
        self.df = pd.concat(self.complete_dt.values(), axis =0 , ignore_index = True)
        return prices_area

    def drop_area(self, area_to_drop):
        self.complete_dt.pop(area_to_drop, None)
        self.df = self.df[self.df['Area'] != area_to_drop]
        print(self.df.columns)

    def drop_last_area(self):
        last_area = list(self.complete_dt.keys())[-1]
        self.complete_dt.pop(last_area)
        self.df = self.df[self.df['Area'] != last_area]
        print(self.df.columns)