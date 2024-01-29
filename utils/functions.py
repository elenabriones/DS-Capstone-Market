#funcion para obtener 3 listas de variables dependiendo del tipo que son
def obtener_lista_variables(dataset, target):
  lista_num = []
  lista_bool = []
  lista_cat = []

  for i in dataset:
    if ((dataset[i].dtype.kind in('i','u','f'))) and i not in target and len(dataset[i].unique())!=2 :
      lista_num.append(i)
    elif ((dataset[i].dtype.kind in('i','u','f'))) and i not in target and len(dataset[i].unique())==2:
      lista_bool.append(i)
    elif ((dataset[i].dtype.kind=='b') ) and i not in target:
      lista_bool.append(i)
    elif ((dataset[i].dtype.kind=='O') ) and i not in target:
      lista_cat.append(i)
  return lista_num, lista_bool, lista_cat

#funcion para coger mas informacion sobre el tipo de fecha
def get_dateinfo (dataset, list_datecol):
    for col in list_datecol:
        dataset[col + '_HOUR'] = dataset[col].dt.hour
        dataset[col + '_DAYNAME'] = dataset[col].dt.day_name()
        dataset[col + '_WEEKDAYNAME'] = dataset[col].dt.weekday_name
        dataset[col + '_DAY'] = dataset[col].dt.day
        dataset[col + '_MONTH'] = dataset[col].dt.month

    return dataset

# funcion obener la yearweek
def obtener_yearweek (df, date_column_name):
  lista_num = []
  lista_bool = []
  lista_cat = []

  for i in dataset:
    if ((dataset[i].dtype.kind in('i','u','f'))) and i not in target and len(dataset[i].unique())!=2 :
      lista_num.append(i)
    elif ((dataset[i].dtype.kind in('i','u','f'))) and i not in target and len(dataset[i].unique())==2:
      lista_bool.append(i)
    elif ((dataset[i].dtype.kind=='b') ) and i not in target:
      lista_bool.append(i)
    elif ((dataset[i].dtype.kind=='O') ) and i not in target:
      lista_cat.append(i)
  return lista_num, lista_bool, lista_cat

