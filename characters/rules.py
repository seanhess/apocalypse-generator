# from typing import Callable

class Move:
  name:str = ""
  rules:str = ""
  examples:list[str] = []

  def example(self, e:str):
    self.examples.append(e)


# class Moves:
#   moves:list[Move] = []

#   def add(self, fn:Callable[[Move],None]):
#     move = Move()
#     fn(move)
#     self.moves.append(move)

moves:list[Move] = []

conflict:Move = Move()
conflict.name = "Surface a conflict, ancient or modern"
conflict.rules = "Cities are rife with conflicts, filled with commu- nities that clash over resources and strong-willed individuals who make bids for power against en- trenched opposition. No Circle in the city has avoided the curse of internal politics, and every political actor is enmeshed in a dozen fights of var- ious sizes. Look for opportunities to present these conflicts to the player characters, especially when they go looking for useful resources or solutions to their problems. Alternate between old and new, se- rious and trivial, deadly and merely annoying. Di- versity in everything."
conflict.example("You cast the bones on the floor of your store, gently chant- ing Watanabe’s name. The visions rush through your mind, almost too fast to comprehend. He’s an old vam- pire. Only one thing is certain: he’s the one that closed the gates to Arcadia a hundred years ago. What do you do?")
conflict.example("Outside the club, Abby leans in close to you. Her blood is racing, you can hear it pounding in her veins. “Rico wants Elora dead. She’s become a problem for our pack. Maybe we can come to a deal?” What do you do?")
moves.append(conflict)

danger:Move = Move()
danger.name = "Put someone in danger"
danger.rules = "Above all others, this is your go-to move for raising the tension in a scene; if there is a lull in the action, putting someone in danger is almost never the wrong move. You can put the player characters in danger directly or threaten NPCs they care about onscreen and offscreen. The city is a dangerous place; bring that danger to bear directly and give the player characters a chance to react accordingly"
danger.example("You land softly in the alley, close enough to the feeding vampire to smell the victim’s blood. You ready a stake when you hear laughter behind you. Four more vamps, all armed, wearing the same gang colors as the one you were hunting. Looks like this was a trap. What do you do?")
danger.example("When you call home to check on the babysitter, fucking Sabrina answers the phone. “Everyone’s fine here, dar- ling. Just don’t do anything stupid, and everyone will be fine.” What do you do?")
moves.append(danger)

harm:Move = Move()
harm.name = "Inflict (or trade) harm"
harm.rules = "Harm is a versatile tool for raising the stakes. You can inflict it against people close to the player characters—allies, loved ones, enemies—or di- rectly against the player characters themselves. The amount of harm is completely up to you, but the weapons and situation should provide guid- ance. Remember that a straightforward fight usu- ally involves trading harm; both combatants take a blow—the amount of harm determined by the fiction—even if only one side of the fight remains standing by the end. See NPC Harm and Healing on page XX for more on how NPCs deal with harm."
harm.example("You hear the crack of a sniper rifle from a nearby apart- ment complex. You turn to look for the source when Ko- zlov’s head snaps back and he crumples to the ground. Shit. You can tell right away that he’s not breathing. What do you do?")
harm.example("As it leaps at you, you level the shotgun at the first de- mon, inflicting 3-harm. The blast rips through its chest knocking it to the ground. A second demon grabs your shoulder and lifts you off your feet, throwing you into the wall across the room with superhuman strength. Mark 2-harm. The demon starts to march toward you, unde- terred by your shotgun, grinning as her claws glint in the low light. What do you do?")
moves.append(harm)

opportunity:Move = Move()
opportunity.name = "Propose an opportunity with a cost"
opportunity.rules = "If the players seem stuck or frustrated by a prob- lem, leap in with NPCs that promise to solve the problem...at a cost. Be honest and direct with your offers: don’t wait for the players to exhaust them- selves when you’ve got a city full of people ready and willing to make a deal to get something done. Same goes for narrative opportunities—tell the players what concrete advantage they can seize and how much it costs to seize it. The players may not realize all the options in front of them, especially when the costs seem fuzzy; tell them what they can get away with and make the offer tempting"
opportunity.example("The dark wizard grins, his smile a sharp cluster of knives: “Bring me Riker’s heart—I’ll need it for the ritual—and I’ll cast the resurrection spell. No one should have to bury a child.” What do you do?")
opportunity.example("You can’t all get away now that you’ve been caught... but you could leave Lianne to fight that elemental alone. She’s already engaged with it, so all you have to do is slip out the back and leave her to hold it off. What do you say?")
moves.append(opportunity)

