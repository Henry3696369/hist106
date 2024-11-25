from drafter import *
from dataclasses import dataclass
hide_debug_information()
set_website_title("The life")
set_website_framed(True)
@dataclass
class State:
    default_name: str
    name: str
    ending_str: str

@route
def index(state: State) -> Page:
    
    return Page(state, ["Hist106-015 Project",
                        "Prof. Dr. Gregory Hargreaves",
                        "Heng Luo",
                        "Story Game: The life",
                        Image("life.jpeg", 500, 500),
                        "<br>",
                        Button("Start the game", begin),
                        Button("Achievements", achieve)])
@route
def begin(state: State) -> Page:
    return Page(state, ["This is a story about a black boy from the toughest time...",
                        Image("blurred_moon.jpeg", 500, 500),
                        "<br>",
                        "Name your character: ",
                        TextBox("name", f"{state.default_name}"),
                        Button("Save", save_name),
                        Button("Back", index)])
                        
@route
def achieve(state: State) -> Page:
    ending1 = ''
    ending2 = ''
    ending3 = ''
    ending4 = ''
    ending5 = ''
    ending6 = ''
    ending7 = ''
    ending8 = ''
    ending9 = ''
    secret = ''
    secret2 = ''
    if "a" in state.ending_str:
        ending1 = "#1 Ending: Death for starving"
    if "b" in state.ending_str:
        ending2 = "#2 Ending: Death for love"
    if "c" in state.ending_str:
        ending3 = "#3 Ending: Death for gratitude"
    if "d" in state.ending_str:
        ending4 = "#4 Ending: Death for the fire"
    if "e" in state.ending_str:
        ending5 = "#5 Ending: Death for madness"
    if "f" in state.ending_str:
        ending6 = "#6 Ending: Beginning of the Panthers"
    if "g" in state.ending_str:
        ending7 = "#7 Ending: Thousands and thousands of me"
    if "h" in state.ending_str:
        ending8 = "#8 Ending: The Rust Belt"
    if "i" in state.ending_str:
        ending9 = "#9 Ending: Disappered"
        
    if ending1 and ending2 and ending3 and ending4 and ending5 and ending6 and ending7 and ending8 and ending9:
        secret = Button("#10 secret ending", secret_ending)
        secret2 = "Congratulations! You have unlocked the secret ending."
    
    return Page(state, [Button("back", index),
                        secret2,
                        "Unlocked Endings:",
                        ending1,
                        ending2,
                        ending3,
                        ending4,
                        ending5,
                        ending6,
                        ending7,
                        ending8,
                        ending9,
                        secret])


@route
def save_name(state: State, name: str) -> Page:
    if name == "999abab":
        state.ending_str = "abcdefghi"
        return index(state)
    state.name = name
    state.default_name = name
    return chapter1_1(state)
    
@route
def chapter1_1(state: State) -> Page:
    return Page(state, ["Chapter 1",
                        "1940, Montgomery, Alabama...",
                        f"You are {state.name}, a 17 years black boy",
                        "You are sitting under the tree, thinking about what path you should take in the future.",
                        "Suddenly, your mind drifts back to 10 years ago, when the Great Depression started.",
                        Image("sit_tree.jpeg", 500, 500),
                        "<br>",
                        Button("Next", chapter1_2)])

@route
def chapter1_2(state: State) -> Page:
    return Page(state, ["Your father, the backbone of your family, lost his low-paying job.",
                            "But life always finds a way, he managed to get a job cleaning sewers, which was dirty but brought in hope to your family.",
                            "Just when it seemed like your family might get through the hardship, the white residents turned on your father, accusing him of spreading a foul stench that they claimed was tarnishing the community.",
                            "In the shadow of racial hatred and growing power of Ku Klus Klan, your father was lynched in public.",
                            Image("lynch.webp", 500, 500),
                            "Your mother had alwasy been in poor health, and her husband's death became the final straw that broke her back.",
                            "You didn't remember how your mother fell asleep that night. All you knew was that by the next morning, she never woke up again.",
                            "Overnight, as the only child in your family, you lost everything.",
                            "You wandered the streets aimlessly until you ran into a white farm owner, John.",
                            Image("encounter.jpeg", 500, 500),
                            "<br>",
                            Button("Next", chapter1_3)])

