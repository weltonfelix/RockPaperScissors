# Rock Paper Scissors
Simple Rock Paper Scissors game on Python 3 console.

## How it works?
  I used random library to randomize computer choice.
  The user types his option, a logical test is performed to know the result and what should be printed on screen. If the user inputs one of the key-words (```stopOptions = ["Parar", "Encerrar","Finalizar", "Pare", "Fim"]```) choosed to stop the game, the game is stopped and the final results is shown.
  
### Easter Eggs
  The game has some easter eggs from the tv show "The Big Bang Theory". The user can also choose "Lizard" or "Spock": ``` possibleChoices = [rock, paper, scissors, lizard, spock] ```
  However, the computer cannot choose the easter eggs objects, so interactions between "Lizard" and "Spock" are not available.
  
## Rules:
  1. Equal objects tie.
  2. Diferent objects:
     1. Rock
          * Is covered by the _Paper_ **(-)**           
          * Crushes _Scissors_ __(+)__           
          * Crushes _Lizard_ **(+)**           
          * Is vaporized by _Spock_ __(-)__          
     2. Paper
          * Covers _Rock_ **(+)**
          * Is cutted by _Scissors_ **(-)**
          * Is eated by the *Lizard* **(-)**
          * Disproves _Spock_ __(+)__          
     3. Scissors
          * Is crushed by the *Rock* __(-)__
          * Cuts the *Paper* **(+)**
          * Decapitates the _Lizard_ __(+)__
          * Is smashed by _Spock_ __(-)__      
     4. Lizard
          * Is crushed by the *Rock* __(-)__
          * Eats the _Paper_ **(+)**
          * Is decapitated by *Scissors* **(-)**
          * ~~Poisons *Spock* **(+)**~~ *(As the computer cannot choose easter egg options, this option is unavailable)*      
     5. Spock
          * Vaporizes the _Rock_ __(+)__
          * Is disproved by the _Paper_ **(-)**
          * Smashes the _Scissors_ **(+)**
          * ~~Is poisoned by the _Lizard_ **(-)**~~ *(As the computer cannot choose easter egg options, this option is unavailable)*