deal:Move = Move()
deal.name = "Reveal a deal done in their absence"
deal.rules = "The city moves all around the player characters, striking deals and solving problems. Think about what your NPCs do offscreen sometimes—espe- cially the higher status characters—and look for opportunities to relay to the player characters that they face active and determined opposition; you can look to your prep during the faction turn (page XX) if you aren’t sure what kinds of things might be going on in the city. Make these reveals loud and obvious; it’s a great moment when an ally reveals a betrayal (or weakness) or a villain mono- logues about their plans (or victories). Remember that if your players don’t know that a deal has been struck, it’s like the deal was never struck at all."
deal.example("“I’d love to help you, my friend. I really would. It’s just that Rico came by earlier. He made it clear that you’re on your own in his territory. Best of luck. Nothing per- sonal, you know.”")
deal.example("The Queen of Winter laughs. “You want me to side with you? I’ve been the one trying to kill you, love. And once I finish the job for Watanabe, I’ll finally be able to stop worrying about what I owe him.” What do you do?")
moves.append(deal)

turn:Move = Move()
turn.name = "Turn a move back on them"
turn.rules = "Sometimes the best move is to let the players have everything they want and more. Much more. A miss isn’t a failure, right? It’s your chance to make a move, to remind the players that their choices have real impact. Give them an unexpected consequence that results from their move, and make it clear to them how their actions drive the fiction. You don’t always have to undermine the original move—the intended violence, the hopeful escape—to turn the move back on the player character; the city is filled to the brim with sudden twists and reversals of fortune."
turn.example("You tap your inner wolf, looking for enough strength to shrug off these chains and get out of here. But your wolf isn’t satisfied with a taste of freedom; it wants the whole meal. Your body shifts and warps, changing completely into your wolf form. Those that imprisoned you must pay. Mark corruption. Are you ready to hurt them?")
turn.example("The demons nod when you lie to them about Wong; she’s not to blame, but better to put them on her trail than yours. The demon in charge—Vasquez, you think—smiles and gestures at the demons near the van. “It’s good to know that someone is to blame for all this chaos.” The van door opens, revealing Wong, already captured by these demon fuckups. What do you do?")
moves.append(turn)

debt:Move = Move()
debt.name = "Offer or claim a Debt owed"
debt.rules = "Debt is the central economy of the game. Claim Debts whenever a character does a favor for anoth- er and offer Debts when you need the player char- acters to get moving. Remember that both parties need to agree that a Debt is owed, though, so you need your player’s buy-in to claim a Debt from them. Make it obvious why they owe—someone stepped in and helped them out without proper recompense, or the player characters stepped into someone’s business that wasn’t their own."
debt.example("“Your meddling in my affairs cost me greatly, and I ex- pect you knew that when you got involved.” Watanabe seems almost bemused by your arrogance, but his tone is stern; you owe him a Debt. What do you say in response?")
debt.example("The faerie who saved you from the burning wreckage carries you to her car. She says, “Don’t move. You’ve got burns all over your body. Stay still.” You’re groggy, but you’ll fucking live. You definitely owe her a Debt. What do you do?")
moves.append(debt)

mobilize:Move = Move()
mobilize.name = "Mobilize resources to shift the odds"
mobilize.rules = "The city isn't static; the odds constantly shift as pow- erful forces move resources around to deal with problems and secure their holdings. When things get too easy or too dire, look for an opportunity to shift the odds and keep things interesting. Allies may send support, enemies may acquire new resourc- es, or the situation within a scene might change as NPCs activate supernatural powers. The city should never feel like one side’s victory is inevitable; the movers and shakers of the city always adjust their bets, shifting resources from one column to another to make sure no one ever comes out truly ahead."
mobilize.example("Your shotgun blast catches the werewolf squarely in the chest; he rears his head back and howls, his cry of pain echoed back at him as his pack closes the distance to your position. You know you don’t have much time before the rest of the pack is here. What do you do?")
mobilize.example("As'ad isn't deterred by the forces you've brought to bear against him. “Is this all you have?” He starts to chant, his skin growing harder and more resilient as magic reinforc- es his fragile human form. What do you do?")
moves.append(mobilize)