@route
def chapter1_3(state: State) -> Page:
    return Page(state, ["Even though John owned his farm, his life was far from rich due to the impact of the Great Depression.",
                            "Having witnessed your father's hard work before, John knew that your father's death was truly ironic.",
                            "When John saw you, just 7 years old, a wave of sympathy washed over him, and he knew he couldn't just walk away --- he had to do something to help.",
                            Image("kind_owner.jpeg", 500, 500),
                            "What do you think?",
                            Button("I hate the white...", ending1),
                            Button("I have no way now.", chapter1_4)])

@route
def ending1(state: State) -> Page:
    state.ending_str += "a"
    return Page(state, ["#1 Ending: Death for starving",
                            "John did not force you. He let out a sigh and then walked away.",
                            "You kept walking forward, only knowing that you were terribly hungry.",
                            "Slowly, your vision began to blur...",
                            Image("starve.jpeg", 500, 500),
                        "<br>",
                            Button("previous page", chapter1_3),
                            Button("restart chapter1", chapter1_1),
                            Button("Beginning Page", index)
                            ])

@route
def chapter1_4(state: State) -> Page:
    return Page(state, ["You accepted John's kindness and started working on his farm.",
                        "At first, he was decent to you, but slowly you began to notice his attitude growing more and more unfriendly, as if you were nothing more than a slave.",
                        "Although the work he gave you had increased over the ten years, at least you did not starve to death.",
                        "Over the years, there had always been an in explicable fear in your heart, but you did not know the reason.",
                        "Time flashes back to the present.",
                        '"It is the time to make some change.", you stand up and talk to yourself.',
                        "And you walk to the downtown.",
                        Image("back.jpeg", 500, 500),
                        "<br>",
                        Button("Next", chapter1_5)])

@route
def chapter1_5(state: State) -> Page:
    return Page(state, ["You see a beautilful white girl in the downtown.",
                        "The white long dress barely conceals her graceful figure, and beneath the light yellow hat is a lovely face.",
                        Image("whitelady.jpeg", 500, 500),
                        "You are staring at her, lost in a daze...",
                        Button("You are falling love...", ending2),
                        Button("You lower your head.", chapter1_6)])

@route
def ending2(state: State) -> Page:
    state.ending_str += "b"
    return Page(state, ["#2 Ending: Death for love",
                        '"Officer!!!", she noticed your gaze and let out a scream.',
                        "Instantly, her lovely face turned vicious.",
                        "This black man wants to hurt me!",
                        '''You were startled and hurriedly explained, "No, I am not. I didn't..."''',
                        "Before you could finish explaining, a white police punched you and you lost consciousness.",
                        "When you woke up, you found yourself tightly bound.",
                        "You closed your eyes, knowing that your father's story was about to play out again...",
                        Image("lynch.webp", 500, 500),
                        "<br>",
                        Button("Previous page", chapter1_5),
                        Button("restart chapter1", chapter1_1),
                        Button("Beginning Page", index)])

@route
def chapter1_6(state: State) -> Page:
    return Page(state, ["You thought of the death of your father, knowing that in this era, even making eye contact with them might be considered as a crime.",
                        "You lower your head and continue walking forward.",
                        "You head to the ...",
                        Button("John's farm", ending3),
                        Button("The balck church", chapter1_7)])

