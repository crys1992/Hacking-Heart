import pyglet
import time
import sys
import random



# =========== Before beginning the game, please download the music files from https://www.dropbox.com/sh/ft0tlsred1qqihn/AAB3nwjA5jwGX-UYSfPkiP88a?dl=0
# =========== Next, please chance crystalwang in the file paths below with the name of your personal laptop directory 


loveStoryAudio = pyglet.media.load("/Users/crystalwang/Desktop/LoveStory.wav", streaming = False)
heartlessAudio = pyglet.media.load("/Users/crystalwang/Desktop/Heartless.wav", streaming = False)
dontGoBreakingMyHeartAudio = pyglet.media.load("/Users/crystalwang/Desktop/DontGoBreakingMyHeart.wav", streaming = False)
myHeartWillGoOnAudio = pyglet.media.load("/Users/crystalwang/Desktop/myHeartWillGoOn.wav", streaming = False)
dontPhunkWithMyHeartAudio = pyglet.media.load("/Users/crystalwang/Desktop/dontPhunkWithMyHeart.wav", streaming = False)
trueToYourHeartAudio = pyglet.media.load("/Users/crystalwang/Desktop/trueToYourHeart.wav", streaming = False)
shapeOfMyHeartAudio = pyglet.media.load("/Users/crystalwang/Desktop/shapeOfMyHeart.wav", streaming = False)
loveIsAnOpenDoorAudio = pyglet.media.load("/Users/crystalwang/Desktop/loveIsAnOpenDoor.wav", streaming = False)
endlessLoveAudio = pyglet.media.load("/Users/crystalwang/Desktop/endlessLove.wav", streaming = False)
player = pyglet.media.Player()


# ========= Printing the Title of the Game and Welcome Screen =============== #

def printGraphic(name):
    if (name == "title"):
      print '                   _    _                                     _    '   
      print '   /\  /\__ _  ___| | _(_)_ __   __ _    /\  /\___  __ _ _ __| |_  ' 
      print '  / /_/ / _` |/ __| |/ / | _  \ / _` |  / /_/ / _ \/ _` |  __| __| '
      print ' / __  / (_| | (__|   <| | | | | (_| | / __  /  __/ (_| | |  | |_  ' 
      print ' \/ /_/ \__,_|\___|_|\_\_|_| |_|\__, | \/ /_/ \___|\__,_|_|   \__| ' 
      print '                                |___/                              '  
      print '__________________________________________________________________ '
      print 'Welcome to Hacking Heart! Here you will learn how to make anybody "hack your heart" and fall in love with you in the way you deserve to be loved.'
      print '          '
      


# ========= Introduction ============= #

def intro():
  printGraphic("title")

  playGame = raw_input ("Are you interested in playing? (Y/N):")

  if (playGame == "Y"):
        print "Hooray! Let's hack some hearts;)"
        print "    "
  else:
      print "Too bad. You're playing anyway. Who doesn't want love? ;)"
      print "  "

   
