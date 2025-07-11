
# My Chatbot
------------


# Initial Workflow

* Because of VRAM limitations, i've only been able to try flan-t5-small, flan-t5-large and DialoGPT, out of which flan-t5-large seems to be working marginally better although it's still not very reliable. flan-t5-xxl could produce even better results potentially.

* I ran into severe GPU limitations while trying to fine-tune. A better GPU can potentially train flan-t5-large, but i'll stick to base for now.

* I tried translations using the bot and it seems to be consistently working better when translating German, probably because it was trained on English-German sentence pairs.

# TO DO:

1) [✔️] Migrate to python file in chatbot/
2) [✔️] Wrap in class
3) [✔️] Work on Gradio UI
4) [😕] Fine Tune Using Yahoo QA dataset -> Train Overnight
5) [😕] After Training the model -> Update the chatbot.py file to use the latest checkpoint (now do-able from app.py)
6) [➖] Train the flan-t5-base model overnight
7) [➖] Update app.py to use the latest checkpoint after fine-tuning on flan-t5-base

***Legend***
✔️: Done
➖: Not Done (yet)
😞: Done, but at what cost
😕: Done? Maybe?


# Updates

**Update**: For simplicity's sake, i decided to stick with flan-t5-small, because i was running into Value Errors. I was able to get the model to be fine-tuned, though i'm not getting any loss values, which may be because i commented out the rouge score metric line. The bot is giving me a migraine so i think i'm going to stop for now.

**Update2**: I finally got the training to work properly, and also got the rouge scores and losses to be computed properly. This time the training actually worked, i think. Some of the changes i made was turning fp16=False in the train_args and also i changed how the rouge score was calculated because i was having a problem with the nltk.download('punkt'), so i made the sent_tokenize function manual instead of using nltk's version.


# Instructions:
**1)** Run 'python ui/app.py' and open the internal link supplied.
**2)** Using chat history for the conversations works but may not be supported very well by the model and may result in weirder responses. I recommend keeping it turning it on only for experimental purposes. 