@route
def ending3(state: State) -> Page:
    state.ending_str += "c"
    return Page(state, ["#3 Ending: Death for gratitude",
                        "You did not know where to go, but you decided to tell John that you were leaving.",
                        "After all, to some extent, he was the one who saved you.",
                        '''"You want to leave?", after hearing your plan, John became angry.''',
                        '"I saved your ass and now you want to leave?"',
                        '"I have taken care of you all the time, and now, when you are capable of doing the most work, you want to leave?"',
                        '''"Who is going to do the work for my farm? You selfish traitor.",
                        "Now you knew the source of the fear in your heart. You did not want to argue with him, and you turned back to walk away."''',
                        '"After all these years of feeding you, now you just walk away?", John shouted hysterically.',
                        "Then, you heard the sound of a gunshot, and after that, everthing went balck...",
                        Image("gun.jpeg", 500, 500),
                        "John told the police that you had stolen money from him, and then everything vanished as if it had never happened.",
                        "In that times, the death of the black was too common...",
                        Button("Previous page", chapter1_6),
                        Button("restart chapter1", chapter1_1),
                        Button("Beginning Page", index)])
@route
def chapter1_7(state: State) -> Page:
    return Page(state, ["You remember that you had once met a black minister around John's farm, Rick. He had told you to come to the church if you ever needed help.",
                        "You don't know if he was trustworthy, but you can't think of anyone else who can help you.",
                        Image("church.jpeg", 500, 500),
                        "To you suprise, the church is organinzing a trip to Detroit recently.",
                        "Many black people like you, have decided to head north and try their luck.",
                        "You decide to ...",
                        Button("Say goodbye to John first.", ending3_2),
                        Button("Discuss more details with Rick", chapter1_8)])

@route
def ending3_2(state):
    state.ending_str += "c"
    return Page(state, ["#3 Ending: Death for gratitude",
                        "Before leaving, you decided to tell John first.",
                        "After all, to some extent, he was the one who saved you.",
                        '''"You want to leave?", after hearing your plan, John became angry.''',
                        '"I saved your ass and now you want to leave?"',
                        '"I have taken care of you all the time, and now, when you are capable of doing the most work, you want to leave?"',
                        "Who is going to do the work for my farm? You selfish traitor.",
                        "Now you knew the source of the fear in your heart. You did not want to argue with him, and you turned back to walk away.",
                        '"After all these years of feeding you, now you just walk away?", John shouted hysterically.',
                        "Then, you heaed the sound of a gunshot, and after that, everthing went balck...",
                        Image("gun.jpeg", 500, 500),
                        "John told the police that you had stolen money from him, and then everything vanished as if it had never happened.",
                        "In that times, the death of the black was too common...",
                        Button("Previous page", chapter1_7),
                        Button("restart chapter1", chapter1_1),
                        Button("Beginning Page", index)])

@route
def chapter1_8(state):
    return Page(state, ["Rick says that you are arriving just in time. They are leaving tonight.",
                        "You tell Rick that you want to say goodbye to John. But Rick's face grows serious and tells you not to go.",
                        "You don't ask why, and you have realized the fear inside is gradually fading away.",
                        "You decide to trust the man in front of you.",
                        Image("rick.jpeg", 500, 500),
                        "And this night, you are getting on the bus to Detroit.",
                        "(Chapter 1 is over)",
                        Button("Next", chapter2_1)])

@route
def chapter2_1(state):
    return Page(state, ["Chapter 2",
                        "On the bus, you overhearded others saying that the North is more friendly to balck people.",
                        "You can't help but feel a sense of relief, knowing that you have made the right choice.",
                        "But after you arrived in Detroit, you just realized things wan't as good as you have hoped.",
                        "It is better than south, but not too much.",
                        "The attitude of the white to black is still poor, but here, at least, the lynchins are less frequent.",
                        '"That is enough." You comfort yourself.',
                        "The church would not just send you to Detroit and leave you alone.",
                        "Under the arrangement of the local black church, you found a job at an automobile factory.",
                        Image("factory.jpeg", 500, 500),
                        "<br>",
                        Button("next", chapter2_2)])