# ========= Primary Quiz ================= #   
def quiz(): 
  giftGiving = 0 
  physicalTouch = 0 
  qualityTime = 0 
  wordsOfAffirmation = 0
  actsOfService = 0
  
  name = raw_input ("What is your name? > ")
  print "Hello " + name + " <3. Let's begin." 
  print "         "
  print "(Question 1 of 30) It's more meaningful to me when... "
  print "(a) I receive a loving note/text/email for no special reason from my loved one."
  print "(b) my partner and I hug"
  question1 = raw_input ("Please choose a or b > ")
  if (question1 == "a"): 
    actsOfService +=1
  elif (question1 == "b"):
    physicalTouch +=1
  print "         "
  print "(Question 2 of 30) It's more meaningful to me when..."
  print "(a) I can spend alone time with my partner - just the two of us."
  print "(b) My partner does something practical to help me out"
  question2 = raw_input ("Please choose a or b > ")
  if (question2 == "a"): 
    qualityTime +=1
  elif (question2 == "b"):
    actsOfService +=1
  print "         "
  print "(Question 3 of 30) It's more meaningful to me when ..."
  print "(a) my partner gives me a little gift as a token of our love for each other"
  print "(b) I get to spend uninterrupted leisure time with my partner"
  question3 = raw_input ("Please choose a or b > ")
  if (question3 == "a"): 
    giftGiving +=1
  elif (question3 == "b"):
    qualityTime +=1
  print "         "
  print "(Question 4 of 30) It's more meaningful to me when..."
  print "(a) My partner unexpectedly does something for me like filling my car or doing the laundry"
  print "(b) my partner and I touch"
  question4 = raw_input ("Please choose a or b > ")
  if (question4 == "a"): 
    actsOfService +=1
  elif (question4 == "b"):
    physicalTouch +=1
  print "         "
  print "(Question 5 of 30) It's more meaningful to me when..."
  print "(a) my partner puts his/her arm around me when we're in public"
  print "(b) my partner surprises me with a gift"
  question5 = raw_input ("Please choose a or b > ")
  if (question5 == "a"): 
    physicalTouch +=1
  elif (question5 == "b"):
    giftGiving +=1
  print "         "
  print "(Question 6 of 30) It's more meaningful to me when..."
  print "(a) I'm around my partner, even if we're not really doing anything."
  print "(b) I hold hands with my partner"
  question6 = raw_input ("Please choose a or b > ")
  if (question6 == "a"): 
    actsOfService +=1
  elif (question6 == "b"):
    physicalTouch +=1
  print "         "
  print "(Question 7 of 30) It's more meaningful to me when..."
  print "(a) my partner gives me a gift."
  print "(b) I hear 'I love you' from my partner."
  question7 = raw_input ("Please choose a or b > ")
  if (question7 == "a"): 
    giftGiving +=1
  elif (question7 == "b"):
    wordsOfAffirmation +=1
  print "         "
  print "(Question 8 of 30) It's more meaningful to me when..."
  print "(a) I sit close to my partner."
  print "(b) I am complimented by my partner for no apparent reason"
  question8 = raw_input ("Please choose a or b > ")
  if (question8 == "a"): 
    physicalTouch +=1
  elif (question8 == "b"):
    wordsOfAffirmation +=1
  print "         "
  print "(Question 9 of 30) It's more meaningful to me when..."
  print "(a) I get the chance to just 'hang out' with my partner."
  print "(b) I unexpectedly get small gifts from my partner. "
  question9 = raw_input ("Please choose a or b > ")
  if (question9 == "a"): 
    qualityTime +=1
  elif (question9 == "b"):
    giftGiving +=1
  print "         "
  print "(Question 10 of 30) It's more meaningful to me when..."
  print "(a) I hear my partner tell me 'I'm proud of you'."
  print "(b) my partner helps me with a task"
  question10 = raw_input ("Please choose a or b > ")
  if (question10 == "a"): 
    wordsOfAffirmation +=1
  elif (question10 == "b"):
    actsOfService +=1
  print "         "
  print "(Question 11 of 30) It's more meaningful to me when..."
  print "(a) I get to do things with my partner'."
  print "(b) I hear supportive words from my partner"
  question11 = raw_input ("Please choose a or b > ")
  if (question11 == "a"): 
    qualityTime +=1
  elif (question1 == "b"):
    wordsOfAffirmation +=1
  print "         "
  print "(Question 12 of 30) It's more meaningful to me when..."
  print "(a) My partner does things for me instead of just talking about doing nice things."
  print "(b) I feel connected to my partner through a hug."
  question12 = raw_input ("Please choose a or b > ")
  print "         "
  if (question12 == "a"): 
    actsOfService +=1
  elif (question12 == "b"):
    physicalTouch +=1
  print "(Question 13 of 30) It's more meaningful to me when..."
  print "(a) I hear praise from my partner."
  print "(b) My partner gives me something that shows he/she was really thinking about me."
  question13 = raw_input ("Please choose a or b > ")
  if (question13 == "a"): 
    wordsOfAffirmation +=1
  elif (question13 == "b"):
    giftGiving +=1
  print "         "
  print "(Question 14 of 30) It's more meaningful to me when..."
  print "(a) I am able to just be around my partner."
  print "(b) I get a backrub or a massage from my partner."
  question14 = raw_input ("Please choose a or b > ")
  if (question14 == "a"): 
    qualityTime +=1
  elif (question14 == "b"):
    giftGiving +=1
  print "         "
  print "(Question 15 of 30) It's more meaningful to me when..."
  print "(a) My partner reacts positively to something I've accomplished."
  print "(b) My partner does something for me that I know they don't particularly enjoy."
  question15 = raw_input ("Please choose a or b > ")
  if (question15 == "a"): 
    wordsOfAffirmation +=1
  elif (question15 == "b"):
    actsOfService +=1
  print "         "
  print "(Question 16 of 30) It's more meaningful to me when..."
  print "(a) My partner and I kiss frequently."
  print "(b) I sense my partner is showing interest in the things I care about."
  question16 = raw_input ("Please choose a or b > ")
  if (question16 == "a"): 
    physicalTouch +=1
  elif (question16 == "b"):
    qualityTime +=1
  print "         "
  print "(Question 17 of 30) It's more meaningful to me when..."
  print "(a) My partner works on special projects with me that I have to complete."
  print "(b) My partner gives me an exciting gift."
  question17 = raw_input ("Please choose a or b > ")
  if (question17 == "a"): 
    physicalTouch +=1
  elif (question17 == "b"):
    qualityTime +=1
  print "         "
  print "(Question 18 of 30) It's more meaningful to me when..."
  print "(a) I am complimented by my partner on my appearance."
  print "(b) My partner takes the time to listen to me and really understands my feelings."
  question18 = raw_input ("Please choose a or b > ")
  if (question18 == "a"): 
    wordsOfAffirmation +=1
  elif (question18 == "b"):
    qualityTime +=1
  print "         "
  print "(Question 19 of 30) It's more meaningful to me when..."
  print "(a) My partner and I are affectionate in public."
  print "(b) My partner offers to run errands for me."
  question19 = raw_input ("Please choose a or b > ")
  if (question19 == "a"): 
    physicalTouch +=1
  elif (question19 == "b"):
    actsOfService +=1
  print "         "
  print "(Question 20 of 30) It's more meaningful to me when..."
  print "(a) My partner does a bit more than his/her normal share of the responsibilites we share."
  print "(b) I get a gift that I know my partner put thought into choosing."
  question20 = raw_input ("Please choose a or b > ")
  if (question20 == "a"): 
    actsOfService +=1
  elif (question20 == "b"):
    giftGiving +=1
  print "         "
  print "(Question 21 of 30) It's more meaningful to me when..."
  print "(a) My partner doesn't check his/her phone while we're talking."
  print "(b) My partner goes out of the way to do something that relieves pressure on me."
  question21 = raw_input ("Please choose a or b > ")
  print "         "
  if (question21 == "a"): 
    qualityTime +=1
  elif (question21 == "b"):
    actsOfService +=1
  print "(Question 22 of 30) It's more meaningful to me when..."
  print "(a) I can look forward to a holiday because of a gift I anticipate receiving."
  print "(b) I hear the words 'I appreciate you' from my partner."
  question22 = raw_input ("Please choose a or b > ")
  if (question22 == "a"): 
    giftGiving +=1
  elif (question22 == "b"):
    wordsOfAffirmation +=1
  print "         "
  print "(Question 23 of 30) It's more meaningful to me when..."
  print "(a) My partner brings me a little gift after he/she has been traveling without me."
  print "(b) My partner takes care of something I'm responsible to do but I feel to stressed to do at the time. "
  question23 = raw_input ("Please choose a or b > ")
  if (question21 == "a"): 
    qualityTime +=1
  elif (question21 == "b"):
    actsOfService +=1
  print "         "
  print "(Question 24 of 30) It's more meaningful to me when..."
  print "(a) My partner doesn't interrupt me while I'm talking."
  print "(b) Gift giving is an important part of our relationship."
  question24 = raw_input ("Please choose a or b > ")
  if (question24 == "a"): 
    qualityTime +=1
  elif (question24 == "b"):
    giftGiving +=1
  print "         "
  print "(Question 25 of 30) It's more meaningful to me when..."
  print "(a) My partner helps me out when he/she knows I'm already tired."
  print "(b) I get to go somewhere while spending time with my partner."
  question25 = raw_input ("Please choose a or b > ")
  if (question25 == "a"): 
    actsOfService +=1
  elif (question25 == "b"):
    qualityTime +=1
  print "         "
  print "(Question 26 of 30) It's more meaningful to me when..."
  print "(a) My partner and I are physically intimate."
  print "(b) My partner gives me a little gift that he/she picked up in the course of their normal day."
  question26 = raw_input ("Please choose a or b > ")
  if (question26 == "a"): 
    physicalTouch +=1
  elif (question26 == "b"):
    giftGiving +=1
  print "         "
  print "(Question 27 of 30) It's more meaningful to me when..."
  print "(a) My partner says something encouraging to me."
  print "(b) I get to spend time in a shared activity or hobby with my partner."
  question27 = raw_input ("Please choose a or b > ")
  if (question27 == "a"): 
    wordsOfAffirmation +=1
  elif (question27 == "b"):
    qualityTime +=1
  print "         "
  print "(Question 28 of 30) It's more meaningful to me when..."
  print "(a) My partner surprises me with a small token of their appreciation."
  print "(b) My partner and I touch a lot during the normal course of the day."
  question28 = raw_input ("Please choose a or b > ")
  if (question21 == "a"): 
    giftGiving +=1
  elif (question21 == "b"):
    physicalTouch +=1
  print "         "
  print "(Question 29 of 30) It's more meaningful to me when..."
  print "(a) My partner helps me out, especially if I know they already are busy."
  print "(b) I hear my partner specifically tell me, 'I appreciate you'."
  question29 = raw_input ("Please choose a or b > ")
  if (question29 == "a"): 
    qualityTime +=1
  elif (question29 == "b"):
    wordsOfAffirmation +=1
  print "         "
  print "(Question 30 of 30) It's more meaningful to me when..."
  print "(a) My partner and I embrace after we've been apart for a while."
  print "(b) I hear my partner say how much I mean to him/her."
  question30 = raw_input ("Please choose a or b > ")
  if (question30 == "a"): 
    physicalTouch +=1
  elif (question30 == "b"):
    wordsOfAffirmation +=1
    
  print "                         "
  raw_input ("Thanks for answering a shitton of questions! We are calculating your top love languages now. Press enter to reveal your results! >")
  score = [qualityTime, wordsOfAffirmation, physicalTouch, giftGiving, actsOfService]
  topChoice = max(score)
  secondChoice = sorted(score, reverse=True)[1]
  


  if (topChoice == qualityTime):
      loveLanguageText1 = 'Quality Time'
      loveLanguageDescription1 = 'In the vernacular of Quality Time, nothing says, "I love you," like full, undivided attention. Being there for this type of person is critical, but really being there - with the TV off, fork and knife down, and chores and tasks on standby - makes your significant other feel truly special and loved. Distractions, postponed dates, or the failure to listen can be especially hurtful. Quality Time also means sharing quailty conversation and quality activities. ' 
  elif (topChoice == wordsOfAffirmation):
      loveLanguageText1 = 'Words of Affirmation'
      loveLanguageDescription1 = "Actions don't always speak louder than words. If this is your love language, unsolicited compliments mean the world to you. Hearing the words, 'I' love you,'' are important - hearing the reasons behind that love sends your spirits skyward. Insults can leave you shattered and are not easily forgotten. Kind, encouraging, and positive words are truly life-giving." 
  elif (topChoice == physicalTouch):
      loveLanguageText1 = 'Physical Touch'
      loveLanguageDescription1 = "This language isn't all about the bedroom. A person whose primary language is Physical Touch is, not surprisingly, very touchy. Hugs, pats on the back, holding hands, and thoughtful touches on the arm, shoulder, or face - they can all be ways to show excitement, concern, care, and love Physical presence and accessibility are crucial, while neglect or abuse can be unforgivable and destructive. Physical touch fosters a sense of security and belonging in any relationship."
  elif (topChoice == giftGiving):
      loveLanguageText1 = 'Gift Giving'
      loveLanguageDescription1 = "Don't mistake this love language for materialism; the receiver of gifts thrives on the love, thoughtfulness, and effort behind the gift. If you speak this language, the perfect gift or gesture shows that you are known, you are cared for, and you are prized above whatever was sacrificed to bring the gift to you. A missed birthday, anniversary, or a hasty, thoughtless gift would be disastrous - so would the absence of everyday gestures. Gifts are visual representations of love and are treasured greatly."
  elif (topChoice == actsOfService):
      loveLanguageText1 = 'Acts of Service:'
      loveLanguageDescription1 = "Can vacuuming the floors really be an expression of love? Absolutely! Anything you do to ease the burden of responsibilities weighing on 'Acts of Service' person will speak volumes. The words he or she most want to hear: 'Let me do that for you.' Laziness, broken commitments, and making more work for them tell speakers of this language their feelings don't matter. Finding ways to serve speaks volumes to the recipient of these acts." 
   
   
  if (topChoice != secondChoice): 
     
    if (secondChoice == qualityTime):
      loveLanguageText2 = 'Quality Time'
      loveLanguageDescription2 =  'In the vernacular of Quality Time, nothing says, "I love you," like full, undivided attention. Being there for this type of person is critical, but really being there - with the TV off, fork and knife down, and chores and tasks on standby - makes your significant other feel truly special and loved. Distractions, postponed dates, or the failure to listen can be especially hurtful. Quality Time also means sharing quailty conversation and quality activities. ' 
    elif (secondChoice == wordsOfAffirmation):
      loveLanguageText2 = 'Words of Affirmation'
      loveLanguageDescription2 = "Actions don't always speak louder than words. If this is your love language, unsolicited compliments mean the world to you. Hearing the words, 'I' love you,'' are important - hearing the reasons behind that love sends your spirits skyward. Insults can leave you shattered and are not easily forgotten. Kind, encouraging, and positive words are truly life-giving." 
    elif (secondChoice == physicalTouch):
      loveLanguageText2 = 'Physical Touch'
      loveLanguageDescription2 = "This language isn't all about the bedroom. A person whose primary language is Physical Touch is, not surprisingly, very touchy. Hugs, pats on the back, holding hands, and thoughtful touches on the arm, shoulder, or face - they can all be ways to show excitement, concern, care, and love Physical presence and accessibility are crucial, while neglect or abuse can be unforgivable and destructive. Physical touch fosters a sense of security and belonging in any relationship."
    elif (secondChoice == giftGiving):
      loveLanguageText2 = 'Gift Giving'
      loveLanguageDescription2 = "Don't mistake this love language for materialism; the receiver of gifts thrives on the love, thoughtfulness, and effort behind the gift. If you speak this language, the perfect gift or gesture shows that you are known, you are cared for, and you are prized above whatever was sacrificed to bring the gift to you. A missed birthday, anniversary, or a hasty, thoughtless gift would be disastrous - so would the absence of everyday gestures. Gifts are visual representations of love and are treasured greatly."
    elif (secondChoice == actsOfService):
      loveLanguageText2 = 'Acts of Service:'
      loveLanguageDescription2 = "Can vacuuming the floors really be an expression of love? Absolutely! Anything you do to ease the burden of responsibilities weighing on 'Acts of Service' person will speak volumes. The words he or she most want to hear: 'Let me do that for you.' Laziness, broken commitments, and making more work for them tell speakers of this language their feelings don't matter. Finding ways to serve speaks volumes to the recipient of these acts." 
 
  if (topChoice == secondChoice):
    switch = False 
    if (secondChoice == qualityTime and topChoice == qualityTime):
        switch = True
    if (secondChoice == wordsOfAffirmation and topChoice == wordsOfAffirmation):
        if (switch == True):    
          loveLanguageText2 = 'Words of Affirmation'
          loveLanguageDescription2 = "Actions don't always speak louder than words. If this is your love language, unsolicited compliments mean the world to you. Hearing the words, 'I' love you,'' are important - hearing the reasons behind that love sends your spirits skyward. Insults can leave you shattered and are not easily forgotten. Kind, encouraging, and positive words are truly life-giving." 
        elif (switch == False):
            switch = True
    if (secondChoice == physicalTouch and topChoice == physicalTouch):
        if (switch == True):
          loveLanguageText2 = 'Physical Touch'
          loveLanguageDescription2 = "This language isn't all about the bedroom. A person whose primary language is Physical Touch is, not surprisingly, very touchy. Hugs, pats on the back, holding hands, and thoughtful touches on the arm, shoulder, or face - they can all be ways to show excitement, concern, care, and love Physical presence and accessibility are crucial, while neglect or abuse can be unforgivable and destructive. Physical touch fosters a sense of security and belonging in any relationship."
        elif (switch == False):
            switch = True
    if (secondChoice == giftGiving and topChoice == giftGiving):
        if (switch == True):
          loveLanguageText2 = 'Gift Giving'
          loveLanguageDescription2 = "Don't mistake this love language for materialism; the receiver of gifts thrives on the love, thoughtfulness, and effort behind the gift. If you speak this language, the perfect gift or gesture shows that you are known, you are cared for, and you are prized above whatever was sacrificed to bring the gift to you. A missed birthday, anniversary, or a hasty, thoughtless gift would be disastrous - so would the absence of everyday gestures. Gifts are visual representations of love and are treasured greatly."
        elif (switch == False):
            switch = True
    if (secondChoice == actsOfService and topChoice == actsOfService):
        if (switch == True):
          loveLanguageText2 = 'Acts of Service:'
          loveLanguageDescription2 = "Can vacuuming the floors really be an expression of love? Absolutely! Anything you do to ease the burden of responsibilities weighing on 'Acts of Service' person will speak volumes. The words he or she most want to hear: 'Let me do that for you.' Laziness, broken commitments, and making more work for them tell speakers of this language their feelings don't matter. Finding ways to serve speaks volumes to the recipient of these acts." 
 
 # ======= Printing Your Test Results ============= #


  print '                 '
  print '                 '
  print '........Your Test Results.........'
  print '                                  '
  print 'Your Primary Love Language is: ' + loveLanguageText1
  print '                                  '
  print loveLanguageDescription1
  print '                                 '
  print 'Your Secondary Love Language is: ' + loveLanguageText2
  print '                              '
  print loveLanguageDescription2
  

  # ======== Part 2 - Putting your Love Languages Into Action ========= #
  print '            '
  print '            '
  print "Great! Now that you've got your love languages figured out, let's put it into action! Pick either option a or b below. Dont think too hard about it!"
  
  qt_choice = None
  qt_choice1 = None
  qt_choice2 = None
  wa_choice = None
  wa_choice1 = None
  wa_choice2 = None
  as_choice = None
  as_choice1 = None
  as_choice2 = None
  gg_choice = None
  gg_choice1 = None
  gg_choice2 = None 
  pt_choice = None 
  pt_choice1 = None
  pt_choice2 = None
  
  if (topChoice == qualityTime):
    qt_choice = raw_input ("(a) Walk or (b) Drink? > ")
    if (qt_choice == 'a'): 
      qt_choice1 = raw_input ("(a) Trees or (b) Gatherings? > ")
    elif (qt_choice== 'b'):
      qt_choice2 = raw_input ("(a) Above 21 or (b) Under 21? > ")
  if (topChoice == wordsOfAffirmation):
    wa_choice = raw_input ("(a) Praise  or (b) Encouragement? > ")
    if (wa_choice == 'a'): 
      wa_choice1 = raw_input ("Do you want to feel like a (a) superstar or a (b) llama? > ")
    elif (wa_choice== 'b'):
      wa_choice2 = raw_input ("Do you want to feel better (a) in class or (b) in life? > ")
  if (topChoice == actsOfService):
    as_choice = raw_input ("(a) Home or (b) Class? > ")
    if (as_choice == 'a'): 
      as_choice1 = raw_input ("(a) Elves or (b) Fairies? > ")
    elif (as_choice== 'b'):
      as_choice2 = raw_input ("(a) The best spot in town or (b) 'Please wake me up' > ")
  if (topChoice == giftGiving):
    gg_choice = raw_input ("(a) Temporary or (b) Permanent? > ")
    if (gg_choice == 'a'): 
      gg_choice1 = raw_input ("(a) Sweet or (b) Savory? > ")
    elif (gg_choice== 'b'):
      gg_choice2 = raw_input ("something (a) Unexpected or (b) Creative? > ")
  if (topChoice == physicalTouch):
    pt_choice = raw_input ("(a) 'the bro way' or (b) 'the hygienic way'? > ")
    if (pt_choice == 'a'): 
      pt_choice1 = raw_input ("(a) a bro high-five or (b) something suave ;) > ")
    elif (pt_choice == 'b'):
      pt_choice2 = raw_input ("a (a) teddy-bear (b) or 'gone with the wind' > ")
  print '           '
  
  raw_input ('Alrighty, thanks for bearing with us! Our computer will now generate the ideal activity to win your heart based on our complex algorithms. Press enter for your results >')
  print '         '

  print 'Your ideal activity is: '
  
  if (qt_choice1 == 'a'):
    print 'Take me on a walk in Central Park for 30 mins.'
  elif (qt_choice1 == 'b'):
      print 'Take me to an interesting spot in Williamsburg for 30 mins.'
  if (qt_choice2 == 'a'):
      print "Let's have coffee or bubble tea this Thursday after class."
  elif (qt_choice2 == 'b'):
      print "Let's go grab beer or wine this Thursday after class."
  if (wa_choice1 == 'a'):
      print 'Next time we are in the same elevator, say out loud, "You are the superstar of our class!"'
  elif (wa_choice1 == 'b'):
      print 'Next time we are in the same elevator, say out loud, "You would make the coolest llama in Machu Picchu!"'
  if (wa_choice2 == 'a'):
      print 'Next time we are in the same elevator, say out loud, "You are the superstar of our class!"'
  elif (wa_choice2 == 'b'):
      print 'Next time we are in the same elevator, say out loud, "You would make the coolest llama in Machu Picchu!"'
  if (as_choice1 == 'a'):
    print 'Next time you go grocery shopping, carry my bag for me to the subway station!'
  elif (as_choice1 == 'b'):
      print 'At the end of the semester, deep clean and sanitize my desk for me'
  if (as_choice2 == 'a'):
      print 'Save a good seat for me in class for a week! Ask me where I prefer to sit'
  elif (as_choice2 == 'b'):
      print 'Buy 2 coffees for me to keep me awake and energized in class'
  if (gg_choice1 == 'a'):
      print 'Ask me what my favorite sweet snack is! Surprise me with it. :) '
  elif (gg_choice1 == 'b'):
      print 'Ask me what my favorite savory snack is! Surprise me with it. :)'
  if (gg_choice2 == 'a'):
      print 'Suprise me with any gift that you choose!'
  elif (gg_choice2 == 'b'):
      print 'Create a work of art for me to display on my desk!'
  if (pt_choice1 == 'a'):
      print 'Give me a fist bump whenever you see them for a week!'
  elif (pt_choice1 == 'b'):
      print 'Create a secret handshake with me! Show off to our classmates. '
  if (pt_choice2 == 'a'):
      print 'Give me a big bear hug every time you see them for a week.'
  elif (pt_choice2 == 'b'):
      print 'Give me an air kiss across the classroom for a week.'
 


