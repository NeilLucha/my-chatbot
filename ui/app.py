import gradio as gr
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chatbot.chatbot import Chatbot

bot = Chatbot(checkpoint_path='model/checkpoint-58971')

# Chat function updated to account for checkbox


def reset_chat():
    """
    Function to reset the chat history.
    """
    bot.clear_chat_history()
    return [], []

with gr.Blocks() as demo:
    gr.Markdown(f"# Chatbot Interface - {bot.model_name}")
    
    with gr.Row():
        chatbot = gr.Chatbot(label="Chatbot", value=[])
        user_input = gr.Textbox(label="Your Message", placeholder="Type your message here...")

    with gr.Row():
        use_history = gr.Checkbox(label="Use chat history (Experimental)", value=False)
    
    with gr.Row():
        send_button = gr.Button("Send")
        reset_button = gr.Button("Reset Chat")
    
    chat_state = gr.State([])
    
    def chat(user_input, chat_history, use_history_flag):
        if use_history_flag:
            response = bot.add_to_chat_history(user_input)
            chat_history = chat_history + [(user_input, response)]
        else:
            response = bot.get_response(user_input)
            chat_history = chat_history + [(user_input, response)]
        return "", chat_history, chat_history
    
    send_button.click(chat, inputs=[user_input, chat_state, use_history], outputs=[user_input, chatbot, chat_state])
    reset_button.click(fn=reset_chat, outputs=[chatbot, chat_state])  
    
if __name__ == "__main__":
    demo.launch()