paint:Move = Move()
paint.name = "Paint the city in magical tones"
paint.rules = "The Circles aren’t shy or nervous about their influ- ence; their spaces and interests often spill out into the open, just out of reach of mortal eyes...but ev- erywhere you look if you know the truth. Blend the mundane and magical together: hints in the shad- ows sometimes—vampires slinking through the crowd at a rave—and brazen intrusions others—a faerie bar open to anyone who can get past the troll bouncer. Remind your players that the supernatu- ral is always present by marking the city with the obvious presence of every Circle, overlapping and crashing into each other until it’s clear that the city belongs to everyone all at once."
paint.example("Everyone at the conference appears to have one of Riker’s cards, his sigil burning with magical energy that’s obvious to anyone with the sight to see it. You haven’t seen him, but...he must be around here somewhere. What do you do?")
paint.example("You stumble out of the alley—leaving your pursuers far behind you—into a part of the city you’ve never seen be- fore; a ghost market. You see enslaved wraiths on display, chained to anchors held by other spirits, ghostly currency changing hands back and forth. What do you do?")
moves.append(paint)

claim:Move = Move()
claim.name = "Lock down, exploit, or claim a place of power"
claim.rules = "Use this move to change the status quo of a place that matters to the player characters, perhaps be- cause they care about it directly or because they want to seize or exploit it themselves. Locking down a place of power makes entry to it more dif- ficult: added security, locked and reinforced entry points, political pressure to stay out, etc; exploit- ing a place of power means treating it like a mere resource, revealing a weakness in it, or striking at someone inside who might have thought they were safe; claiming a place of power means someone or something takes possession of the place somehow, claiming it as their own."
claim.example("The city planning office said this building was aban- doned, but the wizards who are squatting here don’t seem to have gotten the memo. They’re tapping a ley line. Hard. You can feel it from a block away. What do you do?")
claim.example("The faeries don’t take kindly to your threats. The Queen of Summer rises: “Enough. You shame yourself with this clumsy intimidation. I have told you what is mine—your sanctum—and I see no reason to change course. Vacate it or face my wrath, little wizard.” What do you do?")
moves.append(claim)

consequences:Move = Move()
consequences.name = "Tell the consequences and ask"
consequences.rules = "Whenever the player characters try to get some- thing, make it clear what it’s going to cost them. Sometimes that cost is direct, like taking gunfire (and harm) when you wade into a battle or marking corruption to complete a terrible act, but often it’s about risk and uncertainty: tell them what it might cost them and then let them make moves to see what comes of their choices. If you tell them the cost of something outright, though, let it stand; don’t dou- ble back to make things easier on them later or re- quire them to roll dice when there’s no uncertainty."
consequences.example("You can tell that the werewolves aren’t interested in storm- ing your position. Too much chaos. They all want to live. If you make a run for your truck, though, you’re exposed and vulnerable...and they still have teeth. What do you do?")
consequences.example("When you get everything together for the banishment rit- ual, you realize that this is the kind of ritual that requires dark magics your mentor warned you not to touch. You’ll have to mark corruption if you complete it. You still want to go forward with it?")
moves.append(consequences)

downside:Move = Move()
downside.name = "Activiate their stuff's downside"
downside.rules = "The fictional positioning around each character gives you an infinite number of opportunities to turn their own bodies, powers, relationships, and resources against the player characters. Whether it’s the limitation on a weapon—guns need to re- load, swords get stuck in stuff—the cost of super- natural power—corruption, unintended effects—or the inevitable selfishness of their allies and friends, turning something the players see as useful into a problem or complication drives home how vulner- able the characters are to the city’s dangers. Don’t forget to be a fan of the player characters when you use this move; play toward the player’s conception of their own character, and they’ll be thrilled to see their weaknesses appear during a session."
downside.example("Your knees can’t take this shit, old man. There’s a reason you got out of the game, a reason you leave ghost hunting to the young now. But just as you realize how little juice you’ve got left, the wraith is on you, sinking cold, spectral fingers into your chest. What do you do?")
downside.example("You try to shoot the demon with your rifle, but she’s too quick for you. She gets in close, teeth bared, and goes for your throat. At this range, the gun is useless. “I know how you fight, hunter. We’ve been watching you for weeks.” What do you do?")
moves.append(downside)

# print(list(map(lambda m: m.name, moves)))

# Hmm, I could upload screenshots instead. That might be better!