# ============================== Quality Time Game ========================== #

def qualityTimeGame(): 
  repeatFlag = False
  print '                           '
  print 'Welcome to "Day In The Big Apple"!'
  print '                           '
  print 'In this game, we will conquer the quality time love language! The rules are simple: '
  print "Please plan a day in the city!' + partnerName + ' wants to visit the following 5 places in one day. It's a pretty packed itinerary, so you want to optimize the route. You live all the way in Washington Heights (168th St), and want to make your way to the following locations." 
  print "         "
  print "(a) The Strand Bookstore" #12th St
  print "(b) Metropolitan Museum of Art" #82rd
  print "(c) The High Line"#23 St
  print "(d) Grand Central" #42 St 
  print "(e) Momofuku Milk Bar - East Village" #14th St
  print "(f) Levain Bakery" #72nd Street
  print "         "   
  repeatFlag = True 
  
  while (repeatFlag == True):
 
    qualityTimeGameAns = raw_input ('Please order these destinations from uptown to downtown. (for example, enter "abcdef")')
    
    if (qualityTimeGameAns == "bfdcea"):
      print "                                   "
      print "Congratulations! You've planned a successful outing! You've conquered " + partnerName + " 's love language!"
      repeatFlag = False
    else:
      print "                                  "
      print "Oops! That's not the most optimal path! Perhaps you want to try to use google maps to aid in your planning?"
      tryAgain = raw_input ('Try again? (Y/N)')
      if (tryAgain == "Y"):
        repeatFlag = True
      else:
        tryAgain2 = raw_input ("Hmm, are you sure you want to give up so easily?")
        if (tryAgain == "N"):
          repeatFlag = True
        else: 
          repeatFlag = True
          print "Too bad. Love requires persistence! Keep trying!!"

  playAgain = raw_input ('Do you want to play another game? (Y/N): ')
  if (playAgain == "Y"):
    wantToPlay = True
  else: 
    wantToPlay = False


