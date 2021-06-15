from config.configuration import engine
import tools.getdata as get



def insert_character(name):
    """
    This function inserts a new character in the database.
    Arg: Name of the character.
    Returns: The inserted name. 
    """
    engine.execute(f"""
    INSERT IGNORE INTO characters (name) VALUES
    ('{name}');
    """
    )
    return get.get_name(name)


def insert_phrase(episode_id, character_id, phrase):
    """
    This function inserts a new character in the database. 
    Args: Episode_id, character_id and phrase
    Returns: A message saying that the data has been added to the database. 
    """
    engine.execute(f"""
    INSERT INTO phrases (episode_id, character_id, phrase) VALUES
    ({episode_id}, {character_id}, '{phrase}');               
    """
    )
    return "The info has been added to the database"

def delete_character(name):
    """
    This function deletes a character from the database. 
    Arg: Name of the character to delete. 
    Returns: A message saying that the character has been deleted. 
    """
    engine.execute(
        f"""
        DELETE FROM characters
        WHERE name = "{name}"; 
        """
    )
    return "The character has been deleted from the database"

def delete_phrase(phrase):
    """
    This function deletes a phrase from the dataset. 
    Arg: The phrase to delete. 
    Returns: A message saying that the phrase has been deleted from the database.
    """
    engine.execute(
        f"""
        DELETE FROM phrases
        WHERE phrase = '{phrase}';
        """
    )
    return "The phrase has been deleted from the database"


