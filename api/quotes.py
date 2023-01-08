import re
from typing import Dict

quotes = """
1. “I'm sick of following my dreams, man. I'm just going to ask where they're going and hook up with ’em later."
—Mitch Hedberg

2. “Gentlemen, you can't fight in here. This is the war room.”
—President Merkin Muffley (Peter Sellers), Dr. Strangelove

3. “My mother always used to say: The older you get, the better you get, unless you’re a banana.”
—Rose (Betty White), The Golden Girls

4. “Halloween is the beginning of the holiday shopping season. That’s for women. The beginning of the holiday shopping season for men is Christmas Eve.”
—David Letterman

5. “Before you criticize someone, you should walk a mile in their shoes. That way when you criticize them, you are a mile away from them and you have their shoes.”
—Jack Handey

6. Bob: “Looks like you've been missing a lot of work lately.”
Peter: “I wouldn't say I've been missing it, Bob.”
—Bob (Paul Wilson) and Peter (Ron Livingston), Office Space

7. “Clothes make the man. Naked people have little or no influence in society.”
—Mark Twain

8. “Before you marry a person, you should first make them use a computer with slow Internet to see who they really are.”
—Will Ferrell

9. “I love being married. It's so great to find that one special person you want to annoy for the rest of your life.”
—Rita Rudner

Related: New Comedy Movies Release Schedule

10. “Ned, I would love to stand here and talk with you—but I’m not going to.”
—Phil Connors (Bill Murray), Groundhog Day

11. “When your mother asks, ‘Do you want a piece of advice?’ it is a mere formality. It doesn’t matter if you answer yes or no. You’re going to get it anyway.”
—Erma Bombeck

12. “I want my children to have all the things I couldn't afford. Then I want to move in with them.”
—Phyllis Diller

13. “Never follow anyone else’s path. Unless you’re in the woods and you’re lost and you see a path. Then by all means follow that path.”
—Ellen DeGeneres

14. “Insomnia sharpens your math skills because you spend all night calculating how much sleep you’ll get if you’re able to ‘fall asleep right now.’”
—Anonymous

15. “Breaking up is like knocking over a Coke machine. You can’t do it in one push; you got to rock it back and forth a few times, and then it goes over.”
—Jerry (Jerry Seinfeld), Seinfeld

16. “I’m not superstitious, but I am a little stitious.”
—Michael Scott (Steve Carrell), The Office

17. “I walk around like everything’s fine, but deep down, inside my shoe, my sock is sliding off.”
—Anonymous

18. “I haven't spoken to my wife in years. I didn't want to interrupt her.”
—Rodney Dangerfield

19. “I used to sell furniture for a living. The trouble was, it was my own.”
—Les Dawson

20. “There’s nothing wrong with you that an expensive operation can’t prolong.”
—Surgeon (Graham Chapman), Monty Python’s Flying Circus

21. “Someone asked me, if I were stranded on a desert island what book would I bring: ‘How to Build a Boat.’”
—Steven Wright

22. Ted Striker: “Surely you can’t be serious.”
Dr. Rumack: “I am serious. And don’t call me Shirley”
—Ted Striker (Robert Hays) and Dr. Rumack (Leslie Nielsen), Airplane!

23.“There is no sunrise so beautiful that it is worth waking me up to see it.”
―Mindy Kaling,Is Everyone Hanging Out Without Me?

24. “You know you’ve reached middle age when you’re cautioned to slow down by your doctor, instead of by the police.”
—Joan Rivers

25. “Truth hurts. Maybe not as much as jumping on a bicycle with a seat missing, but it hurts.”
—Lt. Frank Drebin (Leslie Nielsen), Naked Gun 2½: The Smell of Fear

26. “My Mama says that alligators are ornery because they got all them teeth and no toothbrush.”
—Bobby Boucher (Adam Sandler), The Waterboy

27. “I never feel more alone than when I’m trying to put sunscreen on my back.”
—Jimmy Kimmel

28. “Marriage is like an unfunny, tense version of Everybody Loves Raymond, but it doesn’t last 22 minutes. It lasts forever.”
—Pete (Paul Rudd), Knocked Up

29. “Being a mom means never buying the right amount of produce. Either everyone suddenly loves grapes and a week’s worth are eaten in one afternoon, or fruit flies are congregating around my rotting bananas.”
—Lessons from the Minivan

30. “I’m not insane. My mother had me tested.”
—Sheldon Cooper (Jim Parsons), The Big Bang Theory

31. “There are only three ages for women in Hollywood: babe, district attorney and Driving Miss Daisy.”
—Elise (Goldie Hawn), The First Wives Club

32. Usher: “Bride or groom?”
Wedding guest: “It should be perfectly obvious I’m neither!”
—Four Weddings and a Funeral

33. Stan Fields: “Describe your perfect date.”
Cheryl: “That’s a tough one. I’d have to say April 25. Because it’s not too hot and not too cold. All you need is a light jacket.”
—Stan Fields (William Shatner) and Cheryl Frasier (Heather Burns), Miss Congeniality

34. “I saw a study that said speaking in front of a crowd is considered the number one fear of the average person. Number two was death. This means to the average person, if you have to be at a funeral, you would rather be in the casket than doing the eulogy.”
—Jerry Seinfeld

35. Lucy: “There's just two things keeping me from dancing in that show.”
Fred: “Your feet?”
—Lucy (Lucille Ball) and Fred Mertz (William Frawley),I Love Lucy

36. “Common sense is like deodorant. The people who need it most never use it.”
—Anonymous

37. Coach: “How’s a beer sound, Norm?”
Norm: “I don't know, I usually finish before they get a word in.”
—Coach (Nicholas Colasanto) and Norm (George Wendt), Cheers

38. “If I woke up tomorrow with my head sewn to the carpet, I wouldn’t be more surprised.” —Clark Griswold (Chevy Chase), National Lampoon’s Christmas Vacation

39.“There’s nothing simpler than avoiding people you don’t like. Avoiding one’s friends, that’s the real test.”
—Dowager Countess Violet Crawley (Maggie Smith), Downton Abbey

40. “If I’m not back in five minutes, just wait longer.”
—Ace Ventura (Jim Carrey), Ace Ventura: Pet Detective

41. “The only thing that separates us from the animals is our ability to accessorize.”
—Clairee Belcher (Olivia Dukakis), Steel Magnolias

42. “I’m at a place in my life when errands are starting to count as going out.”
—Anonymous

43. “A good rule to remember for life is that when it comes to plastic surgery and sushi, never be attracted by a bargain.”
—Graham Norton

44. “I’m not good at the advice. Can I interest you in a sarcastic comment?”
—Chandler (Matthew Perry), Friends

45. “Here’s all you have to know about men and women: Women are crazy, men are stupid. And the main reason women are crazy is that men are stupid.”
—George Carlin

46. “When I'm in social situations, I always hold onto my glass. It makes me feel comfortable and secure and I don't have to shake hands.”
—Larry (Larry David), Curb Your Enthusiasm

47. “As you get older, three things happen. The first is your memory goes, and I can’t remember the other two.”
—Sir Norman Wisdom

48. “That’s why New York is so great, though. Everyone you care about can despise you and you can still find a bagel so good, nothing else matters. Who needs love when you’ve got lox? They both stink, but only one tastes good.”
—Midge Maisel (Rachel Brosnahan), The Marvelous Mrs. Maisel

49. “Here’s some advice: At a job interview, tell them you’re willing to give 110 percent. Unless the job is a statistician.”
—Adam Gropman

50. “Does it disturb anyone else that ‘The Los Angeles Angels’ baseball team translates directly to ‘The The Angels Angels’?”
—Neil DeGrasse Tyson

51. “I never forget a face—but in your case, I’ll be glad to make an exception.”
—Groucho Marx

52. “Here’s something to think about: How come you never see a headline like ‘Psychic Wins Lottery’?”
—Jay Leno

53. “A day without sunshine is like, you know, night.”
—Steve Martin

54. “My therapist told me the way to achieve true inner peace is to finish what I start. So far I’ve finished two bags of M&Ms and a chocolate cake. I feel better already.”
—Dave Barry

55. “Never do anything out of hunger. Not even eating.”
—Frank Semyon (Vince Vaughn), True Detective

56. “What do you mean, he don't eat no meat? That's okay, that's okay. I make lamb.”
—Aunt Voula (Andrea Martin), My Big Fat Greek Wedding

57. “You know you’re getting old when you stoop to tie your shoelaces and wonder what else you could do while you’re down there.”
—George Burns

58. “To call you stupid would be an insult to stupid people!”
—Wanda (Jamie Lee Curtis), A Fish Called Wanda

59. “Instead of the mahi mahi, may I just get the one mahi because I’m not that hungry?”
—Shelley Darlingson (Anna Faris), The House Bunny

60. “Accept who you are. Unless you’re a serial killer.”
—Ellen DeGeneres

61. Francois: “Do you know what kind of a bomb it was?”
Clouseau: “The exploding kind.”
—Francois (André Maranne) and Inspector Clouseau (Peter Sellers), The Pink Panther Strikes Again

62. “My ability to turn good news into anxiety is rivaled only by my ability to turn anxiety into chin acne.”
—Tina Fey, Bossypants

63. “There is one word that describes people that don't like me: Irrelevant.”
—Anonymous

64. “Why do they call it rush hour when nothing moves?”
—Robin Williams

65. “I remember it like it was yesterday. Of course, I don’t really remember yesterday all that well.”
—Dory (Ellen DeGeneres), Finding Dory

66. “I don’t have to take this abuse from you; I’ve got hundreds of people dying to abuse me.”
—Dr. Peter Venkman (Bill Murray), Ghostbusters

67. Police officer: “Pull over.”
Harry: “No, it’s a cardigan. But thanks for noticing.”
—Harry Dunne (Jeff Daniels), Dumb and Dumber

68. “I grew up with six brothers. That's how I learned to dance: waiting for the bathroom.”
—Bob Hope

69. “If we’re going to pay this much for crab, it better sing and dance and introduce us to the Little Mermaid.”
—Claire Foster (Tina Fey), Date Night

70. “I prefer not to think before speaking. I like being as surprised as everyone else by what comes out of my mouth.”
—Anonymous

71. “Never put off till tomorrow what you can do the day after tomorrow just as well.”
—Mark Twain

72. “Woke up today. It was terrible.”
—Grumpy Cat

73. “Eggs are fantastic for a fitness diet. If you don’t like the taste, just add cocoa, flour, sugar, butter, baking powder and cook at 350 for 30 minutes.”
—Anonymous

74. “I can’t end my messages with Love, Shaq because the B-52s ruined that for me.”
—Meme attributed to Shaquille O’Neal

75. “My husband and I fell in love at first sight. Maybe I should have taken a second look.”
—Halley Reed (Mia Farrow), Crimes and Misdemeanors

76. “Thanksgiving dinners take 18 hours to prepare. They are consumed in 12 minutes. Half-times take 12 minutes. This is not a coincidence.”
—Erma Bombeck

77. “Insanity runs in my family. It practically gallops.”
—Mortimer Brewster (Cary Grant), Arsenic and Old Lace

78. Brian: “Look, you've got it all wrong. You don't need to follow me. You don't need to follow anybody. You've got to think for yourselves. You're all individuals.”
Crowd: “Yes, we’re all individuals!”
Individual: “I’m not!”
—Brian (Graham Chapman) and cast, Monty Python’s Life of Brian

79. “Why can't you just be happy for me and then go home and talk behind my back later like a normal person?”
—Lillian (Maya Rudolph), Bridesmaids

80. “Anyone who lives within their means suffers from a lack of imagination.”
—Oscar Wilde

81. “What they could do to make it easier is combine the two, real estate and obituaries: Mr. Klein died today leaving a wife, two children, and a spacious three-bedroom apartment with a wood-burning fireplace.”
—Harry (Billy Crystal), When Harry Met Sally

82. “The key to faking out the parents is the clammy hands. It's a good non-specific symptom; I'm a big believer in it. A lot of people will tell you that a good phony fever is a dead lock, but you get a nervous mother, you could wind up in a doctor's office. That's worse than school. You fake a stomach cramp, and when you're bent over, moaning and wailing, you lick your palms. It's a little childish and stupid, but then, so is high school.”
—Ferris Bueller (Matthew Broderick), Ferris Bueller's Day Off

83. “I like my money where I can see it: hanging in my closet.”
—Carrie (Sarah Jessica Parker), Sex and the City

84: Cal: “You are really pushing my buttons today.”
Becky: “Which one is 'mute'?”
—Waitress, the Musical

85. “The worst part of online shopping is having to get up and get your credit card from your purse.”
—Anonymous

86. “People say, ‘But Betty, Facebook is a great way to connect with old friends.’ Well, at my age, if I want to connect with old friends I need a Ouija board.”
—Betty White

87. “My therapist says I'm afraid of success. I guess I could understand that, because after all, fulfilling my potential would really cut into my sitting-around time.”
—Maria Bamford

88. “From the ages of eight to 18, me and my family moved around a lot. Mostly we would just stretch, but occasionally one of us would actually get up to go to the fridge.”
—Jarod Kintz

89. “Money cannot buy health, but I'd settle for a diamond-studded wheelchair.”
—Dorothy Parker

90. “The whole purpose of places like Starbucks is for people with no decision-making ability whatsoever to make six decisions just to buy one cup of coffee. Short, tall, light, dark, caf, decaf, low-fat, non-fat. So people who don’t know what they’re doing, or who on earth they are can, for only $2.95, get not just a cup of coffee but an absolutely defining sense of self.”
—Joe Fox (Tom Hanks), You’ve Got Mail

91. “Good parenting means investing in your child's future, which is why I am saving to buy mine a hoverboard someday.”
—Lin-Manuel Miranda

92. “I love airports because the rules of society don’t apply. Eat a pizza and have a glass of wine at 7 am while in track pants. Nobody cares.”
—Anonymous

93. “Outside of a dog, a book is man’s best friend. Inside of a dog, it’s too dark to read.”
—Groucho Marx

94. “I’m one stomach flu away from my goal weight.”
—Emily Charlton (Emily Blunt), The Devil Wears Prada

95. “My perfect beautiful miracle baby? Never slept. Ever. Never. Twelve years later the memories of those nights, of that sleep deprivation, still make me rock back and forth a little bit. You want to torture someone? Hand them an adorable baby they love who doesn’t sleep.”
—Shonda Rimes

96. “I’d like to have a kid, but I’m not sure I’m ready to spend 10 years of my life constantly asking someone where his shoes are.”
—Damien Fahey

97. “Why yes, I can carry on a conversation made up entirely of movie quotes.”
—Anonymous

98. “I’m sure wherever my Dad is, he’s looking down on us. He’s not dead, just very condescending.”
—Jack Whitehall

99. “I like long walks, especially when they are taken by people who annoy me.”
—Noel Coward

100. “Trying is the first step toward failure.”
—Homer Simpson, The Simpsons

101. “I have a lot of growing up to do. I realized that the other day inside my fort.”
—Zach Galifianakis

"""

quotes_dict = {}

def parse_quotes():
  quote_parser = re.compile(r"(?P<key>\d{1,3})\.\s.(?P<phrase>([A-Za-z\'\s,\.:‘\?’]|’)*).")
  # —(?P<speaker>[\w ]*)(\((?P<actor>[\w ]*)\))?(, (?P<piece>[\w .’]*))?
  author_parser = re.compile(r"—(?P<speaker>[\w ]*)(\((?P<actor>[\w ]*)\))?(, (?P<piece>[\w .’]*))?")
  
  key = None
  for line in quotes.split("\n"):
    # print(line)
    qp = quote_parser.match(line)
    ap = author_parser.match(line)
    if qp is not None:
      key = qp.group('key')
      phrase = qp.group('phrase')
      quotes_dict[int(key)] = {'id':int(key), 'quote': phrase}
    if ap is not None:
      quotes_dict[int(key)]['speaker'] = ap.group('speaker')
      quotes_dict[int(key)]['actor'] = ap.group('actor')
      quotes_dict[int(key)]['piece'] = ap.group('piece')
    
def get_quote(id:int) -> Dict:
  if not quotes_dict:
    parse_quotes()
  return quotes_dict.get(id, None)
