# Pokemon TCG Hacks
This is a collection of all the hacks I've created using the pret disassembly of [pokemon TCG](https://github.com/pret/poketcg). This repo will fall behind pret's, only pulling when I want to work on a new hack.

Every hack is set up as a branch of this repo, with _patch\__ as a prefix


## Included Hacks

* [Card Loss Challenge](https://github.com/anmart/poketcg-hacks/tree/patch_CardLossChallenge)
  * First time trying custom menus!
  * Removes cards from your deck after every battle and gives extra booster packs to make up for it


## Below is a duplicate of the original README

### Pokémon TCG

This is a disassembly of Pokémon TCG.

It uses the following ROM as a base:

* Pokémon Trading Card Game (U) [C][!].gbc  `md5: 219b2cc64e5a052003015d4bd4c622cd`

To assemble, first download RGBDS (https://github.com/bentley/rgbds/releases) and extract it to /usr/local/bin.
Copy the above ROM to this directory as "baserom.gbc".
Run `make` in your shell.

This will output a file named "tcg.gbc".


### See Also

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
