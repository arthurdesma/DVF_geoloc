import pandas as pd

start = 2014
end = 2017


dtype_dict = {
    'Identifiant de mutation (Etalab)': 'str',
    'Date de la mutation': 'str',
    'Numéro de disposition': 'str',
    'Nature de la mutation': 'str',
    'Valeur foncière': 'float64',
    'Numéro de voie': 'float64',
    'Suffixe du numéro (bis/ter)': 'str',
    'Nom de la voie': 'str',
    'Code Fantoir/Rivoli de la voie': 'str',
    'Code postal': 'str',
    'Code INSEE de la commune': 'str',
    'Nom de la commune': 'str',
    'Code INSEE du département': 'str',
    'Ancien code de la commune': 'str',
    'Ancien nom de la commune': 'str',
    'Identifiant de la parcelle cadastrale': 'str',
    'Ancien identifiant de la parcelle cadastrale': 'str',
    'Numéro du volume': 'str',
    'Numéro du lot 1': 'str',
    'Surface Carrez du lot 1': 'float64',
    'Numéro du lot 2': 'str',
    'Surface Carrez du lot 2': 'float64',
    'Numéro du lot 3': 'str',
    'Surface Carrez du lot 3': 'float64',
    'Numéro du lot 4': 'str',
    'Surface Carrez du lot 4': 'float64',
    'Numéro du lot 5': 'str',
    'Surface Carrez du lot 5': 'float64',
    'Nombre de lots': 'int32',
    'Code du type de local': 'str',
    'Type de local': 'str',
    'Surface réelle du bâti': 'float64',
    'Nombre de pièces principales': 'float64',
    'Code de la nature de culture': 'str',
    'Nature de culture': 'str',
    'Code de la nature de culture spéciale': 'str',
    'Nature de culture spéciale': 'str',
    'Surface du terrain': 'float64',
    'Longitude': 'float64',
    'Latitude': 'float64'
}

columns_to_drop = [
    'Code Officiel EPCI', 'Nom Officiel EPCI',
    'Nom du département', 'Code INSEE de la région', 'Nom de la région',
    'Géolocalisation'
]

rename_dict = {
    'Identifiant de mutation (Etalab)': 'id_mutation',
    'Date de la mutation': 'date_mutation',
    'Numéro de disposition': 'numero_disposition',
    'Nature de la mutation': 'nature_mutation',
    'Valeur foncière': 'valeur_fonciere',
    'Numéro de voie': 'adresse_numero',
    'Suffixe du numéro (bis/ter)': 'adresse_suffixe',
    'Nom de la voie': 'adresse_nom_voie',
    'Code Fantoir/Rivoli de la voie': 'adresse_code_voie',
    'Code postal': 'code_postal',
    'Code INSEE de la commune': 'code_commune',
    'Nom de la commune': 'nom_commune',
    'Code INSEE du département': 'code_departement',
    'Ancien code de la commune': 'ancien_code_commune',
    'Ancien nom de la commune': 'ancien_nom_commune',
    'Identifiant de la parcelle cadastrale': 'id_parcelle',
    'Ancien identifiant de la parcelle cadastrale': 'ancien_id_parcelle',
    'Numéro du volume': 'numero_volume',
    'Numéro du lot 1': 'lot1_numero',
    'Surface Carrez du lot 1': 'lot1_surface_carrez',
    'Numéro du lot 2': 'lot2_numero',
    'Surface Carrez du lot 2': 'lot2_surface_carrez',
    'Numéro du lot 3': 'lot3_numero',
    'Surface Carrez du lot 3': 'lot3_surface_carrez',
    'Numéro du lot 4': 'lot4_numero',
    'Surface Carrez du lot 4': 'lot4_surface_carrez',
    'Numéro du lot 5': 'lot5_numero',
    'Surface Carrez du lot 5': 'lot5_surface_carrez',
    'Nombre de lots': 'nombre_lots',
    'Code du type de local': 'code_type_local',
    'Type de local': 'type_local',
    'Surface réelle du bâti': 'surface_reelle_bati',
    'Nombre de pièces principales': 'nombre_pieces_principales',
    'Code de la nature de culture': 'code_nature_culture',
    'Nature de culture': 'nature_culture',
    'Code de la nature de culture spéciale': 'code_nature_culture_speciale',
    'Nature de culture spéciale': 'nature_culture_speciale',
    'Surface du terrain': 'surface_terrain',
    'Longitude': 'longitude',
    'Latitude': 'latitude'
}

for year in range(start, end+1):
    filename = f"data/buildingref-france-demande-de-valeurs-foncieres-geolocalisee-millesime_{year}.csv"
    df_global = pd.read_csv(filename, delimiter=';', encoding='utf-8', dtype=dtype_dict)
    
    df_global.rename(columns=rename_dict, inplace=True)
    df_global.drop(columns=columns_to_drop, inplace=True)
    
    output_filename = f"data/full_{year}.csv"
    df_global.to_csv(output_filename, index=False)