@route
def chapter2_2(state):
    return Page(state, ["The North does not have Jim Crow laws, but the segregation to the black still exists.",
                        "You are assigned to a segregated workshop, and your colleagues were all Black.",
                        "Compared to the white workers, you earn the lowest wage, doing the hardest and dirtiest jobs.",
                        "You are exhausted by the heavy work, but you have already gotten used to is.",
                        "However, you don't know whether you should get used to it.",
                        Image("sweat.jpeg", 500, 500),
                        "<br>",
                        Button("next", chapter2_3)])

@route
def chapter2_3(state):
    return Page(state, ["On the morning of December 7, 1941, at 7:48 AM, Japan attacked Pearl Harbor.",
                        "The United States officially entered World War II on December 8 after the speech of the president, Franklin D. Roosevelt",
                        Image("pearl_harbor.jpeg", 500, 500),
                        "The United States begins drafting soldiers nationwide, including at your factory.",
                        "You decide to ...",
                        Button("Join the army", chapter2_4),
                        Button("Stay at the factory", ending4)])
@route
def ending4(state):
    state.ending_str += "d"
    return Page(state, ["#4 Ending: Death for the fire",
                        "You decided to stay at the factory.",
                        "Although you were exhausted after everyday work, but at least, the work was stable to you. You did not want to lose the small but stable source of income.",
                        "You told yourself that if your father had such a work like you, eveything would be different.",
                        "Thanks to the effort of the union, the working condition have improved, but only for the white workers.",
                        "For your segregated workshop, nothing had changed. In fact, things had only gotton worse and worse.",
                        "Due to the failure of safety facilities, you died in a fire at your workshop.",
                        Image("fire.jpeg", 500, 500),
                        Button("Previous page", chapter2_3),
                        Button("restart chapter2", chapter2_1),
                        Button("Beginning Page", index)])

@route
def chapter2_4(state):
    return Page(state, ["You noticed that the working conditions in your workshop is getting worse. And you have raised your concerns to your supervisor, who is a white, about the aging safety facilities, but he remained in different.",
                        "The fear inside returns, just like before. You can endure the physcal pain, but you can not the bear the torturing fear.",
                        "W.E.B. Du Bois' idea is popular within black community. He believe that African Americans should participate in World War II to win equality.",
                        "You agree that it is a fair idea, and now is the best time. You decide to join the military.",
                        "Fortunately, you successfully pass the draft test and join the army.!",
                        "It is not that surprising to you, as segregation exist in the army as well.",
                        Image("soldier1.jpeg", 500, 500),
                        "<br>",
                        "And you will be assined to the ...",
                        Button("European Theater", chapter2_5),
                        Button("Pacific Theater", ending5)])

@route
def ending5(state):
    state.ending_str += "e"
    return Page(state, ["#5 Ending: Death for madness",
                        "You were assigned to the Pacific Theater.",
                        "The U.S. military adopted the strategy of island hopping. Your job was to build airfields after capturing key islands, for future attack.",
                        "However, you could never imagine how mad the Japanese forces could be.",
                        "You died in a suicide attack by the Japanese military.",
                        Image("suicide.jpeg", 500, 500),
                        "<br>",
                        Button("Previous page", chapter2_4),
                        Button("restart chapter2", chapter2_1),
                        Button("Beginning Page", index)])

@route
def chapter2_5(state):
    return Page(state, ["Due to the segregation, you are still assigned to the worst and most exhausting logisitical tasks in the army.",
                        "But this actually keeps you away from the intense combat, which means you are not so easy to die.",
                        "Here, you meet Black soldier from France, and you finally realize that it is possilble for Black people to work with White people with dignity and equality.",
                        "The seed of equality begins to sprout in your heart. Though you still face unequal treatment, you know that you are not inferior to anyone.",
                        "Logistical work is not always safe. Due to sudden Nazi attacks, you got many bullet holes in your body.",
                        Image("nazi.jpeg", 500, 500),
                        "But luckily, you make it thorough.",
                        "After V-E day(Victory in Europe Day), May 7, 1945, a year after D day(Normandy Invasion), when the Germany officially surrendered, you returned to the United States, proudly as a Black man.",
                        Image("soldier2.jpeg", 500, 500),
                        "(Chaper 2 is over)",
                        Button("next", chapter3_1)])

