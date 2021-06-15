import pandas as pd
import sqlalchemy as alch
import numpy as np
from getpass import getpass
import tools.cleaning as cle

simpsons_data = pd.read_csv("./data/simpsons_script_lines.csv")

simpsons_relevant_data = simpsons_data.copy()

simpsons_relevant_data.drop(["id", "number", "raw_text", "speaking_line", "normalized_text", "word_count"], axis = 1, inplace = True)
cle.drop_nan(simpsons_relevant_data)

simpsons_relevant_data.to_csv("./data/simpsons_relevant_data.csv", index = False)

simpsons_phrases = simpsons_relevant_data[['episode_id', 'character_id', 'raw_character_text', 'spoken_words']].sort_values(by = 'episode_id')

simpsons_phrases['raw_character_text'].replace(['"Just Stamp the Ticket" Man'], np.nan, inplace = True)

cle.drop_nan(simpsons_phrases)

cle.replace(simpsons_phrases, 'raw_character_text', r"[\"]", r"'")

cle.replace(simpsons_phrases, 'spoken_words', r"[\"]", r"'")

cle.replace(simpsons_phrases, 'spoken_words', "%", "per cent")

cle.create_index(simpsons_phrases)

simpsons_phrases.to_csv("./data/simpsons_phrases.csv", index = False)

simpsons_characters2 = simpsons_phrases[['character_id', 'raw_character_text']]

characters_grouped = simpsons_characters2.groupby('character_id')

characters_grouped = characters_grouped.first()

characters_grouped.reset_index(inplace=True)

characters_grouped.drop_duplicates(subset = ['raw_character_text'], keep = 'first', inplace = True) 

cle.replace(characters_grouped, 'raw_character_text', r"[\/]", "")

characters_grouped['character_id'] = characters_grouped['character_id'].apply(pd.to_numeric)

characters_grouped.sort_values(by='character_id', ascending = True, inplace = True)

characters_grouped.drop_duplicates(subset = ['character_id'], keep = 'first', inplace = True) 

characters_grouped.to_csv("./data/simpsons_characters.csv", index = False)

password = getpass("Introduce tu pass de sql: ")
dbName="The_simpsons"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"

engine = alch.create_engine(connectionData)
print("Conected")