# ============================== Words of Affirmation Game ========================== #

def wordsOfAffirmationGame(): 

  print '                           '
  wordsofAffirmationPoints = 0
  print 'Welcome to "Songs of Affirmation"!'
  print '                           '
  print 'In this game, we will conquer the words of affirmation love language! The rules are simple: '
  print "What better way to express words of love than through song? Please listen to the following 20 second clips of songs with the words 'Love' and 'Heart' and answer the trivia questions associated with these songs! "
  print "If you get 5 correct, then you win!"
  print "                                   "
  time.sleep(3)
  print "......Question 1......."
  print "...Listen to this song..."
  loveStoryAudio.play()
  time.sleep(20)
  print "Who is the artist who sang this song?"
  loveStoryAns = raw_input ("(a) Katy Perry  (b) Taylor Swift (c) Demi Lovato (d) Ariana Grande > ")
  if (loveStoryAns == "b"):
      wordsofAffirmationPoints += 1
      print "              "
      print "Congratulations, you are correct! This is 'Love Story' by Taylor Swift."
      print "                            "
  else:
      print "Sorry! That is incorrect. This is 'Love Story' by Taylor Swift. "
      print "                            "
  print "                                "

  print "......Question 2......."
  print "...Listen to this song..."
  heartlessAudio.play()
  time.sleep(20)
  print "Who is the artist who sang this song?"
  heartlessAns = raw_input ("(a) Eminem  (b) Jay-Z (c) Kanye West (d) Lupe Fiasco > ")
  if (heartlessAns == "c"):
      wordsofAffirmationPoints += 1
      print "Congratulations, you are correct! This is 'Heartless' by Kanye West."
      print "                            "
  else:
      print "Sorry! That is incorrect. This is 'Heartless' by Kanye West. "
      print "                            "

  print "                                "

  print "......Question 3......."
  print "...Listen to this song..."
  myHeartWillGoOnAudio.play()
  time.sleep(20)
  print "Who is the artist who sang this song?"
  myHeartWillGoOnAns = raw_input ("(a) Mariah Carey  (b) Leona Lewis (c) Whitney Houston (d) Celine Dion > ")
  if (myHeartWillGoOnAns == "d"):
      wordsofAffirmationPoints += 1
      print "Congratulations, you are correct! This is 'My Heart Will Go On' by Celine Dion."
      print "                            "
  else:
      print "Sorry! That is incorrect. This is 'My Heart Will Go On' by Celine Dion. "
      print "                            "

  print "                                "

  print "......Question 4......."
  print "...Listen to this song..."
  dontGoBreakingMyHeartAudio.play()
  time.sleep(20)
  print "Who is the artist who sang this song?"
  dontGoBreakingMyHeartAns = raw_input ("(a) Lionel Richie and Diana Ross  (b) Elton John and Kiki Dee (c) The Carpenters (d) Jason Aldean and Kelly Clarkson > ")
  if (dontGoBreakingMyHeartAns == "b"):
      wordsofAffirmationPoints += 1
      print "Congratulations, you are correct! This is 'Don't Go Breaking My Heart by Elton John and Kiki Dee. "
      print "                            "
  else:
      print "Sorry! That is incorrect. This is 'Don't Go Breaking My Heart by Elton John and Kiki Dee. "
      print "                            "

  print "                                "

  print "......Question 5......."
  print "...Listen to this song..."
  loveIsAnOpenDoorAudio.play()
  time.sleep(20)
  print "Who is the artist who sang this song?"
  loveIsAnOpenDoorAns = raw_input ("(a) Idina Menzel  (b) Kristen Bell (c) Mandy Moore (d) Angela Lansbury > ")
  if (loveIsAnOpenDoorAns == "b"):
      wordsofAffirmationPoints += 1
      print "Congratulations, you are correct! This is 'Love Is An Open Door' by Kristen Bell. "
      print "                            "
  else: 
      print "Sorry! That is incorrect. This is 'Love Is An Open Door' by Kristen Bell. "
      print "                            "

  print "                                "

  if (wordsofAffirmationPoints > 4):
      print "Congratulations! You've suceeded in conquering the Words of Affirmation Love Language!"
  else: 
      print "Aw, you didn't win this time. It's okay, love is all about persistence! Try again later!"
  playAgain = raw_input ('Do you want to play another game? (Y/N): ')
  if (playAgain == "Y"):
    wantToPlay = True
  else: 
    wantToPlay = False