@route
def chapter3_1(state):
    return Page(state, ["Chapter 3",
                        "You have decided to return to Montgomery, your home town.",
                        "Over the past four years, you’ve been through so much. You thought you black soldiers had successfully fought for equality for your people, but in reality, nothing had changed.",
                        "The condition for the black people is still poor in the south.",
                        "Your heart is burning with anger.",
                        Image("anger.jpeg", 500, 500),
                        "Wher do you want to go?",
                        Button("John's Farm", chapter3_2),
                        Button("The black church", ending6)])
@route
def chapter3_2(state):
    return Page(state, ["You decide to visit John, as leaving without saying goodbye back then has left feeling guilty until now.",
                        "Nothing had changed, yet everything is different. John's farm has turned into an abandoned field.",
                        '''You ask the neighbours about him, but they only answer indifferently with "I don't know", even as a medal hung proudly on your chest.''',
                        '''"Maybe Rick would know, if he is still there". You tell yourself.''',
                        "You turn around and head toward the church.",
                        Image("turnaround.jpeg", 500, 500),
                        Button("next", chapter3_3)])

@route
def chapter3_3(state):
    return Page(state, ['''"Long time no see", Rick smiles at you.''',
                        Image("rick.jpeg", 500, 500),
                        "Rick is just like he used to be, always smiling",
                        "You ask him about John, he shakes his head and says that he died in a Black Riot a year ago.",
                        '''"So ironic.", you think to yourself, "John adopted me, a black boy, and died in a black riot.''',
                        "Now you know the reason why the neighbours were so cold to you.",
                        "The anger inside you gradually settles down.",
                        "You tell him about your desire to fight for equality for Black people, and Rick's face becomes serious.",
                        '''"I can understand you.", Rick says, "But be patient, my son."'''
                        "You can understand Rick's implied message -- he does not want you to use the violent way to gain equality.",
                        '''"Could I work in the church, and try to get some wisdom from bible for my future fight of equality?", you sincerely plead.''',
                        '''"You are always welcom." Rick smiles again.''',
                        "You settle down in the church.",
                        Button("next", chapter3_4)])

@route
def ending6(state):
    state.ending_str += "f"
    return Page(state, ["#6 Ending: Beginning of the Panthers",
                        '''"Long time no see", Rick smiles at you.''',
                        Image("rick.jpeg", 500, 500),
                        "Rick is just like he used to be, always smiling",
                        "You tell him about your desire to fight for equality for Black people, and Rick's face becomes serious.",
                        '''"I can understand you.", Rick says, "But be patient, my son."''',
                        '''How can I be patient, after going through all of this.''',
                        '''"If we want equality, wo need to fight for it! Just like what we did on the battlefield."''',
                        '''"Don't do that, my son. Try to pray to God, there must be a better way." Rick tries to presuade you.''',
                        "You didn't want to argue with Rick, who is a weak old man in your eyes.",
                        "You turned back and left, ready to fight for equality in your own way.",
                        "<br>",
                        "6 months later, you organized a protest, using your relationship from army.",
                        "At first, you only hoped for the local goverment to end segregation, but with the armed suppression by the white forces, the protest turned into a riot.",
                        "You died in the riot.",
                        "In your organization, there was a man named Bobby Seale, who survived the riot. Twenty years later, he founded the Black Panthers Party to continue the work you had started.",
                        Image("panthers.jpeg", 500, 500),
                        Button("previous page", chapter3_1),
                        Button("restart chapter3", chapter3_1),
                        Button("BEGINNING PAGE", index)])
