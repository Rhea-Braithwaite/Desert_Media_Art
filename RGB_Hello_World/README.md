## Concept/Intention
The idea behind the work is to show the progression of an unhealthy relationship using a single LED light.

The overarching story is that a solitary individual (Blue) meets a new person (Yellow), and eventually develops a crush. This crush then transforms into a relationship between Blue and Yellow, which is signified by the Bright Pink. However, their relationship is not always great as we see more and more that hurt and pain begins to infiltrate, shown by the color Red. Eventually, the relationship ends in a clean break, with a rush of White light. But unfortunately the cycle then begins again.  

To reiterate the colors that are used and their meaning are as follows
- Blue: Solitude and loneliness of one party
- Yellow: The hope that comes with meeting someone new
- Light Pink: Developing a crush for this new individual
- Bright Pink: Crush becoming a full blown relationship
- Red: Dangerous elements of the relationship which surface
- White: A clean break, and end to the relationship

## Animations
My primary concern when developing the animations was to not lose the different characters and emotions in the story. With a single LED, if you look away for a single moment and look back, you may have missed something. So I felt it useful to repeat the previous colors to highlight the meaning when new colors are introduced. 

### Animation 1
- Blue then Yellow
- Blue, Yellow, then Light Pink (repeated twice)
- Meaning: Blue and Yellow are introduced. Blue develops a crush on Yellow. Therefore, repeating the meeting of these characters and the introduction of the new emotion, Light Pink.  
### Animation 2
- Blue then Yellow
- Followed by Bright Pink, and Red (repeated three twice)
- Meaning: Introducing the unhealthy component (Red) into the relationship. Initially, the healthy section (Bright Pink) is longer than the Red, but eventually, Bright Pink begins to be shorter, and the Red, longer. 

## Code
A part of the code that I really enjoyed writing is where the relationship begins to become unhealthy. I used two variables to represent the initial time lengths for the different colors, Bright Pink: 5 seconds, Red: 1 second. With a loop, I used math calculations to reduce the Bright Pink time and increase the Red time on each iteration. This signifies that the love is being overshadowed by the abuse and danger that has presented itself. 
```
    brightPink_time = 5
    red_time = 1

    #Loop as the relationship becomes unhealthy
    #Bright Pink becomes shorter and Red becomes longer
    for i in range (0, 3):
        led[0] = (255, 0, 102) #Pink = Full relationship
        time.sleep(brightPink_time - (2*i))
        led[0] = (139, 0, 0) # Red = Abusive elements
        time.sleep(red_time + (2*i))
```
## What I achieved
I think I was able to develop a solid story and it is a really important one, given the continued occurrence of abusive relationships. Ultimately, it is a tragedy, as the code begins again and so the main character is stuck in a cycle of loneliness, hope, initial love, danger, and then escape.

I was a bit intimidated because we had to use only one LED-light, but I think it makes the story more open-ended. There are no restrictions placed on the background of the characters, as it is primarily their emotions that are shown, therefore many different viewers may be able to place themselves within the story. Moreover, the abuse (Red) isn’t shown to be done by a specific party, which leaves it open to interpretation as well. I believe it could be developed further to include two separate paths. Using a sensor to detect the light, if it is brighter, a more optimistic story is displayed using the LED. However, if it's darker, the more tragic story is told.  

