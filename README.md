# ZDF: Zombie Defense Force

**A text-based zombie survival and rebuilding adventure built with Python.**

Five months after a mysterious infection devastated the country, you arrive at **Mysthaven**, a once-thriving town filled with abandoned homes, farms, shops, a clinic, and an industrial district. Zombies wander its streets, supplies are scarce, and the infrastructure is failing.

Your objective isn't simply to fight the undead. It's to **survive, gather resources, and eventually rebuild a safe community**.

> **Development status:** Early playable prototype. The current program includes an introduction, instructions, a player status display, and four starting routes into Mysthaven. Exploration, base building, quests, inventory, combat, and the full survival loop have not yet been implemented.

## Requirements

- Python 3 (no external packages required)
- A terminal, command prompt, or Python-compatible editor

## How to Run

1. Save the game code in a file such as `zdf.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python zdf.py
   ```

   On some systems, use `python3 zdf.py` instead.
4. Read the introduction and press **Enter** when prompted.
5. Select an entry route by typing **1**, **2**, **3**, or **4**, then press **Enter**.
6. View your updated character stats. Press **Enter** to end the current prototype.

## Story

The world's electrical grid has failed. Food and clean water are increasingly difficult to find, and scattered survivors struggle to stay alive. After weeks of searching, your group discovers Mysthaven—a town that offers something you haven't had for months: **a chance to rebuild**.

In the planned full game, you'll need to use your knowledge and survival skills to establish shelter, explore buildings, recover supplies, and maintain a long-term base.

## Starting Player Stats

| Statistic | Initial Value | Description |
| --- | --- | --- |
| Health | `100 / 100` | Your current physical condition |
| Food | `20 / 100` | Hunger / food status |
| Water | `50 / 100` | Hydration status |
| Time | `800` | In-game time counter (not yet formatted or advanced as a clock) |
| Day | `0` | Current day counter |
| Infection | `0` | Infection status |
| Weapon | `tire Iron` | Your starting weapon |

The game displays status messages as health, food, and water levels change. For example, low health may produce bleeding or critical-injury warnings, while low food and water generate hunger and thirst warnings.

**Current limitation:** The `display_statistics()` function attempts to subtract health when food or water is zero, but those changes are made only to a local variable and are not saved to the main `health` value. Persistent starvation and dehydration damage still need to be implemented.

## How to Play

The intended gameplay emphasizes **survival over combat**. Players will need to find shelter, manage food and water, explore Mysthaven, and eventually build and maintain a base.

The instructions in the game describe these **planned controls**:

| Key | Intended Function | Available Now? |
| --- | --- | --- |
| `C` | Check character status | Not yet (stats display automatically at set points) |
| `I` | Open inventory | Not yet |
| `Q` | View objectives and quests | Not yet |

The game also describes an intended 24-hour day with six hours of sleep, plus risks of zombie or raider attacks when sleeping in unsafe locations. **The sleep system, automatic sleep at the 18-hour mark, day rollover, and sleep encounters are not yet coded.**

## Entering Mysthaven

At the beginning of the game, choose one of four ways into town. Each route has a unique introductory scene and affects your stats.

| Choice | Entry Route | Encounter | Changes |
| --- | --- | --- | --- |
| `1` | Main Street from the North | Discover a damaged, stained bag near the welcome sign | Time `+10`, Food `-2`, Water `-4` |
| `2` | Trucktrail Road from the West | Spot two suspicious figures on an old farm road | Time `+15`, Food `-2`, Water `-4` |
| `3` | Railroad Tracks from the South | Fall and scrape yourself while approaching a neighborhood | Time `+5`, Health `-2`, Food `-2`, Water `-4` |
| `4` | First Avenue from the East | Enter a commercial district with wrecked vehicles and wandering zombies | Time `+5`, Food `-2`, Water `-4` |

Each route currently shows narrative text and applies its listed changes. The scenes do **not** yet continue into additional decisions or encounters.

If you enter anything other than `1`–`4`, the program prints an invalid-choice message but does not ask you to choose again.

## Current Features

- Text-based introduction and setting
- Player statistics and condition warnings
- Starting equipment (tire iron)
- Four entry locations with distinct descriptions
- Basic stat changes based on your chosen route
- Interactive **Enter** prompts between sections

## Planned Features

These are concepts described by the current game instructions or natural directions for expanding the prototype, **not features already implemented**:

- Room-by-room exploration of homes, stores, farms, and industrial buildings
- Scavenging, inventory management, and item use
- Food, hydration, injury, and infection systems
- An actual clock, day progression, and sleep/rest mechanics
- Safe houses, shelter construction, and base improvements
- Crafting, repairs, and infrastructure rebuilding
- Objectives, quests, and survivor interactions
- Random zombie and raider encounters
- Combat with an emphasis on avoiding unnecessary risk
- Saving and loading progress

## Code Structure

The prototype is organized into these main parts:

1. **Initial variables:** Sets starting health, food, water, time, day, infection, and weapon.
2. **`display_statistics(...)`:** Prints player statistics and condition warnings.
3. **Title and introduction:** Establishes the story and world of Mysthaven.
4. **How to Play:** Explains the intended mechanics and keyboard shortcuts.
5. **Route selection:** Uses `input()` and an `if` / `elif` chain to choose one of four entry scenes.
6. **Final status and exit:** Displays updated stats, then ends the prototype.

## Known Limitations

- The game ends immediately after the entry-route scene and second status display.
- Status shortcuts (`C`, `I`, `Q`) are described but do not work yet.
- Time is modified as a number (for example, `800 + 15 = 815`); there is no working HH:MM clock or day rollover.
- The displayed starvation/dehydration health deductions are not retained after `display_statistics()` returns.
- Stat values are not clamped to the range `0`–`100`.
- Invalid entry choices are not retried.
- The current version has no save system, combat loop, inventory, quest tracking, or full base-building mechanics.

## Project Goal

Build a survival game in which players use **planning, resource management, engineering, and STEM problem-solving** to turn the abandoned town of Mysthaven into a place where survivors can live again.

**Survive. Explore. Rebuild.**