@route
def chapter3_4(state):
    return Page(state, ["1950, a well-educated young pastor named Martin arrived at the church.",
                        "Hearing that you had served in World War II, he came to visit you and asked you about the situation of Black people during the war.",
                        "You talked a lot with him, from the poor situation of black people to how to fight for equality.",
                        Image("talking.jpeg", 500, 500),
                        "In your conversation, you realized that Martin was highly knowledgeable, and he also recognized that you had various life experiences that he never had.",
                        "Your patience had finally paid off, and you knew that he was the person you had been waiting for.",
                        "You two instantly connected and decided to begin spreading the message of racial equality and nonviolent revolution in the black community.",
                        "Although you were 8 years older than him, you respected him like your teacher. Martin, however, never acted arrogantly and he treated you like his brother.",
                        "Gradually, more and more black people began to support you.",
                        "Then, in 1955, on December 1st, a Black woman was arrested on a bus for refusing to give up her seat to a white person on a bus...",
                        Button("next", chapter3_5)])

@route
def chapter3_5(state):
    return Page(state, ["The resentment among the local Black community reached its peak at this moment.",
                        "Martin was elected as the local civil rights leader, and under his leadership, the Montgomery Bus Boycott began.",
                        Image("protest.jpeg", 500, 500),
                        "Almost all the local black residents joined this protest, expressing their dissatisfaction by refusing to take the bus.",
                        "After 381 days of boycott, the Montgomery bus system was economically crippled, and the municipal government agreed to abolish segregation on the bus.",
                        "You succeeded.",
                        Button("next", chapter3_6)])

@route
def chapter3_6(state):
    return Page(state, ["This was the first time that you truly tasted the sweetness of success in fighting for Black rights.",
                        "And it only strengtnened your resolve to continue fighting.",
                        "In the days followed, you and Martin traveled to many places togeter.",
                        "You together established the Southern Christian Leadership Conference (SCLC) in Atlanta, then led another protest in Birmingham.",
                        "Following that, in 1963, you two arrived in Washington, where you led a march of 250,000 people, which made a profound mark on Martin’s place in history.",
                        Image("king.png", 500, 500),
                        '''“I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.”, Martin, also known as Martin Luther King Jr., was delivering a passionate speech in front of the crowd.''',
                        '''“Free at last! Free at last! Thank God Almighty, we are free at last!”''',
                        "As the speech came to an end, you joined the crowd in a surge of excitement, knowing that you had just made history.",
                        Button("Next", chapter3_7)])

@route
def chapter3_7(state):
    return Page(state, ["A year later, in 1964, the Civil Rights Act was passed, which ended segregation in public places.",
                        "But your fight was not over. Although there were legal constraints, discrimination against Black people was still widespread in society.",
                        "As Martin's right-hand man, you both organized many more marches and speeches together.",
                        "However, life is always full of unexpected turns. In 1968, Martin was assassinated while supporting a workers' strike in Memphis, Tennessee.",
                        Image("assassin.jpeg", 500, 500),
                        '''"How can we face violence when we advocates of nonviolence?" You ask yourself.''',
                        "What are you going to do?",
                        Button("Give up", chapter3_8),
                        Button("Continue Martin's legacy", ending7)])
@route
def ending7(state):
    state.ending_str += "g"
    return Page(state, ["#7 Ending: Thousands and thousands of me",
                        "You decided to carry on Marin's unfinished work, continuing to uphold the philosophy of nonviolence.",
                        "You gave speeches and organize marches, advocating not only for black rights but also raising your voice for other marginalized groups.",
                        "Soon, you became the new target of assassins and were killed on your way to your house.",
                        "Later, people found these words in your diary.",
                        Image("diary.jpeg", 500, 500),
                        '''"When I choose nonviolence, I have already accepted any violence that may befall me. Because I know, even if I fall, there are thousands and thousands of me who will rise again."''',
                        Button("previous page", chapter3_7),
                        Button("restart chapter3", chapter3_1),
                        Button("Beginning page", index)])

