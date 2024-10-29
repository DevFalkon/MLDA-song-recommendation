import pandas as pd
root_dir = "dataset/"

def get_song_id(song_name, artist_name):
    df_file = root_dir+"dataset.csv"
    df = pd.read_csv(df_file, encoding='utf-8')

    for idx, row in df.iterrows():
        if row['title'].lower() == song_name.lower():
            for artist in row['artists'][1:-1].split(','):
                if artist[1:-1].lower() == artist_name.lower():
                    return row['id']
    return


def row_to_list(row):
    row = row.split("\"")
    singers = row[1].split("'")
    row = [i.split("\'")[1] for i in row]
    row[1] = singers[1:-1:2]
    return row

def get_recom(id):
    save_file = root_dir+"similarity_data.txt"
    dataset_file = root_dir+"dataset.csv"
    dataset = pd.read_csv(dataset_file, encoding='utf-8')

    song_title = dataset.iloc[id]['title']
    song_artist = dataset.iloc[id]['artists'].split("'")[1:-1:2]


    with open(save_file, 'r', encoding='utf-8') as file:
        similarity_data = file.read().split('\n')
        similar_titles = similarity_data[id]
        similarity_list = []
        for row in similar_titles.split("(")[1:]:
            if row:
                row = row_to_list(row)
                if song_title.lower() not in row[0].lower():
                    add = True
                    for val in similarity_list:
                        if row[0].lower() in val[0].lower():
                            add = False
                    if len(similarity_list) > 4:
                        file.close()
                        return similarity_list
                    if add:
                        similarity_list.append(row)
    return

if __name__=="__main__":
    print(get_recom(10))