# ============================== Acts of Service Game ========================== #

def actsOfServiceGame():
  print '                           '
  print 'Welcome to Acts of Service Design!'
  print '                           '
  print 'In this game, we will conquer the acts of service love language! The rules are simple: '
  print 'Please answer the following trivia questions about our Service Design class with Marshall!'
  print '                           '
  print "Sorry, this game is still under construction!"
  playAgain = raw_input ('Do you want to play another game? (Y/N): ')
  if (playAgain == "Y"):
    wantToPlay = True
  else: 
    wantToPlay = False
  
  
  

# ============================== Gift Giving Game ========================== # 

def giftGivingGame():
  print '                           '
  print 'Welcome to "re-Present-ation"!'
  print '                           '
  print 'In this game, we will conquer the gift giving love language! The rules are simple: '
  print '                           '
  print "Sorry, this game is still under construction!"
  playAgain = raw_input ('Do you want to play another game? (Y/N): ')
  if (playAgain == "Y"):
    wantToPlay = True
  else: 
    wantToPlay = False
  

# ============================== Physical Touch  Game ========================== #

def physicalTouchGame():

  print '                           '
  print 'Welcome to "Awkward Contact"!'
  print '                           '
  print "Sorry, this game is still under construction!"
  playAgain = raw_input ('Do you want to play another game? (Y/N): ')
  if (playAgain == "Y"):
    wantToPlay = True
  else: 
    wantToPlay = False  
  #print 'In this game, we will conquer the physical touch love language! The rules are simple: '
  #print "We will present you with a few potentially awkward social situations! Your goal is to reciprocate appropriately."
  #raw_input = "For example, your creepy uncle Mel is coming towards you. How will he approach? > "
  #print " You will need to guess if he will come in for (a) a dead fish handshake (b) an awkward side hug (c) a peck on the cheek (d) hug that lasts just a little bit too long? > "

  #print "... Question 1 ... "
  #print " What will Bob the Businessman do?"
  #print "                                  "
  #bobGuess = raw_input('(a) a dead fish handshake (b) an awkward side hug (c) a peck on the cheek (d) hug that lasts just a little bit too long? >')
  
  #bobChoice = random.randint(1,4)
  #if (bobChoice == 1):
  #  bobContact = "a"
  #if (bobChoice ==2):
  #  bobContact = "b"
  #if (bobChoice ==3):
  #  bobContact = "c"
  #if (bobChoice ==4):
  #  bobContact = "d"
  #if (bobGuess == bobContact):
  #  print "Yay good job! You guessed correctly. :)"
  #  print "                                       "
  #else: 
  #  print "Boo, you guessed incorrectly..."
  #  print "                              "
  #print "... Question 2 ... "
  #print " What will Lisa the Librarian do?"
  #print "                                  "
  #lisaChoice = random.randint(1,4)
  #if (lisaChoice == 1):
  #  lisaContact = "a"
 # if (lisaChoice ==2):
  #  lisaContact = "b"
  #if (lisaChoice ==3):
 #   lisaContact = "c"
 # if (lisaChoice ==4):
 #   lisaContact = "d"
 # lisaGuess = raw_input ('(a) a dead fish handshake (b) an awkward side hug (c) a peck on the cheek (d) hug that lasts just a little bit too long? >')