@route
def chapter3_8(state):
    return Page(state, ["You are tired, and the loss of your best friend has left you with no motivation to continue the civil rights movement.",
                        Image("tired.jpeg", 500, 500),
                        "You decide to...",
                        Button("Go back to Montgomery", chapter3_9),
                        Button("Leave the south", ending8)])

@route
def ending8(state):
    state.ending_str += "h"
    return Page(state, ["#8 Ending: The Rust Belt",
                        "You decided to leave the South, which was full of memories with Martin.",
                        "You returned to Detroit.",
                        "You found a job at the automobile factory through your connections.",
                        "Your workshop is still filled with Black workers, which did not surprise you.",
                        "Because you know that while segregation has been legally abolished, it still existed in people's minds.",
                        '''"Let it be," you comforted yourself.''',
                        "After working steadily for a few years, deindustrialization began. As a Black man, you were among the first employees to be laid off.",
                        "Perhaps you had already guessed this outcome, but you chose not to resist.",
                        "You, unemployed, spent your days drinking away the pain.",
                        Image("drinking.jpeg", 500, 500),
                        "A month later, your body was found by a neighbor, the smell leading them to your door.",
                        Button("previous page", chapter3_8),
                        Button("restart chapter3", chapter3_1),
                        Button("beginning page", index)])
@route
def chapter3_9(state):
    return Page(state, ["You decide to return to where it all began, the Black church in Montgomery.",
                        "Rick is glad to see you. He knows about your achievements over the years and asks if you would like to take on the church.",
                        Image("rick.jpeg", 500, 500),
                        '''"Sorry, I am tired, Rick", you refuse Rick, and ask if there is some cleaning work for you to do.''',
                        "Rick doesn’t say a lot. He assignes you the task of cleaning, as you requested, and arranges a place for you to live.",
                        "You start a simple life, daily activities of which are cleaning and worship.",
                        Image("cleaning.jpeg", 500, 500),
                        "<br>",
                        Button("next", ending9)])

@route
def ending9(state):
    state.ending_str += "i"
    return Page(state, ["#9 Ending: Disappered",
                        "After cleaning in the church for three years, you suddenly disappeared, and no one knew where you had gone.",
                        "(The story is over)",
                        Image("wenhao.jpeg", 300, 500),
                        "<br>",
                        Button("restart chapter3", chapter3_1),
                        Button("beginning page", index)])

@route
def secret_ending(state):
    return Page(state, ["#Secret Ending: The spirit",
                        "The death of a close friend and the confusion about what is right have been deeply troubling your heart.",
                        "And that is the reason why you just want to do cleaning in the church after all the things you have been through, believing it can help you find peace.",
                        "However, it does not work. The more you seek peace, the more restless your heart becomes, because deep down, your heart has always been longing for an answer.",
                        "One night, you had a dream",
                        "In that dream, you met god. You asked him what should you do, and how could you do.",
                        Image("god.jpeg", 500, 500),
                        '''"Find your spirit that I tell in the bible! It will have all the answers you." God spoke in an assertive tone.''',
                        '''"But where is the spirit? How can I find it?" You asked more questions.''',
                        '''"The spirit has always been with you, but you have been ignoring it all the time."''',
                        "You suddenly woke up, as if you have understood something.",
                        "That night, you left the church without telling anyone. You just disappeared.",
                        Image("leaving.jpeg", 500, 500),
                        "You had came to the church to seek answers and peace, and now you had both of them.",
                        "No one knows where you went, not even you, but none of it matters anymore.",
                        Button("previous page", achieve),
                        Button("beginning page", index)])
                        
                        
                        
                        
                        
                

        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
            

                        
                        
                        
                        
                        


                        
                        

                        
                        
                        
                        

                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        




                        
    
                        
                        
                        
    
                        
                        
                        
                        
                        
                        

                        
                        
                        

    
                        
                        
                            
                            
                            
                            
                            
                            
                            

start_server(State("James", "1James", ""))

