import pandas as pd

def area_uni_finder():
    while True:
        area = input("Select the desired area from the dataset: ").strip().lower()
        
        matches = area_uni[area_uni["Area"].str.lower() == area]
        
        if not matches.empty:
            return matches
        else:
            print("Selected area not available. Please select again")

####

def area_check():
    area_list = [a.strip().lower() for a in area_uni['Area'].tolist()]
    input_areas = [a.strip().lower() for a in dt.show_dt_list()]

    while True:
        area = input("Select the area you want to check: ").strip().lower()

        if area not in area_list:
            print("Please insert an available area")
            continue
        else:
            if area in input_areas:
                return "This area has already been inserted"
            else:
                return "This area is yet to be added"

####

def column_check(dt, column_list):
    
    results = []
    
    for col in column_list:
        data = dt[col]
        
        summary = {
            "Column": col,
            "NaN": data.isna().sum(),
            "Zeros": (data == 0).sum(),
            "Unique Values": data.nunique(),
            "Total Values": len(data)
        }
        
        results.append(summary)
    
    return pd.DataFrame(results)

####

def numerical_check(dt, numerical_list):
    results1 =[]

    for col1 in numerical_list:
        data1 = dt[col1]
        
        summary1={
            "Column": col1,
            "Min Value": data1.min(),
            "Max Value":data1.max(),
            "Data Type":data1.dtype
        }

        results1.append(summary1)

    return pd.DataFrame(results1)


def categorical_check(dt, categorical_list):

    results2 = []

    for col2 in categorical_list:

        data2 = dt[col2]

        summary2 = {
            "Column": col2,
            "Leading Spaces": data2.str.startswith(' ').sum(),
            "Trailing Spaces": data2.str.endswith(' ').sum(),
            "Multiple Internal Spaces": data2.str.contains(r'\\s{{2,}}').sum(),
            "First Capital Letter": data2.str[0].str.isupper().sum()
        }

        results2.append(summary2)

    return pd.DataFrame(results2)