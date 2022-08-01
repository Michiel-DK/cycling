def get_sequences(df, name, year, tour, weeks=52):
    
    #get tour data
    tour_data = df[(df['name'] == name) & (df['year'] == year) & (df['race_name'] == tour)].sort_values(by='date')
    y = tour_data[['date', 'points']].set_index('date')
    X_decoder = tour_data[['date', 'distance', 'ProfileScore:', 'Vert. meters:', 'Startlist quality score:']].set_index('date')
    
    season_data = df[(df['name'] == name) & (df['date'] < min(tour_data['date'])) & (df['date'] >= min(tour_data['date']) - datetime.timedelta(weeks=weeks))].sort_values(by='date')
    X_encoder = season_data[['date', 'points', 'distance', 'ProfileScore:', 'Vert. meters:', 'Startlist quality score:']].set_index('date')
    
    return X_encoder, X_decoder, y

