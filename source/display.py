from enum import Enum
from utils import cls


class Character(Enum):
    ZERO = """   ###   
  #   #  
 #     # 
 #     # 
 #     # 
  #   #  
   ###   """
    ONE = """   #   
  ##   
 # #   
   #   
   #   
   #   
 ##### """
    TWO = """  #####  
 #     # 
       # 
  #####  
 #       
 #       
 ####### """

    THREE = """  #####  
 #     # 
       # 
  #####  
       # 
 #     # 
  #####  """

    FOUR = """ #       
 #    #  
 #    #  
 #    #  
 ####### 
      #  
      #  """

    FIVE = """ ####### 
 #       
 #       
 ######  
       # 
 #     # 
  #####  """

    SIX = """  #####  
 #     # 
 #       
 ######  
 #     # 
 #     # 
  #####  """

    SEVEN = """ ####### 
 #    #  
     #   
    #    
   #     
   #     
   #     """

    EIGHT = """  #####  
 #     # 
 #     # 
  #####  
 #     # 
 #     # 
  #####  """

    NINE = """  #####  
 #     # 
 #     # 
  ###### 
       # 
 #     # 
  ##### """

    COLON = """  #  
 ### 
  #  
     
  #  
 ### 
  #  """


characters_mapping = {
    "0": Character.ZERO,
    "1": Character.ONE,
    "2": Character.TWO,
    "3": Character.THREE,
    "4": Character.FOUR,
    "5": Character.FIVE,
    "6": Character.SIX,
    "7": Character.SEVEN,
    "8": Character.EIGHT,
    "9": Character.NINE,
    ":": Character.COLON,
}


def clear_screen():
    cls()


def print_clock(minutes: int, seconds: int):
    clear_screen()
    if seconds not in range(0, 60):
        raise Exception("seconds must be in range [0, 60)")

    minutes = [characters_mapping[character] for character in str(minutes).zfill(2)]
    divider = [Character.COLON]
    seconds = [characters_mapping[character] for character in str(seconds).zfill(2)]

    print_line(characters=minutes + divider + seconds)


def print_line(characters: list = [Character]):
    characters = [character.value.split("\n") for character in characters]

    def get_nth_line(n):
        return "".join([character_line[n] for character_line in characters])

    print("\n".join([get_nth_line(n) for n in range(7)]))
