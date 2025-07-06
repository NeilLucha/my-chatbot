import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class Chatbot:
    def __init__(self, model_name='google/flan-t5-large'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)
        self.chat_history = []
        self.history_length = 5  # Default history length

    def format_chat_history(self, history):
        history_length = min(self.history_length, len(history))
        return '\n'.join(history[-history_length:])

    def generate_response(self, input_sequence):
        
        '''
        Generates a response from the model based on the input sequence.
        This method tokenizes the input sequence, generates a response using the model,
        and decodes the output to return a human-readable response.
        '''
        
        inputs = self.tokenizer(input_sequence, return_tensors='pt').to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_length=100,
            do_sample=True,
            top_p=0.95,
            top_k=50,
            temperature=0.7,)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def add_to_chat_history(self, input_sequence):
        
        '''
        Generates Response using the chat history.
        This method appends the user's input to the chat history,
        formats the chat history, and generates a response from the model.
        The response is then appended to the chat history.
        '''
        
        
        
        self.chat_history.append('user: ' + input_sequence)
        formatted = self.format_chat_history(self.chat_history)
        response = self.generate_response(formatted + '\nbot: ')
        self.chat_history.append('bot: ' + response)
        
        #Trim the actual chat history to the last 2 * history_length messages
        # This is to ensure that the chat history does not grow too large.
        
        if len(self.chat_history) > self.history_length * 2:
            self.chat_history = self.chat_history[-self.history_length * 2:]
        
        return response
    
    def get_response(self, input_sequence):
        '''
        Get a direct response from the chatbot.
        This method is used to get a response without using the chat history.
        '''
        
        return self.generate_response(input_sequence)
    
    def clear_chat_history(self):
        '''
        Clears the chat history.
        This method is used to reset the chat history.
        '''
        
        self.chat_history = []
        return "Chat history cleared."
    
    def set_history_length(self, length):
        '''
        Sets the length of the chat history to be used for formatting.
        This method allows the user to specify how many previous messages to consider.
        '''
        
        if length > 0:
            self.history_length = length
            return f"Chat history length set to {length}."
        else:
            return "History length must be a positive integer."