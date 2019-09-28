# Pokémon TCG Card Replacement Hack
---
![Screenshot: Settings Menu](https://i.imgur.com/J9bZhTd.png) ![Screenshot: Card Loss Screen](https://i.imgur.com/zMQ6GJO.png) ![Screenshot: Warning](https://i.imgur.com/Gk4P0TB.png)

This hack aims to force you to change up your deck every time you battle. After you lose, you'll lose somewhere between 1-9 cards (configurable) and receive an extra 1-9 booster packs (configurable). As a result, you'll need to make changes to your deck to make sure it still works well, or at all!


This hack was made to demonstrate what is possible with the disassembly in its current state, and maybe provide a source for would-be asmhackers to start and learn ~~awful practices~~ from. There are a few aspects to this, separated into different commits to make it easier to see how different features work.


## Features
---
* Removes X Pokemon or Trainers from your deck and collection at the end of battle
* Gives X extra booster packs after battle
* Custom Menu
    * Lets you select how many pokemon you lose at the end of a battle
    * Lets you select how many extra boosters to receive after battle
* Custom Screen showing what cards were lost when battle ended
* Custom Overworld Script that executes if you don't have any pokemon in your deck
    * Note: this uses a currently undocumented function to check basic pokemon amount.
* No Tutorial
* A couple minor easter eggs

## Make
---
To make this project, follow the original instructions for pokemon TCG by pret


*The following is the original README packaged with pret's disassembly:*
This is a disassembly of Pokémon TCG.

It uses the following ROM as a base:

* Pokémon Trading Card Game (U) [C][!].gbc  `md5: 219b2cc64e5a052003015d4bd4c622cd`

To assemble, first download RGBDS (https://github.com/bentley/rgbds/releases) and extract it to /usr/local/bin.
Copy the above ROM to this directory as "baserom.gbc".
Run `make` in your shell.

This will output a file named "tcg.gbc".


# See Also

* Disassembly of [**Pokémon Red/Blue**][pokered]
* Disassembly of [**Pokémon Yellow**][pokeyellow]
* Disassembly of [**Pokémon Gold**][pokegold]
* Disassembly of [**Pokémon Crystal**][pokecrystal]
* Disassembly of [**Pokémon Pinball**][pokepinball]
* Disassembly of [**Pokémon Ruby**][pokeruby]
* Disassembly of [**Pokémon Fire Red**][pokefirered]
* Disassembly of [**Pokémon Emerald**][pokeemerald]
* Discord: [**pret**][Discord]
* irc: **irc.freenode.net** [**#pret**][irc]

[pokered]: https://github.com/pret/pokered
[pokeyellow]: https://github.com/pret/pokeyellow
[pokegold]: https://github.com/pret/pokegold
[pokecrystal]: https://github.com/pret/pokecrystal
[pokepinball]: https://github.com/pret/pokepinball
[pokeruby]: https://github.com/pret/pokeruby
[pokefirered]: https://github.com/pret/pokefirered
[pokeemerald]: https://github.com/pret/pokeemerald
[Discord]: https://discord.gg/6EuWgX9
[irc]: https://kiwiirc.com/client/irc.freenode.net/?#pret