#  if (lisaGuess == lisaContact):
 #   print "Yay good job! You guessed correctly. :)"
  #  print "                                       "
  #else: 
  #  print "Boo, you guessed incorrectly..."
  #  print "                              "

  #print "... Question 3 ... "
 # print " What will Henry the Hedge Fund Manager do?"
 # print "                                  "
 # henryChoice = random.randint(1,4)
 # if (henryChoice == 1):
 #   henryContact = "a"
 # if (henryChoice ==2):
 #   henryContact = "b"
 # if (henryChoice ==3):
 #   henryContact = "c"
 # if (henryChoice ==4):
  #  henryContact = "d"
 # henryGuess = raw_input ('(a) a dead fish handshake (b) an awkward side hug (c) a peck on the cheek (d) hug that lasts just a little bit too long? >')
 # if (lisaGuess == lisaContact):
 #   print "Yay good job! You guessed correctly. :)"
#    print "                                       "
#  else: 
#    print "Boo, you guessed incorrectly..."
 #   print "                              "


wantToPlay = True
playAgain = 'Y'
intro()
quiz()




# ========================== Playing Games ========================#
print '              '
print '              '
raw_input ("Great! Now let's go on a quest to conquer someone else's heart! Turn to your neighbor or friend. > ")

partnerName = raw_input ("What is their name? > ")
print "            "
  
while (wantToPlay == True):
  print "            "
  print "What is " + partnerName + "'s love language?"
  print "(a) Quality Time"
  print "(b) Words of Affirmation"
  print "(c) Acts of Service"
  print "(d) Gift Giving"
  gameChoice = raw_input ("(e) Physical Touch > ")

  if (gameChoice == "a"):
    qualityTimeGame()
  if (gameChoice == "b"):
    wordsOfAffirmationGame()
  if (gameChoice == "c"):
    actsOfServiceGame()
  if (gameChoice == "d"):
    giftGivingGame()
  if (gameChoice == "e"):
    physicalTouchGame()











