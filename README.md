# Rock Paper Scissors
Simple Rock Paper Scissors game on Python 3 console.

<p align="center">
  <img alt="Github language counter" src="https://img.shields.io/github/languages/count/weltonfelix/RockPaperScissors?color=%2304D361">

  <img alt="Repo size" src="https://img.shields.io/github/repo-size/weltonfelix/RockPaperScissors">
	
  <a href="https://www.github.com/weltonfelix">
    <img alt="Made by Welton" src="https://img.shields.io/badge/Made%20by-Welton-%2304D361">
  </a>

  <a href="https://github.com/weltonfelix/RockPaperScissors/commits/master">
    <img alt="Last commit" src="https://img.shields.io/github/last-commit/weltonfelix/RockPaperScissors">
  </a>

  <a href="https://github.com/weltonfelix/RockPaperScissors/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/weltonfelix/RockPaperScissors">
  </a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
</p>

## :wrench: How it works?
  I used random library to randomize computer choice.
  The user types his option, a logical test is performed to know the result and what should be printed on screen. If the user inputs one of the key-words (```stopOptions = ["Parar", "Encerrar","Finalizar", "Pare", "Fim"]```) choosed to stop the game, the game is stopped and the final results is shown.
  
  <h3 align="center">
  	<img src="./gameexample.svg" alt="Game" title="Game" width="50%"/>
  </h3>
  
### :bulb: Easter Eggs
  The game has some easter eggs from the tv show "The Big Bang Theory". The user can also choose "Lizard" or "Spock": ``` possibleChoices = [rock, paper, scissors, lizard, spock] ```
  However, the computer cannot choose the easter eggs objects, so interactions between "Lizard" and "Spock" are not available.
  
## :notebook: Rules:
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

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/weltonfelix/RockPaperScissors/issues).
- Make a fork;
- Create a branck with your feature: `git checkout -b my-feature`;
- Commit changes: `git commit -m 'feat: My new feature'`;
- Make a push to your branch: `git push origin my-feature`.

After merging your receipt request to done, you can delete a branch from yours.

## Show your support

Give a ⭐️ if this project helped you!

## :memo: License

This project is under the MIT license. See the [LICENSE](LICENSE.md) for details.

---

Made with ♥ by Welton Felix :wave: [Get in touch!](mailto:contato.weltonf@gmail.com)
