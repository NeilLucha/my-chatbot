# my-chatbot

Because of VRAM limitations, i've only been able to try flan-t5-small, flan-t5-large and DialoGPT, out of which flan-t5-large seems to be working marginally better although it's still not very reliable. flan-t5-xxl could produce even better results potentially.

I ran into severe GPU limitations while trying to fine-tune. A better GPU can potentially train flan-t5-large, but i'll stick to base for now.

I tried translations using the bot and it seems to be consistently working better when translating German, probably because it was trained on English-German sentence pairs.

TO DO:

1) [✔️] Migrate to python file in chatbot/
2) [✔️] Wrap in class
3) [] Work on Gradio UI
4) [😐] Fine Tune Using Yahoo QA dataset -> Train Overnight
5) [😐] After Training the model -> Update the chatbot.py file to use the latest checkpoint
