import random
def mad_libs():
    """
    A simple text-based Mad Libs game.
    """
    print("📝 Welcome to Mad Libs! Please provide the following words:")
    
    # 1. Gather all the required input from the user
    # Using .strip() ensures no extra spaces are included
noun_1 = input("Enter a Noun (person, place, or thing): ").strip()
adjective_1 = input("Enter an Adjective (describing word): ").strip()
verb_past_tense = input("Enter a Verb in Past Tense: ").strip()
adverb = input("Enter an Adverb (describes a verb, ends in -ly): ").strip()
place = input("Enter a Name of a Place: ").strip()
plural_noun = input("Enter a Plural Noun: ").strip()
noun_2 = input("Enter another Noun: ").strip()
    
print("\n--- Generating Your Story ---")
    
    # Optional: Add a short pause for a dramatic effect
import time
time.sleep(1.5) 
    
    # 2. The core story template using f-strings
    # The user's input variables are placed inside the {} braces.
    
story_1 = (
        f"A young {noun_1} was having a very {adjective_1} day at the college. "
        f"They suddenly {verb_past_tense} {adverb} across the campus, heading straight for the "
        f"{place}. They were trying to escape from a horde of angry {plural_noun}, "
        f"who wanted to steal their precious **{noun_2}**! "
        f"They knew they had to be fast to survive the day."
    )

story_2 = (
        f"Last weekend, I decided to visit the famous {place}. "
        f"I packed a single, very **{adjective_1}** {noun_1} and set off on my journey. "
        f"As soon as I arrived, I saw a crowd of wild **{plural_noun}** running "
        f"away from a tiny old {noun_2}. It seems the {plural_noun} had been "
        f"trying to steal the {noun_2} and failed! "
        f"The tiny {noun_2} then {verb_past_tense} **{adverb}** toward me, giving me "
        f"a triumphant wink before disappearing around a corner."
    )

story_3 = (
        f"During my first week at college, I discovered the secret back entrance to the "
        f"cafeteria, located right next to the **{place}**. "
        f"I was carrying a heavy, **{adjective_1}** **{noun_1}** and trying to sneak past the guards. "
        f"Suddenly, a huge stampede of **{plural_noun}** came running at me! "
        f"I quickly **{verb_past_tense}** to the side and hid behind a giant **{noun_2}**. "
        f"The cafeteria manager looked at me **{adverb}** and simply shrugged, "
        f"as if this was a normal Tuesday. I realized college was going to be an adventure!"
    )

story_4 = (
        f"It was a quiet afternoon in the main library at **{place}**. I was studying my "
        f"most **{adjective_1}** **{noun_1}** when I noticed something strange. "
        f"A flock of **{plural_noun}** were gathered around a massive **{noun_2}**. "
        f"The smallest {plural_noun} suddenly **{verb_past_tense}** into the air, "
        f"holding a library book titled 'The Art of Python'. "
        f"The librarian looked up **{adverb}** from her desk, sighed, and muttered: "
        f"'Not again! That's the third time this week they've tried to steal that book.'"        
    )
all_stories = [story_1, story_2, story_3, story_4]
final_story = random.choice(all_stories)
    # 3. Print the final, completed story
print("\n" + "=" * 40)
print("✨ **Your Mad Libs Story** ✨")
print("=" * 40)
print(final_story)
print("=" * 40)
